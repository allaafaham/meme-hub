from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden, JsonResponse
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone
from .forms import UserProfileForm, UserUpdateForm, MemeForm, CommentForm
from .models import Meme, Comment, Label

def home(request):
    """
    Home page view that displays all memes with optional label filtering.
    
    Features:
    - Displays all memes in a grid layout
    - Allows filtering by labels
    - Hides NSFW content from non-authenticated users
    """
    # Get all memes and labels
    memes = Meme.objects.all()
    labels = Label.objects.all()
    selected_labels = request.GET.getlist('label')
    
    # Filter memes by selected labels
    if selected_labels:
        memes = memes.filter(labels__name__in=selected_labels).distinct()
    
    # Hide NSFW content from non-authenticated users
    if not request.user.is_authenticated:
        memes = memes.filter(is_nsfw=False)
    
    context = {
        'memes': memes,
        'labels': labels,
        'selected_labels': selected_labels
    }
    return render(request, 'core/home.html', context)

@login_required
def profile(request, prof=None):
    """
    User profile view for updating profile information and viewing user's memes.
    
    Features:
    - Update user information
    - Update profile picture
    - View all memes posted by the user
    """

    # Determine which user profile
    if prof != request.user.username:
        # Someone else's profile (view their memes)
        profile_user = get_object_or_404(User, username=prof)
        is_own_profile = False
    else:
        # Authenticated user's profile
        profile_user = request.user
        is_own_profile = True

    # Logged-in user is updating their own profile
    if is_own_profile and request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    elif is_own_profile:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
    else:
        # Someone else's profile (no form needed)
        user_form = None
        profile_form = None

    user_memes = profile_user.memes.all()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'memes': user_memes,
        'profile_user': profile_user,
        'is_own_profile': is_own_profile,
    }

    return render(request, 'core/profile.html', context)

@login_required
def meme_create(request):
    """
    View for creating new memes.
    
    Features:
    - Upload meme image
    - Add title and description
    - Add labels
    - Set NSFW status
    """
    if request.method == 'POST':
        form = MemeForm(request.POST, request.FILES)
        if form.is_valid():
            meme = form.save(commit=False)
            meme.user = request.user
            meme.save()
            # Save many-to-many relationships (labels)
            form.save_m2m()
            messages.success(request, 'Your meme has been created!')
            return redirect('meme_detail', pk=meme.pk)
    else:
        form = MemeForm()
    return render(request, 'core/meme_form.html', {'form': form, 'title': 'Create Meme'})

def meme_detail(request, pk):
    """
    Detailed view of a meme with comments.
    
    Features:
    - Display meme details
    - Show comments
    - Allow adding new comments
    - Track view count
    - Prevent duplicate comments
    - NSFW content protection
    """
    meme = get_object_or_404(Meme, pk=pk)
    comments = meme.comments.all()
    comment_form = CommentForm()

    # Protect NSFW content
    if meme.is_nsfw and not request.user.is_authenticated:
        return HttpResponseForbidden("You must be logged in to view NSFW content.")
    
    # Handle comment submission
    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Prevent duplicate comments within 1 minute
            last_comment = Comment.objects.filter(
                meme=meme,
                user=request.user,
                content=comment_form.cleaned_data['content']
            ).order_by('-created_at').first()
            
            if last_comment and (timezone.now() - last_comment.created_at).seconds < 60:
                messages.warning(request, 'This comment was already posted. Please wait a moment before posting again.')
            else:
                comment = comment_form.save(commit=False)
                comment.meme = meme
                comment.user = request.user
                comment.save()
                messages.success(request, 'Your comment has been added!')
            return redirect('meme_detail', pk=meme.pk)

    # Increment view count
    meme.views_count += 1
    meme.save()
    
    context = {
        'meme': meme,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, 'core/meme_detail.html', context)

@login_required
def comment_edit(request, pk):
    """
    View for editing existing comments.
    Only the comment author can edit their comments.
    """
    comment = get_object_or_404(Comment, pk=pk)
    if comment.user != request.user:
        return HttpResponseForbidden("You don't have permission to edit this comment.")
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your comment has been updated!')
            return redirect('meme_detail', pk=comment.meme.pk)
    else:
        form = CommentForm(instance=comment)
    
    return render(request, 'core/comment_form.html', {'form': form, 'comment': comment})

@login_required
def comment_delete(request, pk):
    """
    View for deleting comments.
    Only the comment author can delete their comments.
    """
    comment = get_object_or_404(Comment, pk=pk)
    if comment.user != request.user:
        return HttpResponseForbidden("You don't have permission to delete this comment.")
    
    meme_pk = comment.meme.pk
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Your comment has been deleted!')
        return redirect('meme_detail', pk=meme_pk)
    
    return render(request, 'core/comment_confirm_delete.html', {'comment': comment})

@login_required
def meme_update(request, pk):
    """
    View for updating existing memes.
    Only the meme author can update their memes.
    
    Features:
    - Update meme image
    - Update title and description
    - Update labels
    - Update NSFW status
    """
    meme = get_object_or_404(Meme, pk=pk)
    if meme.user != request.user:
        messages.error(request, "You don't have permission to edit this meme.")
        return redirect('meme_detail', pk=meme.pk)

    if request.method == 'POST':
        form = MemeForm(request.POST, request.FILES, instance=meme)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your meme has been updated!')
            return redirect('meme_detail', pk=meme.pk)
    else:
        form = MemeForm(instance=meme)
    return render(request, 'core/meme_form.html', {'form': form, 'title': 'Update Meme'})

@login_required
def meme_delete(request, pk):
    """
    View for deleting memes.
    Only the meme author can delete their memes.
    """
    meme = get_object_or_404(Meme, pk=pk)
    if meme.user != request.user:
        return HttpResponseForbidden("You don't have permission to delete this meme.")
    
    if request.method == 'POST':
        meme.delete()
        messages.success(request, 'Your meme has been deleted!')
        return redirect('profile')
    return render(request, 'core/meme_confirm_delete.html', {'meme': meme})
