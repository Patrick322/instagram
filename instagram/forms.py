from django import forms
from .models import Post,Comment,Profile



class NewPostForm(forms.ModelForm)
    class Meta:
        model=Comment
        exclude=['username','post']