from pathlib import Path
import json
from datetime import date, timedelta

DAILY = Path("daily-challenges")

def get_all_dates():
    dates = set()
    for meta in DAILY.rglob("meta.json"):
        data = json.loads(meta.read_text(encoding="utf-8"))
        dates.add(date.fromisoformat(data["date"]))
    return sorted(dates)

def compute_streaks():
    days = get_all_dates()
    if not days:
        return 0, 0

    max_streak = cur = 1
    for i in range(1, len(days)):
        if days[i] == days[i - 1] + timedelta(days=1):
            cur += 1
            max_streak = max(max_streak, cur)
        else:
            cur = 1

    # current streak (ending today or yesterday)
    today = date.today()
    if days[-1] not in (today, today - timedelta(days=1)):
        cur = 0

    return cur, max_streak
