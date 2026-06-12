"""Tests for fire-and-forget notification dispatch (audit Tier 3.2)."""
from __future__ import annotations

import time

from helix_v3.notifications.dispatch import fire_and_forget


def test_function_runs_on_worker() -> None:
    hits = []
    fut = fire_and_forget(hits.append, "sent", description="test")
    fut.result(timeout=5)
    assert hits == ["sent"]


def test_exceptions_are_swallowed() -> None:
    def _boom() -> None:
        raise RuntimeError("twilio down")

    fut = fire_and_forget(_boom, description="test")
    # The wrapper logs and absorbs — result() must not raise
    assert fut.result(timeout=5) is None


def test_single_worker_preserves_order() -> None:
    seen = []

    def _slow_then_record(tag: str) -> None:
        time.sleep(0.02)
        seen.append(tag)

    futures = [
        fire_and_forget(_slow_then_record, f"msg{i}", description="test")
        for i in range(5)
    ]
    for f in futures:
        f.result(timeout=5)
    assert seen == [f"msg{i}" for i in range(5)]


def test_kwargs_pass_through() -> None:
    out = {}

    def _record(key: str, value: int = 0) -> None:
        out[key] = value

    fire_and_forget(_record, "a", value=7, description="test").result(timeout=5)
    assert out == {"a": 7}
