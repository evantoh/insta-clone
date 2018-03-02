from django.db import models
from django.contrib.auth.models import User
# User = get_user_model()


# Create your models here.

# create class profile 
class profile(models.Model):
    profile_photo=models.ImageField(upload_to = 'profile/')
    bio=models.TextField()
    user=models.ForeignKey(User)