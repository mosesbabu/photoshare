from .models import Image,Category,Location
from django.http  import HttpResponse,Http404
from django.shortcuts import render
import datetime as dt

# Create your views here.

def photo_display(request):
    all_images = Image.objects.all()
    category_results = Category.objects.all()
    location_results = Location.objects.all()
    return render(request, 'index.html', {"all_images": all_images, 'category_results':category_results, 'location_results':location_results})


def search_results(request):
    
    if 'searchItem' in request.GET and request.GET["searchItem"]:
        search_term = request.GET.get("searchItem")
        searched_image = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search_results.html',{"message":message,"all_images": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search_results.html',{"message":message})


def get_category(request,category):
    category_results = Category.objects.all()
    location_results = Location.objects.all()
    category_result = Image.objects.filter(image_category__name = category)
    return render(request,'index.html',{'all_images':category_result,'category_results':category_results,'location_results':location_results})

def get_location(request,location):
    category_results = Category.objects.all()
    location_results = Location.objects.all()
    location_result = Image.objects.filter(image_location__name= location)
    return render(request,'index.html',{'all_images':location_result,'category_results':category_results,'location_results':location_results})

    