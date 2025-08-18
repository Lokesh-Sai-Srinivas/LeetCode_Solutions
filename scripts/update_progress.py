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

# -------- Filename Styles --------
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

# -------- Parse Problem Header --------
def parse_header(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read(500)  # only need the header
        match = re.search(r"Problem:\s*(\d+)\s*-\s*(.+)", content)
        if match:
            return match.group(1).zfill(4), match.group(2).strip()
    except Exception:
        pass
    return None, None

# -------- Step 1: Copy from daily-challenge → language folders --------
def copy_daily_solutions():
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

            # Copy only if missing
            if not os.path.exists(target_path):
                shutil.copyfile(os.path.join(day_path, file), target_path)

# -------- Step 2: Build progress from language folders --------
def build_progress():
    solved = {}

    for lang, folder in LANG_DIRS.items():
        if not os.path.exists(folder):
            continue

        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            problem_id, title = parse_header(file_path)
            if not problem_id:
                continue

            if problem_id not in solved:
                solved[problem_id] = {"title": title, "py": "❌", "cpp": "❌", "java": "❌"}
            solved[problem_id][lang] = "✅"

    return solved

# -------- Step 3: Update Markdown --------
def update_progress_table(solved):
    header = "| # | Title | C++ ⚡ | Java ☕ | Python 🐍 |\n|---|-------|---|---|---|\n"
    rows = []
    for pid in sorted(solved.keys(), key=lambda x: int(x)):
        row = f"| {int(pid)} | {solved[pid]['title']} | {solved[pid]['cpp']} | {solved[pid]['java']} | {solved[pid]['py']} |"
        rows.append(row)
    table = header + "\n".join(rows)

    # Update PROGRESS.md fully
    with open(PROGRESS, "w", encoding="utf-8") as f:
        f.write("# 📊 LeetCode Progress Tracker\n\n" + table + "\n")

    # Update README.md (replace snapshot section if exists)
    with open(README, "r", encoding="utf-8") as f:
        readme = f.read()

    if "📊 Progress Snapshot" in readme:
        before = readme.split("📊 Progress Snapshot")[0]
        after = "\n👉 View Full Progress\n"
        readme = before + "📊 Progress Snapshot\n\n" + table + after

    with open(README, "w", encoding="utf-8") as f:
        f.write(readme)

# -------- Main --------
if __name__ == "__main__":
    copy_daily_solutions()
    solved = build_progress()
    update_progress_table(solved)
