import json
import shutil
import requests
from pathlib import Path
from datetime import datetime

# ================= CONFIG ================= #
ROOT = Path(".")
INCOMING = ROOT / "incoming"
DAILY = ROOT / "daily-challenges"
LANG_ROOT = ROOT / "solutions-by-language"
README = ROOT / "README.md"

EXT_TO_LANG = {
    ".py": "python",
    ".java": "java",
    ".cpp": "cpp",
}

LEETCODE_GRAPHQL = "https://leetcode.com/graphql"
# ========================================= #


def ensure_dirs():
    INCOMING.mkdir(exist_ok=True)
    LANG_ROOT.mkdir(exist_ok=True)
    DAILY.mkdir(exist_ok=True)


def incoming_ready():
    meta = INCOMING / "meta.json"
    sols = INCOMING / "solutions"
    if not meta.exists() or not sols.exists():
        return False
    return any(f.suffix in EXT_TO_LANG for f in sols.iterdir())


from urllib.parse import urlparse

def extract_slug(url):
    """
    Extracts problem slug safely from any LeetCode problem URL
    """
    path = urlparse(url).path
    parts = [p for p in path.split("/") if p]
    if "problems" not in parts:
        raise ValueError(f"Invalid LeetCode problem URL: {url}")
    idx = parts.index("problems")
    return parts[idx + 1]



def fetch_problem_data(url):
    slug = extract_slug(url)

    payload = {
        "query": """
        query getQuestion($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            questionFrontendId
            title
            difficulty
            titleSlug
            topicTags {
              name
              slug
            }
          }
        }
        """,
        "variables": {"titleSlug": slug}
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://leetcode.com",
    }

    r = requests.post(
        LEETCODE_GRAPHQL,
        json=payload,
        headers=headers,
        timeout=10
    )

    r.raise_for_status()
    data = r.json()

    q = data.get("data", {}).get("question")
    if q is None:
        raise RuntimeError(
            f"❌ Failed to fetch problem data from LeetCode for slug '{slug}'. "
            f"Check URL or network."
        )

    # Extract topic names
    topics = [t["name"] for t in q.get("topicTags", [])]

    return {
        "id": int(q["questionFrontendId"]),
        "title": q["title"],
        "slug": q["titleSlug"],
        "difficulty": q["difficulty"],
        "topics": topics
    }


def clean_code(text):
    import re
    text = re.sub(r'""".*?"""', '', text, flags=re.DOTALL)
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
    return text.strip()


def update_progress():
    solved = {}
    langs = sorted([d.name for d in LANG_ROOT.iterdir() if d.is_dir()])

    for year in DAILY.iterdir():
        for month in year.iterdir():
            for week in month.iterdir():
                for day in week.iterdir():
                    meta_path = day / "meta.json"
                    if not meta_path.exists():
                        continue
                    meta = json.loads(meta_path.read_text(encoding='utf-8'))
                    pid = str(meta["problem_id"]).zfill(4)
                    solved.setdefault(
                        pid,
                        {
                            "url": meta.get("url", ""),
                            "langs": set()
                        }
                    )

                    solved[pid]["langs"].update(meta["solutions"].keys())

    header = "| Problem | " + " | ".join(langs) + " |\n"
    header += "|---------|" + "|".join([":---:"] * len(langs)) + "|\n"

    rows = []
    for pid in sorted(solved, key=int):
        link = f"[{pid}]({solved[pid]['url']})"
        row = f"| {link} "
        for l in langs:
            row += "| ✅ " if l in solved[pid]["langs"] else "| ❌ "
        row += "|"
        rows.append(row)

    table = f"# Progress Overview\n\n**Total Solved:** {len(solved)}\n\n"
    table += header + "\n".join(rows)

    if README.exists():
        content = README.read_text(encoding='utf-8', errors='ignore')
    else:
        content = ""

    marker = "<!-- PROGRESS_TABLE -->"
    if marker in content:
        content = content.split(marker)[0]

    README.write_text(content + "\n\n" + marker + "\n\n" + table, encoding='utf-8')


def ingest():
    ensure_dirs()
    
    SOLUTIONS_INCOMING = INCOMING / "solutions"
    if not SOLUTIONS_INCOMING.exists() or not any(SOLUTIONS_INCOMING.iterdir()):
        print("⏸️ Incoming solutions folder is empty. Skipping ingest.")
        return

    if not incoming_ready():
        print("⏳ Incoming not ready. Waiting...")
        return

    meta_in = json.loads((INCOMING / "meta.json").read_text(encoding='utf-8'))
    url = meta_in["url"]
    date = datetime.strptime(meta_in["date"], "%Y-%m-%d")

    pb = fetch_problem_data(url)

    year = str(date.year)
    month = date.strftime("%m-%B").lower()
    week = f"week-{date.isocalendar().week:02d}"
    day = date.strftime("%Y-%m-%d")

    target = DAILY / year / month / week / day
    sol_dir = target / "solutions"
    sol_dir.mkdir(parents=True, exist_ok=True)

    # Load existing meta if it exists, otherwise create new
    meta_path = target / "meta.json"
    if meta_path.exists():
        meta = json.loads(meta_path.read_text(encoding='utf-8'))
        # Ensure all required fields are present (for backward compatibility)
        meta.setdefault("problem_id", pb["id"])
        meta.setdefault("title", pb["title"])
        meta.setdefault("slug", pb["slug"])
        meta.setdefault("difficulty", pb["difficulty"])
        meta.setdefault("date", day)
        meta.setdefault("url", url)
        meta.setdefault("topics", pb.get("topics", []))
        meta.setdefault("solutions", {})
    else:
        meta = {
            "problem_id": pb["id"],
            "title": pb["title"],
            "slug": pb["slug"],
            "difficulty": pb["difficulty"],
            "date": day,
            "url": url,
            "topics": pb.get("topics", []),
            "solutions": {}
        }

    # Process each solution file in the incoming directory
    for sol in (INCOMING / "solutions").iterdir():
        ext = sol.suffix
        lang = EXT_TO_LANG.get(ext)
        if not lang:
            continue

        clean = clean_code(sol.read_text(encoding='utf-8'))
        target_file = sol_dir / f"{lang}{ext}"
        
        # Only process if the solution file doesn't exist or is different
        if not target_file.exists() or target_file.read_text(encoding='utf-8') != clean:
            # Update language-specific directory
            lang_dir = LANG_ROOT / lang
            lang_dir.mkdir(exist_ok=True)
            
            # Save to language-specific directory with standard naming
            fname = f"{str(pb['id']).zfill(4)}_{pb['title'].lower().replace(' ','_')}{ext}"
            (lang_dir / fname).write_text(clean, encoding='utf-8')
            
            # Only update if not already present (using setdefault)
            meta["solutions"].setdefault(lang, target_file.name)
            
            # Write to daily solutions directory
            target_file.write_text(clean, encoding='utf-8')
            print(f"✅ Added/Updated {lang} solution for problem {pb['id']}")
        else:
            print(f"ℹ️ {lang} solution already exists and is unchanged")
            
        # Always remove the incoming file
        sol.unlink()
    
    # Write the updated meta back
    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding='utf-8')
    # update_progress()

    # Clean up the incoming directory
    def cleanup_incoming():
        solutions_dir = INCOMING / "solutions"
        if solutions_dir.exists():
            for f in solutions_dir.iterdir():
                f.unlink()

    cleanup_incoming()
    print("✅ Ingestion complete. Incoming cleaned.")


if __name__ == "__main__":
    ingest()
