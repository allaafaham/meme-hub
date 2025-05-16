from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Meme, Comment

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email'] 

class MemeForm(forms.ModelForm):
    class Meta:
        model = Meme
        fields = ['title', 'image', 'description', 'is_nsfw']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'is_nsfw': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        } 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write your comment here...',
                'class': 'form-control'
            })
        } 