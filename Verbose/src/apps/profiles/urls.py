from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('edit/', views.edit_profile_view, name='edit_profile'),
    path('follow/<str:username>/', views.follow_view, name='follow'),
    path('unfollow/<str:username>/', views.unfollow_view, name='unfollow'),
    path('<str:username>/', views.user_profile_view, name='user_profile'),
]