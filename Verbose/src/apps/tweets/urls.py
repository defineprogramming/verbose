from django.urls import path
from . import views

app_name = 'tweets'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_tweet, name='new_tweet'),
    path('<int:tweet_id>/', views.view_tweet, name='view_tweet'),
    path('<int:tweet_id>/edit/', views.edit_tweet, name='edit_tweet'),
    path('<int:tweet_id>/delete/', views.delete_tweet, name='delete_tweet'),
    path('user/<str:username>/', views.user_tweets, name='user_tweets'),
]