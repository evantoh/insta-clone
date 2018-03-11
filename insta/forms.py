from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Comment,Image,Profile



class EditProfile(forms.ModelForm):
      class Meta:
            model = Profile
            exclude = ['user']


class CommentForm(forms.ModelForm):
      class Meta:
            model = Comment
            fields = ['comments',]

class UploadForm(forms.ModelForm):
      class Meta:
            model = Image
            exclude = ['user','profile','likes',]