from serpapi import GoogleSearch
import os

def search_google(query: str) -> str:
    params = {
        "q": query,
        "api_key": os.getenv("SERPAPI_API_KEY"),
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    snippets = [res["snippet"] for res in results.get("organic_results", []) if "snippet" in res]
    return "\n".join(snippets[:5])

