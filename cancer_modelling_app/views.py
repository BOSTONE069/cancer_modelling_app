from django.shortcuts import redirect, render
from serpapi import GoogleSearch
from django.conf import settings
from .models import SearchAnalytics 
from .forms import ContactForm
from django.http import HttpResponse


def extract_publication_info(result):
    return {
        'title': result.get('title'),
        'author': result.get('publication_info', {}).get('summary', '').split('-')[0].strip(),
        'pub_year': result.get('publication_info', {}).get('summary', '').split('-')[-1].strip(),
        'abstract': result.get('snippet', 'N/A'),
        'journal': result.get('publication_info', {}).get('summary', '').split(',')[1].strip(),
        'link': result.get('link', '#')
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
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        return redirect('publications_search', keyword=keyword)
    else:
        keyword = request.GET.get('keyword')  # Default keyword is 'cancer'
    # Save the search keyword to the database
    if keyword:
        SearchAnalytics.objects.create(keyword=keyword)

    try:
        publications = search_publications(keyword)
    except Exception as e:
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


def homepage(request):
    return render(request, 'cancer/index.html')

def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Your message has been sent. Thank you!', status=200)
        else:
            return HttpResponse('There was an error in your form submission.', status=400)
    else:
        form = ContactForm()
    return render(request, 'cancer/contacts.html', {'form': form})