import os
import re
import shutil

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DAILY_DIR = os.path.join(BASE_DIR, "daily-challenge")
README = os.path.join(BASE_DIR, "README.md")
PROGRESS = os.path.join(BASE_DIR, "PROGRESS.md")

# -------- Languages --------
LANGUAGES = {
    "cpp":        {"ext": ".cpp",   "emoji": "⚡", "display": "C++"},
    "java":       {"ext": ".java",  "emoji": "☕", "display": "Java"},
    "python":     {"ext": ".py",    "emoji": "🐍", "display": "Python"},
    "golang":     {"ext": ".go",    "emoji": "🐹", "display": "Go"},
    "rust":       {"ext": ".rs",    "emoji": "🦀", "display": "Rust"},
    "javascript": {"ext": ".js",    "emoji": "🌐", "display": "JavaScript"},
    "typescript": {"ext": ".ts",    "emoji": "🔷", "display": "TypeScript"},
    "kotlin":     {"ext": ".kt",    "emoji": "🎯", "display": "Kotlin"},
    "swift":      {"ext": ".swift", "emoji": "🍎", "display": "Swift"},
    "csharp":     {"ext": ".cs",    "emoji": "🎮", "display": "C#"},
    "ruby":       {"ext": ".rb",    "emoji": "💎", "display": "Ruby"},
    "php":        {"ext": ".php",   "emoji": "🐘", "display": "PHP"},
    "scala":      {"ext": ".scala", "emoji": "🔥", "display": "Scala"},
}

# Map ext → lang key for lookup
EXT_TO_LANG = {v["ext"].lstrip("."): k for k, v in LANGUAGES.items()}

# Language folders
LANG_DIRS = {lang: os.path.join(BASE_DIR, lang) for lang in LANGUAGES}

# -------- Filename Styles --------
def get_filename(problem_id, title, lang):
    title_clean = re.sub(r'[^a-zA-Z0-9]+', ' ', title).strip().lower()
    words = title_clean.split()

    if lang == "python":
        return f"{problem_id}_{'_'.join(words)}.py"
    elif lang == "cpp":
        return f"{problem_id}-{'-'.join(words)}.cpp"
    elif lang == "java":
        camel = "".join(w.capitalize() for w in words)
        return f"{problem_id}_{camel}.java"
    else:
        return f"{problem_id}_{'_'.join(words)}{LANGUAGES[lang]['ext']}"

# -------- Parse Problem Header --------
def parse_header(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read(500)  # only need header
        match = re.search(r"Problem:\s*(\d+)\s*-\s*(.+)", content)
        if match:
            return match.group(1).zfill(4), match.group(2).strip()
    except Exception:
        pass
    return None, None

# -------- Step 1: Copy from daily-challenge → language folders --------
def copy_daily_solutions():
    if not os.path.exists(DAILY_DIR):
        return

    for day in os.listdir(DAILY_DIR):
        day_path = os.path.join(DAILY_DIR, day)
        if not os.path.isdir(day_path):
            continue

        for file in os.listdir(day_path):
            ext = file.split(".")[-1]
            if ext not in EXT_TO_LANG:
                continue

            lang = EXT_TO_LANG[ext]
            problem_id, title = parse_header(os.path.join(day_path, file))
            if not problem_id:
                continue

            target_name = get_filename(problem_id, title, lang)
            target_path = os.path.join(LANG_DIRS[lang], target_name)

            os.makedirs(LANG_DIRS[lang], exist_ok=True)

            if not os.path.exists(target_path):
                shutil.copyfile(os.path.join(day_path, file), target_path)

# -------- Step 2: Build progress from language folders --------
def build_progress():
    solved = {}
    active_langs = set()

    for lang, folder in LANG_DIRS.items():
        if not os.path.exists(folder):
            continue

        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            problem_id, title = parse_header(file_path)
            if not problem_id:
                continue

            if problem_id not in solved:
                solved[problem_id] = {"title": title, **{l: "❌" for l in LANGUAGES}}

            solved[problem_id][lang] = "✅"
            active_langs.add(lang)

    return solved, active_langs

# -------- Step 3: Update Markdown --------
def update_progress_table(solved):
    # --- Detect active languages (with at least one ✅) ---
    active_langs = []
    for lang in LANGUAGES:
        if any(solved[pid][lang] == "✅" for pid in solved):
            active_langs.append(lang)

    # Build header
    header = "| # | Title | " + " | ".join(
        f"{LANGUAGES[l]['display']} {LANGUAGES[l]['emoji']}" for l in active_langs
    ) + " |\n"
    header += "|---|-------|" + "|".join("---" for _ in active_langs) + "|\n"

    # Build rows
    rows = []
    for pid in sorted(solved.keys(), key=lambda x: int(x)):
        row = f"| {int(pid)} | {solved[pid]['title']} | " + " | ".join(
            solved[pid][l] for l in active_langs
        ) + " |"
        rows.append(row)

    table = header + "\n".join(rows)

    # Update PROGRESS.md
    with open(PROGRESS, "w", encoding="utf-8") as f:
        f.write("# 📊 LeetCode Progress Tracker\n\n" + table + "\n")

    # Update README.md
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
    solved, active_langs = build_progress()
    if solved:
        update_progress_table(solved, active_langs)
