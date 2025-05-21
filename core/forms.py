from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Meme, Comment, Label


class UserProfileForm(forms.ModelForm):
    """
    Form for updating user profile information.
    """

    class Meta:
        model = UserProfile
        fields = ["bio", "avatar"]


class UserUpdateForm(forms.ModelForm):
    """
    Form for updating basic user information.
    """

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class MemeForm(forms.ModelForm):
    """
    Form for creating and updating memes.
    """

    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "list-unstyled"}),
        required=True,
        help_text="Select at least one label for your meme",
    )

    class Meta:
        model = Meme
        fields = ["title", "image", "description", "is_nsfw", "labels"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
            "is_nsfw": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
        }


class CommentForm(forms.ModelForm):
    """
    Form for adding and editing comments on memes.
    """

    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Write your comment here...",
                    "class": "form-control",
                }
            )
        }
