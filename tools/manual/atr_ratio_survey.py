"""One-off survey: ATR(20, D1) per pair vs the static profile gate values.

Prints the implied ratio (static_value / ATR) for each of the 8 gate fields
so universal GateRatios for Tier 2.3 are grounded in data, not invented.
Run by hand: .venv/Scripts/python.exe tools/manual/atr_ratio_survey.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import numpy as np

from config.pair_profiles import PAIR_PROFILES
from helix_v3.core.quant_engine import MMMQuantitativeEngine
from helix_v3.core.tdi import _wilder_atr

FIELDS = [
    "asian_range_max_pips",
    "stop_hunt_min_pips",
    "stop_hunt_max_pips",
    "expected_level_move_pips",
    "trail_activation_pips",
    "trail_distance_pips",
    "sl_buffer_pips",
    "min_sl_pips",
]


def main() -> None:
    eng = MMMQuantitativeEngine()
    if not eng.connect():
        print("MT5 connect failed")
        return

    ratios: dict[str, list[float]] = {f: [] for f in FIELDS}
    print(f"\n{'Pair':8} {'ATR20p':>8} " + " ".join(f"{f.split('_pips')[0][:12]:>13}" for f in FIELDS))

    for sym, pp in PAIR_PROFILES.items():
        try:
            df = eng.fetch_rates(sym, "D1", 40)
            pip = eng._get_pip_value(sym)
            atr = float(_wilder_atr(df["High"], df["Low"], df["Close"], 20).iloc[-1]) / pip
        except Exception as e:
            print(f"{sym:8} - skipped ({e})")
            continue
        row = []
        for f in FIELDS:
            r = getattr(pp, f) / atr if atr > 0 else float("nan")
            row.append(r)
            # Medians from FX pairs only — gold/indices magic numbers are
            # exactly what the audit called vacuous.
            if sym not in ("XAUUSD", "US30", "USTEC"):
                ratios[f].append(r)
        print(f"{sym:8} {atr:8.1f} " + " ".join(f"{r:13.3f}" for r in row))

    print(f"\n{'MEDIAN(FX)':17} " + " ".join(f"{np.median(ratios[f]):13.3f}" for f in FIELDS))
    print(f"{'MEAN(FX)':17} " + " ".join(f"{np.mean(ratios[f]):13.3f}" for f in FIELDS))


if __name__ == "__main__":
    main()
