from .models import Image
from django.http  import HttpResponse,Http404
from django.shortcuts import render
import datetime as dt

# Create your views here.

def photo_display(request):
    all_images = Image.objects.all()
    return render(request, 'index.html', {"all_images": all_images})


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,"images":searched_images})

    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})
