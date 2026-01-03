from pathlib import Path
import json
from datetime import datetime, timedelta
from collections import defaultdict

# ---------- PATHS ----------
ROOT = Path(__file__).resolve().parents[1]
DAILY = ROOT / "daily-challenges"
README = ROOT / "README.md"

START = "<!-- HEATMAP:START -->"
END = "<!-- HEATMAP:END -->"

ACTIVE = "🟩"
INACTIVE = "⬜"

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


# ---------- LOAD ACTIVITY ----------
def load_activity():
    activity = set()

    for meta in DAILY.rglob("meta.json"):
        try:
            data = json.loads(meta.read_text(encoding="utf-8"))
            date = data.get("date")
            if date:
                activity.add(datetime.strptime(date, "%Y-%m-%d").date())
        except Exception:
            pass

    return activity


# ---------- BUILD HEATMAP ----------
def build_heatmap(activity, days=90):
    today = datetime.today().date()
    start_day = today - timedelta(days=days - 1)

    # Align to Monday
    start_day -= timedelta(days=start_day.weekday())

    lines = ["📅 **Activity Heatmap (Last 90 Days)**\n"]
    lines.append("Mon Tue Wed Thu Fri Sat Sun")

    week = []
    day = start_day

    while day <= today:
        week.append(ACTIVE if day in activity else INACTIVE)

        if len(week) == 7:
            lines.append("  ".join(week))
            week = []

        day += timedelta(days=1)

    if week:
        while len(week) < 7:
            week.append(INACTIVE)
        lines.append("  ".join(week))

    return "\n".join(lines)


# ---------- UPDATE README ----------
def update_readme(content):
    text = README.read_text(encoding="utf-8")

    if START in text and END in text:
        before = text.split(START)[0]
        after = text.split(END)[1]
        text = before + START + "\n\n" + content + "\n\n" + END + after
    else:
        text += f"\n\n{START}\n\n{content}\n\n{END}"

    README.write_text(text, encoding="utf-8")


# ---------- RUN ----------
if __name__ == "__main__":
    activity = load_activity()
    heatmap = build_heatmap(activity)
    update_readme(heatmap)
