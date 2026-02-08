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
NAMES_FILE = ROOT / "problem_names.json"

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

GITHUB_REPO_URL = "https://github.com/Lokesh-Sai-Srinivas/LeetCode_Solutions/blob/main"

# ---------- GLOBAL CACHE ----------
PROBLEM_NAMES = {}

# ---------- HELPERS ----------
def infer_name_from_filename(filename: str) -> str:
    name = filename.split("_", 1)[-1]
    name = name.rsplit(".", 1)[0]
    return name.replace("_", " ").title()


def get_problem_urls():
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


def load_problem_names():
    if NAMES_FILE.exists():
        try:
            return json.loads(NAMES_FILE.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_problem_names():
    if PROBLEM_NAMES:
        NAMES_FILE.write_text(
            json.dumps(PROBLEM_NAMES, indent=2),
            encoding="utf-8"
        )


# ---------- SYNC DAILY SOLUTIONS ----------
def sync_daily_challenges():
    global PROBLEM_NAMES
    PROBLEM_NAMES.update(load_problem_names())

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
            raw_name = match.group(2).strip()
            safe_name = raw_name.lower().replace(" ", "_").replace("-", "_")

            PROBLEM_NAMES[pid] = raw_name
            dest = dest_dir / f"{pid}_{safe_name}{ext}"
            shutil.copy(file, dest)

    save_problem_names()


# ---------- COLLECT SOLVED + LINKS ----------
def get_solved():
    solved = defaultdict(dict)
    inferred_names = {}

    if not LANG_ROOT.exists():
        return solved, inferred_names

    for lang_dir in LANG_ROOT.iterdir():
        if not lang_dir.is_dir():
            continue

        lang = lang_dir.name
        for f in lang_dir.iterdir():
            m = re.match(r"^(\d+)", f.name)
            if not m:
                continue

            pid = m.group(1).zfill(4)
            rel_path = f"solutions-by-language/{lang}/{f.name}"
            github_link = f"{GITHUB_REPO_URL}/{rel_path}"

            solved[pid][lang] = github_link

            if pid not in inferred_names:
                inferred_names[pid] = infer_name_from_filename(f.name)

    return solved, inferred_names


# ---------- UPDATE PROGRESS ----------
def update_progress():
    solved, inferred_names = get_solved()
    problem_urls = get_problem_urls()

    problem_names = load_problem_names()
    problem_names.update(inferred_names)

    active_langs = sorted(
        {lang for langs in solved.values() for lang in langs}
    )

    header = (
        "| ID | Problem Name | Link | "
        + " | ".join(active_langs)
        + " |\n"
    )
    header += (
        "|----|--------------|------|"
        + "|".join([":---:"] * len(active_langs))
        + "|\n"
    )

    rows = []
    for pid in sorted(solved):
        name = problem_names.get(pid, "Unknown")
        problem_link = f"[🔗]({problem_urls.get(pid, '')})" if pid in problem_urls else ""

        row = f"| {pid} | {name} | {problem_link} "

        for lang in active_langs:
            if lang in solved[pid]:
                row += f"| [✅]({solved[pid][lang]}) "
            else:
                row += "| ❌ "

        row += "|"
        rows.append(row)

    table = header + "\n".join(rows)
    content = f"**Total Solved:** {len(solved)}\n\n" + table

    PROGRESS_FILE.write_text(content, encoding="utf-8")

    readme = README_FILE.read_text(encoding="utf-8")
    start = "<!-- PROGRESS:START -->"
    end = "<!-- PROGRESS:END -->"

    if start in readme and end in readme:
        readme = (
            readme.split(start)[0]
            + start
            + "\n\n"
            + content
            + "\n\n"
            + end
            + readme.split(end)[1]
        )
    else:
        readme += f"\n\n## 📊 Progress\n{start}\n\n{content}\n\n{end}\n"

    README_FILE.write_text(readme, encoding="utf-8")

    global PROBLEM_NAMES
    PROBLEM_NAMES.update(problem_names)
    save_problem_names()


# ---------- RUN ----------
if __name__ == "__main__":
    sync_daily_challenges()
    update_progress()
