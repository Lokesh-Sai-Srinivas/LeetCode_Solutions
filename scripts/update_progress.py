import os
import re
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

def get_solved_problems():
    """Scan language folders + daily-challenge for solved problems."""
    solved = defaultdict(set)

    # 1. Scan regular language folders
    for lang in LANG_FOLDERS:
        if not os.path.exists(lang):
            continue

        for file in os.listdir(lang):
            _, ext = os.path.splitext(file)
            if ext in EXT_TO_LANG:
                # Extract problem number from filename (e.g., 0001 from 0001-two-sum.py)
                match = re.match(r"^(\d+)", file)
                if match:
                    problem_id = match.group(1)
                    solved[problem_id].add(EXT_TO_LANG[ext])

    # 2. Scan daily-challenge folder
    if os.path.exists("daily-challenge"):
        for root, _, files in os.walk("daily-challenge"):
            for file in files:
                _, ext = os.path.splitext(file)
                if file.startswith("solution.") and ext in EXT_TO_LANG:
                    lang = EXT_TO_LANG[ext]
                    path = os.path.join(root, file)

                    try:
                        with open(path, "r", encoding="utf-8") as f:
                            content = f.read()
                    except Exception:
                        continue

                    # Extract problem ID from header (Problem: 2348 - ...)
                    match = re.search(r"Problem:\s*(\d+)", content)
                    if match:
                        problem_id = match.group(1)
                        solved[problem_id].add(lang)

    return solved


def ensure_language_folders(solved):
    """Ensure folders exist for all detected languages."""
    for langs in solved.values():
        for lang in langs:
            if not os.path.exists(lang):
                os.makedirs(lang)  # create missing folder


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

    # Update README.md
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
    solved = get_solved_problems()
    ensure_language_folders(solved)

    # detect active langs (only those that exist or were created)
    active_langs = [lang for lang in LANG_FOLDERS if os.path.exists(lang)]
    update_progress_table(solved, active_langs)
