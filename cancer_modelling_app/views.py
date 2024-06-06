from django.shortcuts import render
from serpapi import GoogleSearch
from django.conf import settings

def extract_publication_info(result):
    return {
        'title': result.get('title'),
        'author': result.get('publication_info', {}).get('summary', '').split('-')[0].strip(),
        'pub_year': result.get('publication_info', {}).get('summary', '').split('-')[-1].strip(),
        'abstract': result.get('snippet', 'N/A'),
        'journal': result.get('publication_info', {}).get('summary', '').split(',')[1].strip(),
        'link': result.get('link', '#')  # Extract the publication link
    }

def search_publications(keyword):
    params = {
        "engine": "google_scholar",
        "q": keyword,
        "api_key": settings.SERPAPI_KEY
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    organic_results = results.get("organic_results", [])

    publications = []
    for result in organic_results:
        publication_info = extract_publication_info(result)
        publications.append(publication_info)

    return publications

def publications_view(request):
    keyword = request.GET.get('keyword', 'cancer')  # Default keyword is 'cancer'
    try:
        publications = search_publications(keyword)
    except Exception as e:
        # Handle any exceptions that might occur
        context = {
            'error': str(e),
            'keyword': keyword,
            'publications': [],
        }
        return render(request, 'cancer/publications.html', context)

    context = {
        'publications': publications,
        'keyword': keyword,
    }
    return render(request, 'cancer/publications.html', context)
