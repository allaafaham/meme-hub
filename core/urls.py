from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Meme URLs
    path('meme/new/', views.meme_create, name='meme_create'),
    path('meme/<int:pk>/', views.meme_detail, name='meme_detail'),
    path('meme/<int:pk>/edit/', views.meme_update, name='meme_update'),
    path('meme/<int:pk>/delete/', views.meme_delete, name='meme_delete'),
] 

