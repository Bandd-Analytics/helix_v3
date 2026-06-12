"""One-off survey: current regime state for every configured instrument.

Run by hand: .venv/Scripts/python.exe tools/manual/regime_survey.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from config.pair_profiles import PAIR_PROFILES
from helix_v3.core.quant_engine import MMMQuantitativeEngine
from helix_v3.core.regime import assess_regime


def main() -> None:
    eng = MMMQuantitativeEngine()
    if not eng.connect():
        print("MT5 connect failed")
        return
    for sym in PAIR_PROFILES:
        s = assess_regime(eng, sym)
        flag = "PRESENT" if s.mmm_present else "ABSENT "
        print(f"{sym:8} {flag} volP={s.vol_percentile:.2f} ER={s.efficiency_ratio:.2f}  {s.reason}")


if __name__ == "__main__":
    main()
