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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget=forms.TextInput()
    class Meta
        model = Profile
        exclude=['username']


class LikeForm(forms.Modelform):
    class Meta:
        exclude=['username', 'post']           