import os
import re
import shutil

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DAILY_DIR = os.path.join(BASE_DIR, "daily-challenge")
LANG_DIRS = {
    "py": os.path.join(BASE_DIR, "python"),
    "cpp": os.path.join(BASE_DIR, "cpp"),
    "java": os.path.join(BASE_DIR, "java"),
}
README = os.path.join(BASE_DIR, "README.md")
PROGRESS = os.path.join(BASE_DIR, "PROGRESS.md")

# File naming styles
def get_filename(problem_id, title, lang):
    title_clean = re.sub(r'[^a-zA-Z0-9]+', ' ', title).strip().lower()
    words = title_clean.split()

    if lang == "py":
        return f"{problem_id}_{'_'.join(words)}.py"
    elif lang == "cpp":
        return f"{problem_id}-{'-'.join(words)}.cpp"
    elif lang == "java":
        camel = "".join(w.capitalize() for w in words)
        return f"{problem_id}_{camel}.java"
    return None

# Extract header info from solution file
def parse_header(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read(500)  # only read beginning
    match = re.search(r"Problem:\s*(\d+)\s*-\s*(.+)", content)
    if match:
        return match.group(1).zfill(4), match.group(2).strip()
    return None, None

# Copy solutions to respective language dirs
def copy_daily_solutions():
    solved = {}
    for day in os.listdir(DAILY_DIR):
        day_path = os.path.join(DAILY_DIR, day)
        if not os.path.isdir(day_path):
            continue

        for file in os.listdir(day_path):
            ext = file.split(".")[-1]
            if ext not in LANG_DIRS:
                continue

            problem_id, title = parse_header(os.path.join(day_path, file))
            if not problem_id:
                continue

            target_name = get_filename(problem_id, title, ext)
            target_path = os.path.join(LANG_DIRS[ext], target_name)

            # Copy if not already present
            if not os.path.exists(target_path):
                shutil.copyfile(os.path.join(day_path, file), target_path)

            # Track solved
            solved.setdefault(problem_id, {"title": title, "py": "❌", "cpp": "❌", "java": "❌"})
            solved[problem_id][ext] = "✅"

    return solved

# Update README.md & PROGRESS.md tables
def update_progress_table(solved):
    # Build markdown table
    header = "| # | Title | C++ ⚡ | Java ☕ | Python 🐍 |\n|---|-------|---|---|---|\n"
    rows = []
    for pid in sorted(solved.keys()):
        row = f"| {int(pid)} | {solved[pid]['title']} | {solved[pid]['cpp']} | {solved[pid]['java']} | {solved[pid]['py']} |"
        rows.append(row)
    table = header + "\n".join(rows)

    # Update PROGRESS.md fully
    with open(PROGRESS, "w", encoding="utf-8") as f:
        f.write("# 📊 LeetCode Progress Tracker\n\n" + table + "\n")

    # Update README.md (replace snapshot section)
    with open(README, "r", encoding="utf-8") as f:
        readme = f.read()

    if "📊 Progress Snapshot" in readme:
        before = readme.split("📊 Progress Snapshot")[0]
        after = "\n👉 View Full Progress\n"
        readme = before + "📊 Progress Snapshot\n\n" + table + after

    with open(README, "w", encoding="utf-8") as f:
        f.write(readme)

if __name__ == "__main__":
    solved = copy_daily_solutions()
    update_progress_table(solved)
