from django import forms
from .models import Comments, Post


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['description', 'content', 'link', 'tags']


class NewCommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['comment']
