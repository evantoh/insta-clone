from django import forms

class CommentForm(forms.Form):
your_comment=forms.CharField(label='comment',max_length=500)