from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# User = get_user_model()

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

    @classmethod
    def search_by_username(cls,search_term):
        profiles = cls.objects.filter(user__username__icontains=search_term)
        return profiles
    @classmethod
    def get_profile(cls):
        profile=Profile.objects.all()
        return profile

    @classmethod
    def find_profile(cls,search_term):
        profiles = cls.objects.filter(user__username__icontains=search_term)
        return profiles
# test save method in profile
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete


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

    def __str__(self):
        return self.image_name

    # create class to order the images 
    class Meta:
         ordering=['-time_uploaded']

    # method to save image class objects
    def save_images(self):
        self.save

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls,id): 
        image = Image.objects.filter(id = Image.id)
        return image

    
    @classmethod
    def update_caption(cls,id,caption):
        captions = Image.objects.filter(id=id).update(caption = caption)
        return captions

    @classmethod
    def get_images(cls):
        image = Image.objects.all()
        return image
# create class comments

class Comment(models.Model):
    comments=models.CharField(max_length =250,blank=True)
    author = models.ForeignKey(User,  on_delete=models.CASCADE, blank=True,null=True)
    pic = models.ForeignKey(Image,on_delete=models.CASCADE, related_name='comments',blank=True,null=True)
    time_comment = models.DateTimeField(auto_now_add=True, null=True)
   
# clss that orders comment according to the time commented
    class Meta:
       ordering = ['-time_comment']

    def save_comment(self):
        self.save()

    def delete_comment(self):
        return self.delete()

    def __str__(self):
        return self.text

    @classmethod
    def get_comments(cls):
        comment=Comment.objects.all()
        return comment
        

