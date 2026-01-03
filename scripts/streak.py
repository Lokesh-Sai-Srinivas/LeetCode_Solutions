from pathlib import Path
import json
from datetime import datetime, timedelta

ROOT = Path(".")
DAILY = ROOT / "daily-challenges"
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

OUTPUT = ASSETS / "streak.json"

def get_dates():
    dates = set()

    for meta in DAILY.rglob("meta.json"):
        try:
            data = json.loads(meta.read_text(encoding="utf-8"))
            if "date" in data:
                dates.add(datetime.strptime(data["date"], "%Y-%m-%d").date())
        except Exception:
            continue

    return sorted(dates)

def compute_streaks(dates):
    if not dates:
        return 0, 0

    longest = 1
    current = 1
    temp = 1

    for i in range(1, len(dates)):
        if dates[i] == dates[i - 1] + timedelta(days=1):
            temp += 1
            longest = max(longest, temp)
        else:
            temp = 1

    today = datetime.utcnow().date()
    current = 0
    for d in reversed(dates):
        if d == today or d == today - timedelta(days=current):
            current += 1
        else:
            break

    return current, longest

def main():
    dates = get_dates()
    current, longest = compute_streaks(dates)

    OUTPUT.write_text(
        json.dumps(
            {
                "current_streak": current,
                "longest_streak": longest,
                "total_active_days": len(dates),
                "updated_at": datetime.utcnow().isoformat(),
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    print(f"🔥 Streak updated → current: {current}, longest: {longest}")

if __name__ == "__main__":
    main()
