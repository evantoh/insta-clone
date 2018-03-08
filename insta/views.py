from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Image,Profile,Comment,Like,Post
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
@login_required(login_url='/accounts/login/')
def my_profile(request,user_id):
    current_user=request.user
    my_photos=Profile.objects.get(user_id=current_user)
    
    return render(request,'profile.html',{"my_photos":my_photos})


def user_profile(request):
    profile = Profile.objects.get(id=user_id)
    images = Image.objects.all().filter(user_id=user_id)
    return render(request, 'profile.html', {'profile':profile, 'images':images})


@login_required(login_url='/accounts/register')
def comment(request,id):

    current_user = request.user

    current_post = Post.objects.get(id=id)

    if request.method == 'POST':

        form = CommentForm(request.POST)

        if form.is_valid:

            comment = form.save(commit=False)

            comment.user = current_user

            comment.post = current_post

            comment.save()

            return redirect(post_look,current_post.id)

    else:

        form = CommentForm()

    title = f'Comment {current_post.user.username}'

    return render(request,'comment.html', {"title":title,"form":form,"current_post":current_post})


    def post_look(request,id):
        '''
    View function to display a single post, its comments and likes
    '''
    current_user = request.user
    try:
        current_post = Post.objects.get(id=id)

        title = f'{current_post.user.username}'
        comments = Comment.get_post_comments(id)

        likes = Like.num_likes(id)

        like = Like.objects.filter(post=id).filter(user=current_user)

    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'post_look.html', {"title":title, "post":current_post,"comments":comments,"likes":likes,"like":like })
