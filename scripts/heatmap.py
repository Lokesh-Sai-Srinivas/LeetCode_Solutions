from pathlib import Path
import json
from collections import defaultdict
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
DAILY = ROOT / "daily-challenges"
README = ROOT / "README.md"

BLOCKS = ["⬜", "🟩", "🟨", "🟧", "🟥"]

def load_activity():
    activity = defaultdict(int)

    for meta in DAILY.rglob("meta.json"):
        try:
            data = json.loads(meta.read_text(encoding="utf-8"))
            date = data.get("date")
            if date:
                activity[date] += 1
        except Exception:
            pass

    return activity

def intensity(count):
    if count == 0:
        return BLOCKS[0]
    elif count == 1:
        return BLOCKS[1]
    elif count == 2:
        return BLOCKS[2]
    elif count == 3:
        return BLOCKS[3]
    else:
        return BLOCKS[4]

def build_heatmap(activity):
    lines = ["📅 **Daily Activity Heatmap**\n"]
    for date in sorted(activity.keys()):
        lines.append(f"{date} {intensity(activity[date])}")
    return "\n".join(lines)

def update_readme(content):
    text = README.read_text(encoding="utf-8")

    start = "<!-- HEATMAP:START -->"
    end = "<!-- HEATMAP:END -->"

    if start in text and end in text:
        before = text.split(start)[0]
        after = text.split(end)[1]
        text = before + start + "\n\n" + content + "\n\n" + end + after
    else:
        text += f"\n\n{start}\n\n{content}\n\n{end}"

    README.write_text(text, encoding="utf-8")

if __name__ == "__main__":
    activity = load_activity()
    heatmap = build_heatmap(activity)
    update_readme(heatmap)
