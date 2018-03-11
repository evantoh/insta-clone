from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Comment,Image



# class PostForm(forms.ModelForm):

#     class Meta:
#         model = Post
#         exclude = ['user','profile', 'post_date', 'tags']


class CommentForm(forms.ModelForm):
      class Meta:
            model = Comment
            fields = ['comments',]

class UploadForm(forms.ModelForm):
      class Meta:
            model = Image
            exclude = ['user','profile','likes',]