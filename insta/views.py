from django.shortcuts import render
from django.http import HttpResponse
from .models import image

# Create your views here.
def welcome(request):
    return HttpResponse('welcome to kkjkrj')
def search_results(request):
    
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})
def display_image(request):
    images=image.objects.all()

    return render(request,'display_image.html',{"images":images})
    