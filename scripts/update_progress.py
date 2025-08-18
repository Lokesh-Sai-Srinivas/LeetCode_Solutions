import os
import shutil
import re

# -------------------------
# 1. Helpers
# -------------------------
def ensure_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def normalize_filename(fname):
    """Standardize filename: 0679-24-game.py -> 0679_24_game.py"""
    base, ext = os.path.splitext(fname)
    return base.replace("-", "_") + ext

def extract_problem_info(fname):
    """
    Extract problem number + title from filename.
    Example: 0679_24_game.py -> ("0679", "24 Game")
    """
    base, _ = os.path.splitext(fname)
    parts = base.split("_", 1)
    if len(parts) == 2 and parts[0].isdigit():
        num, raw_title = parts
        title = raw_title.replace("_", " ").title()
        return num, title
    return None, None

def detect_languages():
    """Detect all language folders dynamically."""
    lang_map = {}
    for folder in os.listdir("."):
        if os.path.isdir(folder) and folder not in ["daily-challenge", ".github", "scripts"]:
            for fname in os.listdir(folder):
                _, ext = os.path.splitext(fname)
                if ext:
                    lang_map[folder] = ext
    return lang_map

def copy_from_daily(problem_num, ext, lang):
    """Copy solution from daily-challenge → lang folder if missing"""
    daily_folder = "daily-challenge/"
    if not os.path.exists(daily_folder):
        return False

    for date in os.listdir(daily_folder):
        path = os.path.join(daily_folder, date)
        if os.path.isdir(path):
            for fname in os.listdir(path):
                if fname.startswith(problem_num) and fname.endswith(ext):
                    ensure_folder(lang)
                    new_name = normalize_filename(fname)
                    shutil.copy(os.path.join(path, fname), os.path.join(lang, new_name))
                    return True
    return False

# -------------------------
# 2. Build Problem List
# -------------------------
problems = {}  # { "0001": "Two Sum", "0679": "24 Game", ... }

# Scan language folders
for folder in os.listdir("."):
    if os.path.isdir(folder) and folder not in ["daily-challenge", ".github", "scripts"]:
        for fname in os.listdir(folder):
            num, title = extract_problem_info(fname)
            if num and title:
                problems[num] = title

# Scan daily-challenge
if os.path.exists("daily-challenge"):
    for date in os.listdir("daily-challenge"):
        path = os.path.join("daily-challenge", date)
        if os.path.isdir(path):
            for fname in os.listdir(path):
                num, title = extract_problem_info(fname)
                if num and title:
                    problems[num] = title

# -------------------------
# 3. Build Progress Table
# -------------------------
languages = detect_languages()
header = "| # | Title | " + " | ".join(languages.keys()) + " |"
divider = "|---|-------|" + "|".join(["--------" for _ in languages]) + "|"

progress_table = header + "\n" + divider + "\n"

for num in sorted(problems.keys(), key=lambda x: int(x)):
    title = problems[num]
    row = f"| {int(num)} | {title} |"

    for lang, ext in languages.items():
        folder = f"{lang}/"
        solved = False

        if os.path.exists(folder):
            solved = any(fname.startswith(num) and fname.endswith(ext) for fname in os.listdir(folder))

        if not solved:
            solved = copy_from_daily(num, ext, lang)

        row += " ✅ |" if solved else " ⬜ |"

    progress_table += row + "\n"

# -------------------------
# 4. Update README.md
# -------------------------
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

start_marker = "## 📊 Problem Progress Tracker"
if start_marker in content:
    content = content.split(start_marker)[0] + start_marker + "\n\n" + progress_table
else:
    content += "\n\n" + start_marker + "\n\n" + progress_table

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
