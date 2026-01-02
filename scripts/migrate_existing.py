import os
import re
import json
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(".")
DAILY_ROOT = ROOT / "daily-challenges"

EXT_TO_LANG = {
    ".py": "python",
    ".java": "java",
    ".cpp": "cpp",
}

PROBLEM_RE = re.compile(r"Problem:\s*(\d+)\s*-\s*(.+)", re.IGNORECASE)
DATE_RE = re.compile(r"Date:\s*(\d{4}-\d{2}-\d{2})")

def parse_metadata(text):
    pid, title, date = None, None, None

    m = PROBLEM_RE.search(text)
    if m:
        pid = int(m.group(1))
        title = m.group(2).strip()

    d = DATE_RE.search(text)
    if d:
        date = datetime.strptime(d.group(1), "%Y-%m-%d")

    return pid, title, date

def clean_code(text):
    # remove leading comment blocks """ ... """ or /* ... */
    text = re.sub(r'""".*?"""', '', text, flags=re.DOTALL)
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
    return text.strip()

def migrate():
    for folder in ["python", "java", "cpp"]:
        lang_dir = ROOT / folder
        if not lang_dir.exists():
            continue

        for file in lang_dir.iterdir():
            if file.suffix not in EXT_TO_LANG:
                continue

            content = file.read_text(encoding="utf-8")
            pid, title, date = parse_metadata(content)

            if not (pid and title and date):
                print(f"⚠️ Skipped {file} (missing metadata)")
                continue

            year = str(date.year)
            month = date.strftime("%m-%B").lower()
            week = f"week-{date.isocalendar().week:02d}"
            day = date.strftime("%Y-%m-%d")

            target_dir = DAILY_ROOT / year / month / week / day
            solutions_dir = target_dir / "solutions"
            solutions_dir.mkdir(parents=True, exist_ok=True)

            lang = EXT_TO_LANG[file.suffix]
            clean = clean_code(content)

            new_file = solutions_dir / f"{lang}{file.suffix}"
            new_file.write_text(clean, encoding="utf-8")

            meta_path = target_dir / "meta.json"
            meta = {
                "problem_id": pid,
                "title": title,
                "difficulty": "Unknown",
                "date": day,
                "solutions": {}
            }

            if meta_path.exists():
                meta = json.loads(meta_path.read_text())

            meta["solutions"][lang] = new_file.name
            meta_path.write_text(json.dumps(meta, indent=2))

            print(f"✅ Migrated {file} → {target_dir}")

    print("\n🎉 Migration complete!")

if __name__ == "__main__":
    migrate()
