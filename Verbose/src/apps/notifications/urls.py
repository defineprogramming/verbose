from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.NotificationListView.as_view(), name='notification_list'),
    path('<int:pk>/', views.NotificationDetailView.as_view(), name='notification_detail'),
    path('create/', views.NotificationCreateView.as_view(), name='notification_create'),
    path('<int:pk>/update/', views.NotificationUpdateView.as_view(), name='notification_update'),
    path('<int:pk>/delete/', views.NotificationDeleteView.as_view(), name='notification_delete'),
]