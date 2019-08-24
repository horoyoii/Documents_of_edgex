from django import forms
from .models import Post, Done


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
 
        fields = ['number','title', 'is_meta','slug', 'content']


class CreateDone(forms.ModelForm):
    class Meta:
        model = Done

        fields = ['pub_date', 'title']
