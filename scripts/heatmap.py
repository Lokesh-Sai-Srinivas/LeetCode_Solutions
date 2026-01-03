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

DAYS = 90


# ---------- LOAD ACTIVITY ----------
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
            pass

    return activity


# ---------- BUILD GRID ----------
def build_heatmap(activity):
    today = date.today()
    start_day = today - timedelta(days=DAYS - 1)

    # Normalize to Monday start
    start_day -= timedelta(days=start_day.weekday())

    rows = []
    current = start_day

    while current <= today:
        week = []
        for _ in range(7):
            key = current.isoformat()
            week.append(ACTIVE if activity.get(key, 0) > 0 else EMPTY)
            current += timedelta(days=1)
        rows.append("  ".join(week))

    header = "Mon Tue Wed Thu Fri Sat Sun"
    body = "\n".join(rows[-13:])  # last ~90 days = 13 weeks

    return (
        "📅 **Activity Heatmap (Last 90 Days)**\n\n"
        + header
        + "\n"
        + body
    )


# ---------- UPDATE README ----------
def update_readme(content):
    text = README.read_text(encoding="utf-8")

    if START in text and END in text:
        before = text.split(START)[0]
        after = text.split(END)[1]
        text = before + START + "\n\n" + content + "\n\n" + END + after
    else:
        text += f"\n\n## 📅 Activity Heatmap\n\n{START}\n\n{content}\n\n{END}\n"

    README.write_text(text, encoding="utf-8")


# ---------- RUN ----------
if __name__ == "__main__":
    activity = load_activity()
    heatmap = build_heatmap(activity)
    update_readme(heatmap)
