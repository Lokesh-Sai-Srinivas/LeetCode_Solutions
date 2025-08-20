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
    "php",
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
    """Copy daily-challenge/YYYY-MM-DD/solution.* files into respective language folders."""
    if not os.path.exists("daily-challenge"):
        return

    for date_folder in os.listdir("daily-challenge"):
        date_path = os.path.join("daily-challenge", date_folder)
        if not os.path.isdir(date_path):
            continue

        for file in os.listdir(date_path):
            _, ext = os.path.splitext(file)
            if not file.startswith("solution.") or ext not in EXT_TO_LANG:
                continue

            lang = EXT_TO_LANG[ext]
            lang_folder = os.path.join(lang)
            os.makedirs(lang_folder, exist_ok=True)

            path = os.path.join(date_path, file)

            # Extract problem ID + name from header
            problem_id, problem_name = None, None
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception:
                print(f"⚠️ Could not read {path}")
                continue

            match = re.search(r"Problem:\s*(\d+)\s*-\s*(.+)", content, re.IGNORECASE)
            if match:
                problem_id = match.group(1).zfill(4)  # normalize e.g. 326 -> 0326
                problem_name = (
                    match.group(2)
                    .strip()
                    .lower()
                    .replace(" ", "_")
                    .replace("-", "_")
                )

            if not problem_id:
                print(f"⚠️ Skipped {file} (could not extract problem ID)")
                continue

            dest_name = f"{problem_id}_{problem_name}{ext}" if problem_name else f"{problem_id}{ext}"
            dest_path = os.path.join(lang_folder, dest_name)

            shutil.copy(path, dest_path)  # always overwrite
            print(f"✅ Synced {file} ({date_folder}) → {dest_path}")


def get_solved_problems():
    """Scan language folders and return solved problems dictionary."""
    solved = defaultdict(set)

    for lang in LANG_FOLDERS:
        if not os.path.exists(lang):
            continue

        for file in os.listdir(lang):
            _, ext = os.path.splitext(file)
            if ext in EXT_TO_LANG:
                match = re.match(r"^(\d+)", file)
                if match:
                    problem_id = match.group(1).zfill(4)
                    solved[problem_id].add(lang)

    return solved


def update_progress_table(solved, active_langs):
    """Generate progress table content and update README + PROGRESS.md."""
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

    # Update PROGRESS.md
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
    sync_daily_challenges()
    solved = get_solved_problems()
    active_langs = [lang for lang in LANG_FOLDERS if os.path.exists(lang)]
    update_progress_table(solved, active_langs)
