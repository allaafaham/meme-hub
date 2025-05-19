from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden, JsonResponse
from django.db.models import Q
from .forms import UserProfileForm, UserUpdateForm, MemeForm, CommentForm
from .models import Meme, Comment, Label

def home(request):
    memes = Meme.objects.all()
    labels = Label.objects.all()
    selected_labels = request.GET.getlist('label')
    
    # Filter by labels if selected
    if selected_labels:
        memes = memes.filter(labels__name__in=selected_labels).distinct()
    
    # Filter NSFW content for non-authenticated users
    if not request.user.is_authenticated:
        memes = memes.filter(is_nsfw=False)
    
    context = {
        'memes': memes,
        'labels': labels,
        'selected_labels': selected_labels
    }
    return render(request, 'core/home.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
    
    user_memes = request.user.memes.all()
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'memes': user_memes
    }
    return render(request, 'core/profile.html', context)

@login_required
def meme_create(request):
    if request.method == 'POST':
        form = MemeForm(request.POST, request.FILES)
        if form.is_valid():
            meme = form.save(commit=False)
            meme.user = request.user
            meme.save()
            messages.success(request, 'Your meme has been created!')
            return redirect('meme_detail', pk=meme.pk)
    else:
        form = MemeForm()
    return render(request, 'core/meme_form.html', {'form': form, 'title': 'Create Meme'})

def meme_detail(request, pk):
    meme = get_object_or_404(Meme, pk=pk)
    comments = meme.comments.all()
    comment_form = CommentForm()

    if meme.is_nsfw and not request.user.is_authenticated:
        return HttpResponseForbidden("You must be logged in to view NSFW content.")
    
    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.meme = meme
            comment.user = request.user
            comment.save()
            messages.success(request, 'Your comment has been added!')
            return redirect('meme_detail', pk=meme.pk)

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
    meme = get_object_or_404(Meme, pk=pk)
    if meme.user != request.user:
        return HttpResponseForbidden("You don't have permission to delete this meme.")
    
    if request.method == 'POST':
        meme.delete()
        messages.success(request, 'Your meme has been deleted!')
        return redirect('profile')
    return render(request, 'core/meme_confirm_delete.html', {'meme': meme})
