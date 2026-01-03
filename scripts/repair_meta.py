from pathlib import Path
import json
import time
from leetcode_fetch import fetch_problem_from_url

ROOT = Path("daily-challenges")

def repair():
    updated = 0
    processed_urls = set()  # To avoid duplicate API calls
    url_to_data = {}  # Cache for URL to problem data

    # First pass: collect all unique URLs
    print("🔍 Collecting problem URLs...")
    meta_files = list(ROOT.rglob("meta.json"))
    total_files = len(meta_files)
    
    for i, meta_path in enumerate(meta_files, 1):
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            if "url" in meta:
                processed_urls.add(meta["url"])
        except (json.JSONDecodeError, KeyError) as e:
            print(f"⚠️ Error reading {meta_path}: {e}")
        print(f"\rProcessed {i}/{total_files} files", end="")
    
    print(f"\n📡 Fetching data for {len(processed_urls)} unique problems...")
    
    # Second pass: fetch data for each unique URL
    for i, url in enumerate(processed_urls, 1):
        try:
            print(f"\rFetching {i}/{len(processed_urls)}: {url}", end="")
            url_to_data[url] = fetch_problem_from_url(url)
            time.sleep(1)  # Be nice to LeetCode's servers
        except Exception as e:
            print(f"\n❌ Failed to fetch {url}: {e}")
            continue
    
    # Third pass: update all meta files
    print("\n🔄 Updating meta files...")
    for i, meta_path in enumerate(meta_files, 1):
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            if "url" not in meta or meta["url"] not in url_to_data:
                continue
                
            fresh = url_to_data[meta["url"]]
            needs_update = False
            
            # Only update if the data is different
            for key in ["id", "title", "slug", "difficulty", "topics"]:
                if meta.get(key) != fresh.get(key):
                    meta[key] = fresh[key]
                    needs_update = True
            
            if needs_update:
                meta_path.write_text(
                    json.dumps(meta, indent=2, ensure_ascii=False),
                    encoding="utf-8"
                )
                updated += 1
                print(f"\r✅ Updated {meta_path}", " " * 30)
            else:
                print(f"\rℹ️ No changes needed for {meta_path}", " " * 30)
                
        except Exception as e:
            print(f"\n⚠️ Error processing {meta_path}: {e}")

    print(f"\n🎉 Completed repair: {updated} files updated out of {total_files}")

if __name__ == "__main__":
    repair()