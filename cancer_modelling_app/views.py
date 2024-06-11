from django.shortcuts import redirect, render
from serpapi import GoogleSearch
from django.conf import settings
from .models import SearchAnalytics 
from .forms import ContactForm
from django.http import HttpResponse
from django.db.models import Count
from django.http import JsonResponse

def extract_publication_info(result):
    """
    The function `extract_publication_info` takes a dictionary `result` as input and extracts specific
    information such as title, author, publication year, abstract, journal, and link from the
    dictionary, returning them in a new dictionary.
    
    :param result: The `extract_publication_info` function takes a `result` dictionary as input and
    extracts specific information from it to create a new dictionary with the following keys:
    :return: The function `extract_publication_info` takes a `result` dictionary as input and returns a
    new dictionary with the following keys and values:
    """
    return {
        'title': result.get('title'),
        'author': result.get('publication_info', {}).get('summary', '').split('-')[0].strip(),
        'pub_year': result.get('publication_info', {}).get('summary', '').split('-')[-1].strip(),
        'abstract': result.get('snippet', 'N/A'),
        'journal': result.get('publication_info', {}).get('summary', '').split(',')[1].strip(),
        'link': result.get('link', '#')
    }

def search_publications(keyword):
    """
    The function `search_publications` searches for publications related to a given keyword using the
    Google Scholar search engine.
    
    :param keyword: The `search_publications` function takes a keyword as input and searches for
    publications related to that keyword using the Google Scholar search engine. It uses the SERPAPI_KEY
    from the settings to make the search request
    :return: The function `search_publications` returns a list of publication information based on the
    keyword search using the Google Scholar search engine.
    """
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
    """
    The `publications_view` function in Python handles requests to search for publications based on a
    keyword, saves the search keyword to the database, and displays the search results on a webpage.
    
    :param request: The `request` parameter in the `publications_view` function is an object that
    represents the HTTP request made by a user. It contains information about the request, such as the
    method used (GET, POST, etc.), any data sent with the request (such as form data), and other
    metadata
    :return: The `publications_view` function returns a response with the rendered template
    'cancer/publications.html' along with the context containing publications and keyword information.
    If an exception occurs during the search for publications, it will return a response with an error
    message and an empty list of publications.
    """
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


    """
    The `homepage` function returns a rendered HTML template for the cancer index page.
    
    :param request: The `request` parameter in the `homepage` function is typically an HttpRequest
    object that represents the request made by a user to access a web page. It contains information
    about the request such as the user's browser information, session data, and any data sent in the
    request (e.g., form data
    :return: The `homepage` function is returning a rendered HTML template named 'index.html' located in
    the 'cancer' directory.
    """
def homepage(request):
    return render(request, 'cancer/index.html')

def about(request):
    return render(request, 'cancer/about.html')

def contacts(request):
    """
    The `contacts` function handles form submissions for a contact form in a Django web application.
    
    :param request: The `request` parameter in the `contacts` function is an object that represents the
    HTTP request made by a client to the server. It contains information such as the request method
    (GET, POST, etc.), headers, user data, and any data sent in the request body. In this function,
    :return: The contacts view function returns a rendered HTML template 'contacts.html' with a
    ContactForm instance passed as context data when the HTTP request method is not POST. If the request
    method is POST, it processes the form data, saves it if valid, and returns an appropriate
    HttpResponse message based on the form validation result.
    """
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



def analytics_view(request):
    # Fetch search data and count occurrences of each keyword
    search_data = SearchAnalytics.objects.values('keyword').annotate(count=Count('keyword')).order_by('-count')

    # Prepare data for Chart.js
    keywords = [entry['keyword'] for entry in search_data]
    counts = [entry['count'] for entry in search_data]

    context = {
        'keywords': keywords,
        'counts': counts,
    }
    return render(request, 'admin/analytics.html', context)