from django.db import models
from django.contrib.auth.models import User
# User = get_user_model()


# Create your models here.

# create model profile 
class Profile(models.Model):
    profile_photo=models.ImageField(upload_to = 'profile/')
    bio=models.TextField()
    user=models.ForeignKey(User)
    last_updates=models.DateTimeField(auto_now_add=True,null=True)

# order the profile objects according to when the updates
    class Meta:
        ordering =['-last_updates']

    def __str__(self):
        return self.user.username
# test save method in profile
    def save_profile(self):
        self.save()


# create model image
class Image(models.Model):
    image=models.ImageField(upload_to='pics/',null=True)
    image_name=models.CharField(max_length =60,null=True)
    image_caption=models.TextField(null=True)
    profile=models.ForeignKey(Profile,null=True)
    # comments=models.ForeignKey(Comment)
    likes=models.IntegerField(default=0)
    time_uploaded=models.DateTimeField(auto_now_add=True,null=True)
    user=models.ForeignKey(User,null=True)

    # create class to order the images 
    class Meta:
         ordering=['-time_uploaded']

    # method to save image class objects
    def save_images(self):
        self.save
# create class comments

class Comment(models.Model):
    text=models.CharField(max_length =250,blank=True)
    author = models.ForeignKey(User,  on_delete=models.CASCADE, blank=True,null=True)
    # Image, on_delete=models.CASCADE, related_name='comments')
    time_comment = models.DateTimeField(auto_now_add=True, null=True)
   
# clss that orders comment according to the time commented
    class Meta:
       ordering = ['-time_comment']

    def save_comment(self):
        self.save()

    def __str__(self):
        return self.text


class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    post_date = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to="posts/")

    caption = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    class Meta:

        ordering = ['-post_date']


    user = models.ForeignKey(User, on_delete=models.CASCADE)

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    post_date = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to="posts/")

    caption = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    class Meta:

        ordering = ['-post_date']