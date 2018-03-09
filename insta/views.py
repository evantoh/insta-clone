from django.shortcuts import render,get_object_or_404, redirect
from .models import Image,Profile,Comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
# Create your views here.
# function that returns the images and profile according to the last time updated to the user logged in
def user_timelines(request):
    current_user=request.user
    images=Image.objects.order_by('-time_uploaded')
    profiles=Profile.objects.order_by('-last_updates')
    title ="INSTAGRAM CLONE"

   
    return render(request,'all_temps/user_timelines.html',{"images":images,"profiles":profiles,"title":title})

# getting the single image
def single_image(request,image_id):
    photos = Image.objects.get(id = image_id)
    return render(request,"all_temps/single_image.html", {"photos":photos})
    
  
def search_users(request):
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get('username')
        searched_user = Profile.search_by_username(search_term)

        message = f"{search_term}"

        return render(request, 'all_temps/search.html',{"message":message,"profiles": searched_user})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all_temps/search.html',{"message":message})




def user_profile(request,id):
    profile = Profile.objects.get(id=id)
    images = Image.objects.all()
    return render(request, 'all_temps/profile.html', {'profile':profile, 'images':images})




def other_insta_users(request):
    photo_desc = Profile.objects.all()
    return render(request, 'all_temps/insta_users.html',{"profiles":photo_desc})

def edit_profile(request):
    title = 'Instagram |Edit'
    current_user = request.user
    if request.method == 'POST':
        form = EditProfile(request.POST,request.FILES)
        if form.is_valid():
            update = form.save(commit=False)
            update.user = current_user
            update.profile = current_profile
            update.save()
            return redirect('profile')
    else:
        form = EditProfile()
    return render(request, 'all_temps/edit_profile.html', {"title":title, "form":form})


@login_required(login_url='/accounts/login/')
def post_comment(request, id):
    title = 'Instagrum |Comment'
    post = get_object_or_404(Image, id=id)
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post_comment = form.save(commit=False)
            post_comment.user = current_user
            post_comment.pic = post
            post_comment.save()
            return redirect('index')
    else:
        form = CommentForm()
        
    return render(request,'all_temps/comments.html',{"title":title,"form":form})