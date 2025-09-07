"""Append a trading signal to signals/today.json."""

"""Append a trading signal to signals/today.json."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TODAY_FILE = ROOT / "signals" / "today.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Append a signal")
    parser.add_argument("--market", required=True)
    parser.add_argument("--timeframe", required=True)
    parser.add_argument("--mode", required=True)
    parser.add_argument("--entry", type=float, required=True)
    parser.add_argument("--sl", type=float, required=True)
    parser.add_argument("--tp", type=float, required=True)
    parser.add_argument("--confidence", type=int, required=True)
    parser.add_argument("--basis", required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    with open(TODAY_FILE, "r", encoding="utf-8") as fh:
        signals = json.load(fh)
    signals.append(
        {
            "market": args.market,
            "timeframe": args.timeframe,
            "mode": args.mode,
            "entry": args.entry,
            "sl": args.sl,
            "tp": args.tp,
            "confidence": args.confidence,
            "basis": args.basis,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
    )
    with open(TODAY_FILE, "w", encoding="utf-8") as fh:
        json.dump(signals, fh, indent=2)
        fh.write("\n")


if __name__ == "__main__":  # pragma: no cover
    main()

