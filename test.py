# test_serpapi.py

from serpapi import GoogleSearch

params = {
    "engine": "google_scholar",
    "q": "cancer",
    "api_key": "16b684590d3c08a06278d6ea354b57f255154f4d6beb74d5b9da4fc0c3c4ba58"
}

search = GoogleSearch(params)
results = search.get_dict()
organic_results = results.get("organic_results", [])

print(organic_results)
