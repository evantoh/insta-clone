from django.shortcuts import render,get_object_or_404, redirect
from .models import Image,Profile,Comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm,UploadForm,EditProfile
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
# Create your views here.
# function that returns the images and profile according to the last time updated to the user logged in
@login_required(login_url='/accounts/login/')
def index(request):
    current_user=request.user
    latest_images=Image.objects.order_by('-time_uploaded')
    profiles=Profile.objects.order_by('-last_updates')
    title ="INSTAGRAM CLONE"

   
    return render(request,'all_temps/index.html',{"profiles":profiles,"latest_images":latest_images,"title":title})

# getting the single image
@login_required(login_url='/accounts/login/')
def single_image(request,image_id):
    photos = Image.objects.get(id = image_id)
    return render(request,"all_temps/single_image.html", {"photos":photos})
    
  
#   function to search users according to their usernames
@login_required(login_url='/accounts/login/')
def search_users(request):
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get('username')
        searched_user = Profile.search_by_username(search_term)

        message = f"{search_term}"

        return render(request, 'all_temps/search.html',{"message":message,"profiles": searched_user})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all_temps/search.html',{"message":message})



# function to show images and profile of users
@login_required(login_url='/accounts/login/')
def profile(request):
    current_user=request.user
    profile = Profile.objects.get()
    return render(request, 'all_temps/profile.html', {'profiles':profile, "user":current_user})

# function to upload images
@login_required(login_url='/accounts/login/')
def upload(request):
    current_user = request.user         
    # profiles = Profile.get_profile()
    # for profile in profiles:
      
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = current_user
            upload.save()
            return redirect('index')
        else:
            return HttpResponse('You dont have an account with us')
    else:
        form = UploadForm()
    return render(request,'all_temps/upload.html',{"user":current_user,"form":form})


# function to edit profile
@login_required(login_url='/accounts/login/')
def edit_profile(request):
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
    

# function for user stories
@login_required(login_url='/accounts/login/')
def other_insta_users(request):
    photo_desc = Profile.objects.all()
    return render(request, 'all_temps/insta_users.html',{"profiles":photo_desc})

# function for commenting
@login_required(login_url='/accounts/login/')
def post_comment(request, pk):
    title = 'Instagrum |Comment'
    post = get_object_or_404(Image, pk=pk)
    current_user = request.user
    if request.method == 'POST':
        form =CommentForm (request.POST)
        if form.is_valid():
            post_comment = form.save(commit=False)
            post_comment.user = current_user
            post_comment.pic = post
            post_comment.save()
            return redirect('index')
    else:
        form = CommentForm()
        
    return render(request,'all_temps/comment.html',{"title":title,"form":form})

@login_required(login_url='/accounts/login/')
def user(request,user_id):
    current_user = request.user
    
    try:
        user=Profile.objects.get(id=user_id)
        images=Image.objects.filter(user=request.user)
        
    except Image.DoesNotExist:
        raise Http404()

    return render(request,"all_temps/user.html",{"user":user,"images":images})   