"""Instrument unit helpers for pip and tick-value calculations."""

from __future__ import annotations

from typing import Optional

INDEX_FALLBACK_PIP_SIZES = {
    "US30": 0.01,
    "USTEC": 0.01,
}


def pip_size_from_digits(*, point: float, digits: int) -> float:
    if point <= 0:
        return 0.0
    return point * (10 if digits in (3, 5) else 1)


def fallback_pip_size(symbol: str) -> float:
    normalized = symbol.upper()
    if "JPY" in normalized:
        return 0.01
    if normalized.startswith("XAU"):
        return 0.01
    if normalized in INDEX_FALLBACK_PIP_SIZES:
        return INDEX_FALLBACK_PIP_SIZES[normalized]
    return 0.0001


def pip_value_per_lot(
    *,
    pip_size: float,
    tick_size: float,
    tick_value: float,
) -> Optional[float]:
    if pip_size <= 0 or tick_size <= 0 or tick_value <= 0:
        return None
    return (pip_size / tick_size) * tick_value
