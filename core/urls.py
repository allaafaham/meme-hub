from django.urls import path
from . import views

urlpatterns = [
    # Main pages
    path('', views.home, name='home'),  
    path('profile/<str:prof>/', views.profile, name='profile'),
    
    
    # Meme URLs - CRUD operations
    path('meme/new/', views.meme_create, name='meme_create'),  
    path('meme/<int:pk>/', views.meme_detail, name='meme_detail'),  
    path('meme/<int:pk>/edit/', views.meme_update, name='meme_update'),  
    path('meme/<int:pk>/delete/', views.meme_delete, name='meme_delete'),  
    
    # Comment URLs - Edit and Delete operations
    path('comment/<int:pk>/edit/', views.comment_edit, name='comment_edit'),  
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),  
] 

