from django.contrib import admin
from .models import UserProfile, Meme


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_joined']
    search_fields = ['user__username', 'bio']


@admin.register(Meme)
class MemeAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at', 'is_nsfw', 'views_count']
    list_filter = ['is_nsfw', 'created_at']
    search_fields = ['title', 'description', 'user__username']
    date_hierarchy = 'created_at'
