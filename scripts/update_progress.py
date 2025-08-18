import os
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

def get_solved_problems():
    """Scan language folders and return solved problems dictionary."""
    solved = defaultdict(set)

    for lang in LANG_FOLDERS:
        if not os.path.exists(lang):
            continue  # skip missing folders for now

        for file in os.listdir(lang):
            if file.endswith((".py", ".cpp", ".java", ".go", ".js", ".cs", ".rb", ".swift", ".kt", ".ts", ".rs", ".scala", ".php")):
                problem = os.path.splitext(file)[0]  # filename without extension
                solved[problem].add(lang)

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

    with open(PROGRESS_FILE, "w") as f:
        f.write(progress_md)

    # Update README.md
    with open(README_FILE, "r") as f:
        content = f.read()

    marker = "<!-- PROGRESS_TABLE -->"
    if marker in content:
        before, _ = content.split(marker, 1)
        new_content = before + marker + "\n\n" + progress_md
    else:
        new_content = content + "\n\n" + marker + "\n\n" + progress_md

    with open(README_FILE, "w") as f:
        f.write(new_content)


if __name__ == "__main__":
    solved = get_solved_problems()
    ensure_language_folders(solved)

    # detect active langs (only those that exist or were created)
    active_langs = [lang for lang in LANG_FOLDERS if os.path.exists(lang)]
    update_progress_table(solved, active_langs)
