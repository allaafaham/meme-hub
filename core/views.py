from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from .forms import UserProfileForm, UserUpdateForm, MemeForm
from .models import Meme

def home(request):
    memes = Meme.objects.all()
    if not request.user.is_authenticated:
        memes = memes.filter(is_nsfw=False)
    return render(request, 'core/home.html', {'memes': memes})

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
    if meme.is_nsfw and not request.user.is_authenticated:
        return HttpResponseForbidden("You must be logged in to view NSFW content.")
    meme.views_count += 1
    meme.save()
    return render(request, 'core/meme_detail.html', {'meme': meme})

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
