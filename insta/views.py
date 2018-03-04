from django.shortcuts import render
from django.http import HttpResponse
from .models import image,profile
from django.contrib.auth.decorators import login_required

# Create your views here.
# function that returns the images and profile according to the last time updated
def user_timelines(request):
    current_user=request.user
    images=image.objects.order_by('-time_uploaded')
    profiles=profile.objects.order_by('-last_updates')
    return render(request,'user_timelines.html',{"images":images,"profiles":profiles})
    
  
def search_results(request):
    
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

#create view to handle thre profile
# @login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user=request.user
    my_photos=profile.objects.get(user_id=current_user)
    images=image.objects.all().filter(profile_id=current_user.id)
    return render(request,'profile.html',{"my_photos":my_photos,"images":images})