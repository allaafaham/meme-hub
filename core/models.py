from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from cloudinary.models import CloudinaryField


# Create your models here.

class Label(models.Model):
    """
    Label model for categorizing memes.
    
    Each label has a unique name and optional description.
    Labels are used to organize and filter memes by category.
    """
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']  # Labels are ordered alphabetically

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    """
    Extended user profile model.
    
    Extends the default Django User model with additional fields:
    - bio: User's biography/description
    - avatar: Profile picture stored in Cloudinary
    - date_joined: Timestamp of profile creation
    
    Created automatically when a new User is created through signals.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = CloudinaryField('image', default='avatars/default.png', asset_folder='/avatars/',)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
class Meme(models.Model):
    """
    Main Meme model for storing meme posts.
    
    Features:
    - Title and optional description
    - Image stored in Cloudinary
    - NSFW flag for content filtering
    - View counter
    - Multiple labels through M2M relationship
    - Automatic timestamps for creation and updates
    
    Related to:
    - User (creator)
    - Labels (categories)
    - Comments (through reverse relation)
    """
    title = models.CharField(max_length=200)
    image = CloudinaryField('image', default='memes/default.png', asset_folder='/memes/',)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memes')
    is_nsfw = models.BooleanField(default=False)
    views_count = models.PositiveIntegerField(default=0)
    labels = models.ManyToManyField(Label, related_name='memes')
    
    class Meta:
        ordering = ['-created_at']  # Newest memes first
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        """Returns the URL to access a particular meme instance."""
        return reverse('meme_detail', args=[str(self.id)])

class Comment(models.Model):
    """
    Comment model for meme discussions.
    
    Features:
    - Text content
    - Automatic timestamps for creation and updates
    - Linked to both meme and commenter
    
    Related to:
    - Meme (commented on)
    - User (commenter)
    """
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']  # Newest comments first

    def __str__(self):
        return f'Comment by {self.user.username} on {self.meme.title}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler to automatically create a UserProfile when a new User is created.
    """
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal handler to save UserProfile whenever the associated User is saved.
    """
    instance.userprofile.save()
