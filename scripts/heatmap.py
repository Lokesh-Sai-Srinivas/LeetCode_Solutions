from pathlib import Path
import json
from collections import defaultdict
from datetime import datetime

ROOT = Path(".")
DAILY = ROOT / "daily-challenges"
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

OUTPUT = ASSETS / "heatmap.json"

def collect_dates():
    counts = defaultdict(int)

    for meta in DAILY.rglob("meta.json"):
        try:
            data = json.loads(meta.read_text(encoding="utf-8"))
            date = data.get("date")
            if date:
                counts[date] += 1
        except Exception:
            continue

    return dict(sorted(counts.items()))

def main():
    data = collect_dates()
    OUTPUT.write_text(
        json.dumps(
            {
                "generated_at": datetime.utcnow().isoformat(),
                "days": data,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"🔥 Heatmap generated: {OUTPUT} ({len(data)} active days)")

if __name__ == "__main__":
    main()
