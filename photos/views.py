from .models import Image
from django.http  import HttpResponse,Http404
from django.shortcuts import render
import datetime as dt

# Create your views here.

def photo_display(request):
    news = Article.todays_news()
    return render(request, 'index.html', {"date": date, "news": news})


def search_results(request):

    if 'article' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})