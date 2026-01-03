import json
import shutil
from pathlib import Path

ROOT = Path(".")
DAILY = ROOT / "daily-challenges"
LANG_ROOT = ROOT / "solutions-by-language"

LANG_ROOT.mkdir(exist_ok=True)

def build_language_index():
    count = 0

    for year in DAILY.iterdir():
        if not year.is_dir():
            continue
        for month in year.iterdir():
            if not month.is_dir():
                continue
            for week in month.iterdir():
                if not week.is_dir():
                    continue
                for day in week.iterdir():
                    if not day.is_dir():
                        continue

                    meta_path = day / "meta.json"
                    sol_dir = day / "solutions"

                    if not meta_path.exists() or not sol_dir.exists():
                        continue

                    meta = json.loads(meta_path.read_text())
                    pid = str(meta["problem_id"]).zfill(4)
                    title = meta["title"].lower().replace(" ", "_").replace("-", "_")

                    for lang, filename in meta["solutions"].items():
                        src = sol_dir / filename
                        if not src.exists():
                            continue

                        lang_dir = LANG_ROOT / lang
                        lang_dir.mkdir(parents=True, exist_ok=True)

                        ext = src.suffix
                        dest = lang_dir / f"{pid}_{title}{ext}"

                        # Avoid duplicate overwrite if same content
                        if dest.exists():
                            continue

                        shutil.copy(src, dest)
                        count += 1

    print(f"✅ Language index built: {count} files copied")

if __name__ == "__main__":
    build_language_index()
