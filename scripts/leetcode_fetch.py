import requests
import json
import time
from typing import Optional, Dict, Any

LEETCODE_GRAPHQL = "https://leetcode.com/graphql"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com/",
    "Origin": "https://leetcode.com",
}

def extract_slug(url: str) -> str:
    """Extract problem slug from URL"""
    # Remove any query parameters
    url = url.split('?')[0]
    # Split by / and get the last part
    parts = [p for p in url.split('/') if p]
    return parts[-1] if parts else ""

def fetch_problem_from_url(url: str, max_retries: int = 3) -> Dict[str, Any]:
    """Fetch problem data using GraphQL API with retries"""
    slug = extract_slug(url)
    if not slug:
        raise ValueError(f"Could not extract slug from URL: {url}")
    
    # Clean up the slug (remove any trailing slashes or query params)
    slug = slug.split('?')[0].strip('/')
    
    query = """
    query getQuestionDetail($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionFrontendId
            title
            titleSlug
            difficulty
            topicTags {
                name
                slug
            }
            isPaidOnly
        }
    }
    """
    
    payload = {
        "operationName": "getQuestionDetail",
        "query": query,
        "variables": {"titleSlug": slug}
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.post(
                LEETCODE_GRAPHQL,
                headers=HEADERS,
                json=payload,
                timeout=15  # Increased timeout
            )
            
            # Check for rate limiting
            if response.status_code == 429:
                retry_after = int(response.headers.get('Retry-After', 5))
                print(f"⚠️ Rate limited. Waiting {retry_after} seconds...")
                time.sleep(retry_after)
                continue
                
            response.raise_for_status()
            
            data = response.json()
            if "errors" in data:
                # If we get a "question not found" error, try with a cleaned slug
                if any("question" in str(e).lower() and "not found" in str(e).lower() 
                      for e in data["errors"]):
                    # Try with a cleaned slug (remove any non-alphanumeric characters except hyphens)
                    clean_slug = ''.join(c for c in slug if c.isalnum() or c == '-')
                    if clean_slug != slug:
                        print(f"⚠️ Retrying with cleaned slug: {clean_slug}")
                        return fetch_problem_from_url(
                            f"https://leetcode.com/problems/{clean_slug}/",
                            max_retries - attempt - 1
                        )
                raise ValueError(f"GraphQL Error: {data['errors']}")
                
            q = data.get("data", {}).get("question")
            if not q:
                raise ValueError("Question data not found in response")
                
            return {
                "id": int(q["questionFrontendId"]),
                "title": q["title"],
                "slug": q["titleSlug"],
                "difficulty": q["difficulty"],
                "topics": [t["name"] for t in q.get("topicTags", [])],
                "paid_only": q.get("isPaidOnly", False),
                "url": f"https://leetcode.com/problems/{q['titleSlug']}/"
            }
            
        except (requests.RequestException, json.JSONDecodeError, KeyError) as e:
            if attempt == max_retries - 1:
                raise RuntimeError(f"Failed to fetch problem data after {max_retries} attempts: {str(e)}")
            wait_time = 2 ** attempt  # Exponential backoff
            print(f"⚠️ Attempt {attempt + 1} failed. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)