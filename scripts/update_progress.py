import os
import re
import shutil
from collections import defaultdict

# ---- Config ----
LANGUAGES = {
    "cpp": { "ext": ".cpp", "display": "C++ ⚡" },
    "java": { "ext": ".java", "display": "Java ☕" },
    "python": { "ext": ".py", "display": "Python 🐍" },
}
DAILY_DIR = "daily-challenge"
PROGRESS_FILE = "PROGRESS.md"
README_FILE = "README.md"

# Regex to match files like "0679_24-game.py"
FILENAME_PATTERN = re.compile(r"^(\d+)[-_](.+)\.(py|java|cpp)$")

def slugify(name: str) -> str:
    """Convert problem name to a filesystem-friendly slug."""
    return name.lower().replace(" ", "-").replace("_", "-")

def process_daily_challenges():
    """Copy daily challenge solutions into respective language folders with correct naming."""
    for day in os.listdir(DAILY_DIR):
        day_path = os.path.join(DAILY_DIR, day)
        if not os.path.isdir(day_path):
            continue

        for file in os.listdir(day_path):
            filepath = os.path.join(day_path, file)
            if not os.path.isfile(filepath):
                continue

            name, ext = os.path.splitext(file)
            lang = None
            for l, data in LANGUAGES.items():
                if data["ext"] == ext:
                    lang = l
                    break
            if not lang:
                continue

            # Extract problem number + title from folder name
            # Expected format: "0679_24-game" or "0679-24-game"
            match = re.match(r"(\d+)[-_](.+)", day)
            if not match:
                continue

            prob_num, prob_title = match.groups()
            slug = slugify(prob_title)
            new_filename = f"{int(prob_num):04d}_{slug}{ext}"

            dest_dir = os.path.join(lang)
            os.makedirs(dest_dir, exist_ok=True)
            dest_path = os.path.join(dest_dir, new_filename)

            # Copy file to language folder
            shutil.copyfile(filepath, dest_path)

def collect_progress():
    """Scan language folders and build a progress table."""
    problems = defaultdict(dict)

    for lang, data in LANGUAGES.items():
        folder = lang
        if not os.path.exists(folder):
            continue
        for file in os.listdir(folder):
            match = FILENAME_PATTERN.match(file)
            if not match:
                continue
            prob_num, title, ext = match.groups()
            title = title.replace("-", " ").replace("_", " ").title()
            problems[prob_num]["title"] = title
            problems[prob_num][lang] = "✅"

    return problems

def update_progress_md(problems):
    """Write PROGRESS.md with a full table."""
    langs = list(LANGUAGES.keys())

    lines = []
    lines.append("# 📊 LeetCode Progress Tracker\n")
    lines.append("| # | Title | " + " | ".join(LANGUAGES[l]["display"] for l in langs) + " |")
    lines.append("|---|-------|" + "|".join("---" for _ in langs) + "|")

    for num in sorted(problems, key=lambda x: int(x)):
        p = problems[num]
        row = f"| {int(num)} | {p['title']} | " + " | ".join(p.get(lang, "❌") for lang in langs) + " |"
        lines.append(row)

    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

def update_readme(problems):
    """Update README with snapshot + link to PROGRESS.md."""
    total = len(problems)
    langs = list(LANGUAGES.values())

    snapshot = f"""
## 📊 Progress Snapshot

- Problems Solved: **{total}**
- Languages: { " | ".join(l["display"] for l in langs) }
- Daily Challenge: ✅ Ongoing

👉 [View Full Progress](./{PROGRESS_FILE})
"""

    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace old snapshot (if exists)
    new_content = re.sub(r"## 📊 Progress Snapshot[\s\S]*?(👉 \[View Full Progress\]\(.*\))",
                         snapshot.strip(), content, flags=re.MULTILINE)

    if new_content == content:  # no snapshot before, just append
        new_content += "\n\n" + snapshot

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)


if __name__ == "__main__":
    process_daily_challenges()
    problems = collect_progress()
    update_progress_md(problems)
    update_readme(problems)
