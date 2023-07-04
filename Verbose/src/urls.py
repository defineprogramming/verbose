from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('apps.authentication.urls')),
    path('profiles/', include('apps.profiles.urls')),
    path('tweets/', include('apps.tweets.urls')),
    path('notifications/', include('apps.notifications.urls')),
    path('', include('apps.core.urls')),
]