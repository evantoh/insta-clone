from django.db import models
from django.contrib.auth.models import User
# User = get_user_model()


# Create your models here.

# create class profile 
class profile(models.Model):
    profile_photo=models.ImageField(upload_to = 'profile/')
    bio=models.TextField()
    user=models.ForeignKey(User)


# create class image
class image(models.Model):
    image=models.ImageField(upload_to='pics/')
    image_name=models.CharField(max_length =60)
    image_caption=models.TextField()
    profile=models.ForeignKey(profile)
    # comments=models.ForeignKey(comments)
    likes=models.IntegerField(default=0)

# create class comments

class Comments(models.Model):
    comment = models.CharField(max_length=300)
    user = models.ForeignKey(User, null=True)
    image = models.ForeignKey(image, null=True)
    time_comment = models.DateTimeField(auto_now_add=True, null=True)
# clss that orders comment according to the time commented
    class Meta:
       ordering = ['-time_comment']