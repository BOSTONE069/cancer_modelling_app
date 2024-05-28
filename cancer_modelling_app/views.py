from django.shortcuts import render
from serpapi import GoogleSearch
from django.conf import settings

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
        publications.append({
            'title': result.get('title'),
            'author': result.get('publication_info', {}).get('authors', 'N/A'),
            'pub_year': result.get('publication_info', {}).get('year', 'N/A'),
            'abstract': result.get('snippet', 'N/A'),
            'journal': result.get('publication_info', {}).get('journal', 'N/A')
        })

    return publications

def publications_view(request):
    keyword = request.GET.get('keyword', '')  # Default keyword is 'cancer'
    context = {
        'keyword': keyword,
        'publications': [],
        'error': None
    }

    try:
        publications = search_publications(keyword)
        context['publications'] = publications
    except Exception as e:
        context['error'] = str(e)

    return render(request, 'cancer/publications.html', context)
