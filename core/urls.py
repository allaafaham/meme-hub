from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),

    # Meme URLs
    path('meme/new/', views.meme_create, name='meme_create'),
    path('meme/<int:pk>/', views.meme_detail, name='meme_detail'),
    path('meme/<int:pk>/edit/', views.meme_update, name='meme_update'),
    path('meme/<int:pk>/delete/', views.meme_delete, name='meme_delete'),

    # Comment URLs
    path('comment/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),

] 

