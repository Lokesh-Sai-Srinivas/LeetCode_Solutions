import os
import shutil

# -------------------------
# 1. Problem Metadata
# -------------------------
# ✅ Extend this dictionary as you solve more
problems = {
    "0001": ("Two Sum", "Easy"),
    "0002": ("Add Two Numbers", "Medium"),
    "0003": ("Longest Substring Without Repeating Characters", "Medium"),
    "0679": ("24 Game", "Hard"),
}

# Language → File Extension
languages = {
    "python": ".py",
    "java": ".java",
    "cpp": ".cpp"
}

# -------------------------
# 2. Helpers
# -------------------------
def ensure_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def copy_from_daily(problem_num, ext, lang):
    """If solution exists in daily-challenge, copy it into lang folder"""
    daily_folder = "daily-challenge/"
    if not os.path.exists(daily_folder):
        return False

    for date in os.listdir(daily_folder):
        path = os.path.join(daily_folder, date)
        if os.path.isdir(path):
            for fname in os.listdir(path):
                if fname.startswith(problem_num) and fname.endswith(ext):
                    ensure_folder(lang)
                    # normalize filename e.g. 0679-24-game -> 0679_24_game.ext
                    base_name = fname.replace("-", "_")
                    new_path = os.path.join(lang, base_name)
                    shutil.copy(os.path.join(path, fname), new_path)
                    return True
    return False

def detect_languages():
    """Detect all languages dynamically (add new langs automatically)."""
    lang_map = {}
    for folder in os.listdir("."):
        if os.path.isdir(folder) and folder not in ["daily-challenge", ".github", "scripts"]:
            for fname in os.listdir(folder):
                _, ext = os.path.splitext(fname)
                if ext and ext not in lang_map.values():
                    lang_map[folder] = ext
    return lang_map

# -------------------------
# 3. Build Progress Table
# -------------------------
languages = detect_languages()  # auto-detect langs
header = "| # | Title | Difficulty | " + " | ".join(languages.keys()) + " |"
divider = "|---|-------|------------|" + "|".join(["--------" for _ in languages]) + "|"

progress_table = header + "\n" + divider + "\n"

for num, (title, difficulty) in problems.items():
    row = f"| {int(num)} | {title} | {difficulty} |"

    for lang, ext in languages.items():
        folder = f"{lang}/"
        solved = False

        # Check language folder
        if os.path.exists(folder):
            solved = any(fname.startswith(num) and fname.endswith(ext) for fname in os.listdir(folder))

        # Try to copy from daily if missing
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
