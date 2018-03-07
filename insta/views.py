from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Profile,Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
# function that returns the images and profile according to the last time updated to the user logged in
def user_timelines(request):
    current_user=request.user
    images=Image.objects.order_by('-time_uploaded')
    profiles=Profile.objects.order_by('-last_updates')
    comments=Comment.objects.order_by('-time_comment')
    return render(request,'user_timelines.html',{"images":images,"profiles":profiles,"comments":comments})

# getting the single image
def single_image(request,image_id):
    photos = Image.objects.get(id = image_id)
    return render(request,"single_image.html", {"photos":photos})
    
  
def search_results(request):
    
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

# create view to handle thre profile
# @login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user=request.user
    my_photos=Profile.objects.get(user_id=current_user)
    
    return render(request,'profile.html',{"my_photos":my_photos,"images":images})