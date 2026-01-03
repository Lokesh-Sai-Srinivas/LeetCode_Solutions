from pathlib import Path
import json
from datetime import datetime, timedelta

ROOT = Path(__file__).resolve().parents[1]
DAILY = ROOT / "daily-challenges"
README = ROOT / "README.md"

def collect_dates():
    dates = set()
    for meta in DAILY.rglob("meta.json"):
        try:
            data = json.loads(meta.read_text(encoding="utf-8"))
            if "date" in data:
                dates.add(datetime.strptime(data["date"], "%Y-%m-%d").date())
        except Exception:
            pass
    return sorted(dates)

def compute_streaks(dates):
    if not dates:
        return 0, 0

    longest = 1
    current = 1
    today = dates[-1]

    streak = 1
    for i in range(1, len(dates)):
        if dates[i] == dates[i-1] + timedelta(days=1):
            streak += 1
            longest = max(longest, streak)
        else:
            streak = 1

    # current streak (ending today or yesterday)
    if today >= datetime.today().date() - timedelta(days=1):
        current = streak
    else:
        current = 0

    return current, longest

def update_readme(current, longest):
    content = f"""
🔥 **Daily Streak**
- 🔥 Current streak: **{current} days**
- 🏆 Longest streak: **{longest} days**
""".strip()

    text = README.read_text(encoding="utf-8")

    start = "<!-- STREAK:START -->"
    end = "<!-- STREAK:END -->"

    if start in text and end in text:
        before = text.split(start)[0]
        after = text.split(end)[1]
        text = before + start + "\n\n" + content + "\n\n" + end + after
    else:
        text += f"\n\n{start}\n\n{content}\n\n{end}"

    README.write_text(text, encoding="utf-8")

if __name__ == "__main__":
    dates = collect_dates()
    current, longest = compute_streaks(dates)
    update_readme(current, longest)
