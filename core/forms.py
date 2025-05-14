from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Meme

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

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