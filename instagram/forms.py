from django import forms
from .models import Post,Comment,Profile



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude=['username','post']

class NewPostForm(forms.Model):
    class Meta:
        model = Post
        exclude = ['upload_by', 'pub_date', 'likes', 'location']

class ProfileForm(forms.Modelform):
 