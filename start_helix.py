"""Helix V3 Launcher - runs the orchestrator as a persistent process."""

import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).parent
VENV_PYTHON = BASE / ".venv" / "Scripts" / "python.exe"
LOG_FILE = BASE / "logs" / "orchestrator.log"

LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

print(f"Starting Helix V3 orchestrator...")
print(f"Python: {VENV_PYTHON}")
print(f"Log: {LOG_FILE}")

with open(LOG_FILE, "a") as log:
    proc = subprocess.Popen(
        [str(VENV_PYTHON), "-m", "helix_v3.orchestrator"],
        cwd=str(BASE),
        stdout=log,
        stderr=subprocess.STDOUT,
        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS,
    )

print(f"Orchestrator started with PID: {proc.pid}")
print(f"Monitor: tail -f logs/orchestrator.log")
print(f"Stop: taskkill /PID {proc.pid} /F")
