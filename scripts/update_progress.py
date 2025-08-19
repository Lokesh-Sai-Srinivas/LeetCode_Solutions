import os
import re
import shutil
from collections import defaultdict

# Root folders where language solutions are stored
LANG_FOLDERS = [
    "python",
    "cpp",
    "java",
    "golang",
    "javascript",
    "csharp",
    "ruby",
    "swift",
    "kotlin",
    "typescript",
    "rust",
    "scala",
    "php"
]

README_FILE = "README.md"
PROGRESS_FILE = "PROGRESS.md"

# Map file extensions to language folder names
EXT_TO_LANG = {
    ".py": "python",
    ".cpp": "cpp",
    ".java": "java",
    ".go": "golang",
    ".js": "javascript",
    ".cs": "csharp",
    ".rb": "ruby",
    ".swift": "swift",
    ".kt": "kotlin",
    ".ts": "typescript",
    ".rs": "rust",
    ".scala": "scala",
    ".php": "php",
}


def sync_daily_challenges():
    """Copy daily-challenge solution.* files into respective language folders."""
    if not os.path.exists("daily-challenge"):
        return

    for root, _, files in os.walk("daily-challenge"):
        for file in files:
            _, ext = os.path.splitext(file)
            if not file.startswith("solution.") or ext not in EXT_TO_LANG:
                continue

            lang = EXT_TO_LANG[ext]
            lang_folder = os.path.join(lang)
            os.makedirs(lang_folder, exist_ok=True)

            path = os.path.join(root, file)

            # Extract problem ID from header
            problem_id, problem_name = None, None
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception:
                continue

            match = re.search(r"Problem:\s*(\d+)\s*-\s*(.+)", content)
            if match:
                problem_id = match.group(1).zfill(4)  # normalize (e.g. 326 -> 0326)
                problem_name = (
                    match.group(2)
                    .strip()
                    .lower()
                    .replace(" ", "_")
                    .replace("-", "_")
                )

            if not problem_id:
                continue

            # Build destination file name
            dest_name = f"{problem_id}_{problem_name}{ext}" if problem_name else f"{problem_id}{ext}"
            dest_path = os.path.join(lang_folder, dest_name)

            # Always copy (overwrite to sync)
            shutil.copy(path, dest_path)
            print(f"✅ Synced {file} → {dest_path}")

def get_solved_problems():
    """Scan language folders and return solved problems dictionary."""
    solved = defaultdict(set)

    for lang in LANG_FOLDERS:
        if not os.path.exists(lang):
            continue

        for file in os.listdir(lang):
            _, ext = os.path.splitext(file)
            if ext in EXT_TO_LANG:
                # Extract problem number
                match = re.match(r"^(\d+)", file)
                if match:
                    problem_id = match.group(1).zfill(4)  # normalize
                    solved[problem_id].add(lang)

    return solved


def update_progress_table(solved, active_langs):
    """Generate progress table content."""
    total_problems = len(solved)
    header = "| Problem | " + " | ".join(active_langs) + " |\n"
    header += "|---------|" + "|".join([":---:"] * len(active_langs)) + "|\n"

    rows = []
    for problem in sorted(solved.keys()):
        row = f"| {problem} "
        for lang in active_langs:
            row += "| ✅ " if lang in solved[problem] else "| ❌ "
        row += "|"
        rows.append(row)

    table = header + "\n".join(rows)
    progress_md = f"# Progress Overview\n\n**Total Solved:** {total_problems}\n\n" + table

    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        f.write(progress_md)

    if os.path.exists(README_FILE):
        with open(README_FILE, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = ""

    marker = "<!-- PROGRESS_TABLE -->"
    if marker in content:
        before, _ = content.split(marker, 1)
        new_content = before + marker + "\n\n" + progress_md
    else:
        new_content = content + "\n\n" + marker + "\n\n" + progress_md

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)


if __name__ == "__main__":
    sync_daily_challenges()   # ✅ Step 1: copy daily-challenge → lang folders
    solved = get_solved_problems()  # ✅ Step 2: scan language folders
    active_langs = [lang for lang in LANG_FOLDERS if os.path.exists(lang)]
    update_progress_table(solved, active_langs)
