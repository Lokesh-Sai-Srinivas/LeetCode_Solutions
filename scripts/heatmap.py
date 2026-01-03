from pathlib import Path
import json
from collections import defaultdict
from datetime import date, timedelta

# ---------- PATHS ----------
ROOT = Path(__file__).resolve().parents[1]
DAILY = ROOT / "daily-challenges"
README = ROOT / "README.md"

START = "<!-- HEATMAP:START -->"
END = "<!-- HEATMAP:END -->"

ACTIVE = "🟩"
EMPTY = "⬜"

WEEKS = 13  # ~90 days

def load_activity():
    activity = defaultdict(int)
    if not DAILY.exists():
        return activity

    for meta in DAILY.rglob("meta.json"):
        try:
            data = json.loads(meta.read_text(encoding="utf-8"))
            d = data.get("date")
            if d:
                activity[d] += 1
        except Exception:
            continue
    return activity

def build_heatmap(activity):
    today = date.today()
    end = today - timedelta(days=today.weekday())
    start = end - timedelta(weeks=WEEKS)
    weeks = []
    current = start

    while current < end:
        week = [
            ACTIVE if (current + timedelta(days=i)).isoformat() in activity 
            else EMPTY 
            for i in range(7)
        ]
        weeks.append("| " + " | ".join(week) + " |")
        current += timedelta(weeks=1)

    header = "| Mon | Tue | Wed | Thu | Fri | Sat | Sun |\n" + \
             "|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\n"
    
    return "## 📅 Activity Heatmap\n\n" + header + "\n".join(weeks[-WEEKS:])

def update_readme(content):
    text = README.read_text(encoding="utf-8")
    if START in text and END in text:
        before = text.split(START)[0]
        after = text.split(END)[1]
        text = before + START + "\n\n" + content + "\n\n" + END + after
    else:
        text += f"\n\n{START}\n\n{content}\n\n{END}\n"
    README.write_text(text, encoding="utf-8")

if __name__ == "__main__":
    activity = load_activity()
    heatmap = build_heatmap(activity)
    update_readme(heatmap)
