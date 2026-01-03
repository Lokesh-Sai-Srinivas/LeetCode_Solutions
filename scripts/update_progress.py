import re
import shutil
from pathlib import Path
from collections import defaultdict

# ---------- PATHS ----------
ROOT = Path(__file__).resolve().parents[1]
README_FILE = ROOT / "README.md"
PROGRESS_FILE = ROOT / "PROGRESS.md"
DAILY_FOLDER = ROOT / "daily-challenges"

# ---------- CONFIG ----------
LANG_FOLDERS = [
    "python", "cpp", "java", "golang", "javascript", "csharp",
    "ruby", "swift", "kotlin", "typescript", "rust", "scala", "php",
]

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

# ---------- FUNCTIONS ----------
def sync_daily_challenges():
    if not DAILY_FOLDER.exists():
        return

    for date_dir in DAILY_FOLDER.iterdir():
        if not date_dir.is_dir():
            continue

        for file in date_dir.iterdir():
            ext = file.suffix
            if file.name.startswith("solution.") and ext in EXT_TO_LANG:
                lang = EXT_TO_LANG[ext]
                dest_dir = ROOT / lang
                dest_dir.mkdir(exist_ok=True)

                try:
                    content = file.read_text(encoding="utf-8")
                except Exception:
                    continue

                match = re.search(r"Problem:\s*(\d+)\s*-\s*(.+)", content, re.I)
                if not match:
                    continue

                pid = match.group(1).zfill(4)
                name = match.group(2).lower().replace(" ", "_").replace("-", "_")
                dest = dest_dir / f"{pid}_{name}{ext}"

                shutil.copy(file, dest)

def get_solved():
    solved = defaultdict(set)

    for lang in LANG_FOLDERS:
        lang_dir = ROOT / lang
        if not lang_dir.exists():
            continue

        for f in lang_dir.iterdir():
            if f.suffix in EXT_TO_LANG:
                m = re.match(r"^(\d+)", f.name)
                if m:
                    solved[m.group(1).zfill(4)].add(lang)

    return solved

def update_progress():
    solved = get_solved()
    active_langs = [l for l in LANG_FOLDERS if (ROOT / l).exists()]

    header = "| Problem | " + " | ".join(active_langs) + " |\n"
    header += "|--------|" + "|".join([":---:"] * len(active_langs)) + "|\n"

    rows = []
    for pid in sorted(solved):
        row = f"| {pid} "
        for lang in active_langs:
            row += "| ✅ " if lang in solved[pid] else "| ❌ "
        row += "|"
        rows.append(row)

    table = header + "\n".join(rows)
    content = f"**Total Solved:** {len(solved)}\n\n" + table

    PROGRESS_FILE.write_text(content, encoding="utf-8")

    readme = README_FILE.read_text(encoding="utf-8")

    start = "<!-- PROGRESS:START -->"
    end = "<!-- PROGRESS:END -->"

    if start in readme and end in readme:
        before = readme.split(start)[0]
        after = readme.split(end)[1]
        readme = before + start + "\n\n" + content + "\n\n" + end + after
    else:
        readme += f"\n\n## 📊 Progress\n{start}\n\n{content}\n\n{end}\n"

    README_FILE.write_text(readme, encoding="utf-8")

# ---------- RUN ----------
if __name__ == "__main__":
    sync_daily_challenges()
    update_progress()
