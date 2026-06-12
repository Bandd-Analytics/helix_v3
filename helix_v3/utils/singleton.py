"""PID-lockfile singleton helper.

Refuses to start if another live process holds the lock. Stale locks (PID
no longer alive) are taken over. Lock is released via atexit on graceful exit;
on SIGKILL the next start will detect a stale PID and reclaim.

Also provides a check for multiple MT5 terminals connected to the same account —
the previous dual-instance incident caused trades to be opened and session-exited
within seconds because two terminals were both attached to account 52846409.
"""
from __future__ import annotations

import atexit
import ctypes
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional, Tuple

from config.settings import settings
from helix_v3.utils.logger import get_logger

logger = get_logger("singleton")


def _pid_alive(pid: int) -> bool:
    """Return True if a process with this PID exists."""
    if pid <= 0:
        return False
    if sys.platform == "win32":
        # PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
        handle = ctypes.windll.kernel32.OpenProcess(0x1000, False, pid)
        if not handle:
            return False
        try:
            exit_code = ctypes.c_ulong()
            ok = ctypes.windll.kernel32.GetExitCodeProcess(handle, ctypes.byref(exit_code))
            if not ok:
                return False
            # STILL_ACTIVE = 259. If the process exited with code 259 we'd misreport,
            # but that's an acceptable trade for not pulling psutil.
            return exit_code.value == 259
        finally:
            ctypes.windll.kernel32.CloseHandle(handle)
    try:
        os.kill(pid, 0)
        return True
    except (OSError, ProcessLookupError):
        return False


def acquire_singleton_lock(name: str = "orchestrator") -> Optional[Path]:
    """Acquire an exclusive PID-based lock named `<log_dir>/<name>.lock`.

    Returns the lock Path on success, or None if another live instance holds it.
    Registers atexit cleanup on success.
    """
    lock_dir = Path(settings.log_dir)
    lock_dir.mkdir(parents=True, exist_ok=True)
    lock_path = lock_dir / f"{name}.lock"

    if lock_path.exists():
        existing_pid = -1
        try:
            content = lock_path.read_text(encoding="utf-8").strip()
            existing_pid = int(content.split()[0])
        except (OSError, ValueError) as e:
            logger.warning("Lock file unreadable, removing: %s", e)
            try:
                lock_path.unlink()
            except OSError:
                pass

        if existing_pid > 0 and _pid_alive(existing_pid):
            logger.critical(
                "REFUSING TO START: another %s instance is alive (PID %d). "
                "Stop it first or delete %s if you're sure it's dead.",
                name, existing_pid, lock_path,
            )
            return None

        if existing_pid > 0:
            logger.warning("Stale %s lock from dead PID %d — reclaiming.", name, existing_pid)
            try:
                lock_path.unlink()
            except OSError:
                pass

    # O_EXCL create — races with any other process trying simultaneously
    try:
        fd = os.open(str(lock_path), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        logger.critical("Lost race for %s — another instance grabbed the lock.", name)
        return None

    try:
        os.write(
            fd,
            f"{os.getpid()} {datetime.now(timezone.utc).isoformat()}\n".encode("utf-8"),
        )
    finally:
        os.close(fd)

    def _cleanup() -> None:
        try:
            # Only delete if it's still our PID — protects against takeover races
            content = lock_path.read_text(encoding="utf-8").strip()
            owner = int(content.split()[0])
            if owner == os.getpid():
                lock_path.unlink()
        except (OSError, ValueError):
            pass

    atexit.register(_cleanup)
    logger.info("Acquired %s singleton lock (PID %d) at %s", name, os.getpid(), lock_path)
    return lock_path


def list_mt5_terminals() -> List[Tuple[int, str]]:
    """Return (pid, window_title) for every running terminal64.exe on the system.

    Uses tasklist with verbose output so we can read the window title — that's
    where MT5 puts the account number, e.g. ``52846409 - ICMarketsKE-Demo - Hedge``.
    Empty list on non-Windows or if tasklist isn't available.
    """
    if sys.platform != "win32":
        return []
    try:
        # /v gives window title (last column); /fo csv quotes each field; /nh skips header.
        result = subprocess.run(
            ["tasklist", "/v", "/fi", "imagename eq terminal64.exe", "/fo", "csv", "/nh"],
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        logger.debug("tasklist failed, can't enumerate MT5 terminals: %s", e)
        return []

    out: List[Tuple[int, str]] = []
    for line in result.stdout.splitlines():
        line = line.strip()
        if not line or 'INFO:' in line:
            continue
        # CSV row: "terminal64.exe","41364","Console","1","156,392 K","Running","DESKTOP","0:00:00","Window Title"
        import csv
        from io import StringIO
        try:
            row = next(csv.reader(StringIO(line)))
        except StopIteration:
            continue
        if len(row) < 9:
            continue
        try:
            pid = int(row[1])
        except ValueError:
            continue
        title = row[-1]
        out.append((pid, title))
    return out


def check_mt5_account_conflict(account_login: int) -> Optional[str]:
    """Return a warning string if multiple MT5 terminals are bound to ``account_login``.

    This is informational. Having two terminals open on the same account is
    sometimes intentional (e.g. one for monitoring, one for execution) — the real
    risk is two *orchestrator* processes, which the PID singleton lock catches.
    Use ``verify_connected_server`` after ``mt5.initialize()`` for the strict check
    that we're actually executing on the expected broker.
    """
    terminals = list_mt5_terminals()
    if not terminals:
        return None
    needle = str(account_login)
    matching = [(pid, title) for pid, title in terminals if needle in title]
    if len(matching) <= 1:
        return None
    pid_list = ", ".join(f"PID {pid}" for pid, _ in matching)
    titles = " | ".join(f'"{t}"' for _, t in matching)
    return (
        f"{len(matching)} MT5 terminals show account {account_login} in their title "
        f"({pid_list}). Trades will route through whichever terminal mt5.initialize() "
        f"connects to. Server-match check on connect will hard-fail if it's the wrong one. "
        f"Windows: {titles}"
    )


def verify_connected_server(expected_server: str, expected_login: int) -> Optional[str]:
    """After mt5.initialize(), confirm we connected to the intended account/server.

    Returns None on match, an error string on mismatch. This is the real safety
    check — if the user has two terminals running and Python picks the wrong one,
    we must refuse to trade rather than write orders to the wrong account.
    """
    import MetaTrader5 as mt5  # local import — orchestrator already imports it

    info = mt5.account_info()
    if info is None:
        return "mt5.account_info() returned None — cannot verify server"
    if info.login != expected_login:
        return (
            f"Connected to login {info.login} but .env expects {expected_login}. "
            f"Server reports '{info.server}'. Refusing to trade on the wrong account."
        )
    if expected_server and info.server != expected_server:
        return (
            f"Connected to server '{info.server}' but .env expects '{expected_server}' "
            f"(login {info.login} matches). Likely the wrong MT5 terminal got picked. "
            f"Close the other terminal or change .env to match."
        )
    return None
