import os
import re
import json
import shutil
from pathlib import Path
from collections import defaultdict

# ---------- PATHS ----------
ROOT = Path(__file__).resolve().parents[1]
README_FILE = ROOT / "README.md"
PROGRESS_FILE = ROOT / "PROGRESS.md"
DAILY_FOLDER = ROOT / "daily-challenges"
LANG_ROOT = ROOT / "solutions-by-language"

# ---------- CONFIG ----------
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

# ---------- HELPERS ----------
def get_problem_urls():
    """Map problem_id -> LeetCode URL from meta.json files"""
    urls = {}

    if not DAILY_FOLDER.exists():
        return urls

    for meta in DAILY_FOLDER.rglob("meta.json"):
        try:
            data = json.loads(meta.read_text(encoding="utf-8"))
            pid = data.get("problem_id")
            url = data.get("url")

            if pid and url:
                urls[str(pid).zfill(4)] = url
        except Exception:
            continue

    return urls


# ---------- SYNC DAILY SOLUTIONS ----------
def sync_daily_challenges():
    """Copy daily solutions into solutions-by-language folders"""
    if not DAILY_FOLDER.exists():
        return

    for solutions_dir in DAILY_FOLDER.rglob("solutions"):
        for file in solutions_dir.iterdir():
            if not file.name.startswith("solution."):
                continue

            ext = file.suffix
            if ext not in EXT_TO_LANG:
                continue

            lang = EXT_TO_LANG[ext]
            dest_dir = LANG_ROOT / lang
            dest_dir.mkdir(parents=True, exist_ok=True)

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


# ---------- COLLECT SOLVED ----------
def get_solved():
    solved = defaultdict(set)

    if not LANG_ROOT.exists():
        return solved

    for lang_dir in LANG_ROOT.iterdir():
        if not lang_dir.is_dir():
            continue

        lang = lang_dir.name
        for f in lang_dir.iterdir():
            m = re.match(r"^(\d+)", f.name)
            if m:
                solved[m.group(1).zfill(4)].add(lang)

    return solved


# ---------- UPDATE PROGRESS ----------
def update_progress():
    solved = get_solved()
    problem_urls = get_problem_urls()

    active_langs = sorted({lang for langs in solved.values() for lang in langs})

    header = "| Problem | Link | " + " | ".join(active_langs) + " |\n"
    header += "|---------|------|" + "|".join([":---:"] * len(active_langs)) + "|\n"

    rows = []
    for pid in sorted(solved):
        url = problem_urls.get(pid, "")
        link = f"[🔗]({url})" if url else ""

        row = f"| {pid} | {link} "
        for lang in active_langs:
            row += "| ✅ " if lang in solved[pid] else "| ❌ "
        row += "|"
        rows.append(row)

    table = header + "\n".join(rows)
    content = f"**Total Solved:** {len(solved)}\n\n" + table

    # Write PROGRESS.md
    PROGRESS_FILE.write_text(content, encoding="utf-8")

    # Update README
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
