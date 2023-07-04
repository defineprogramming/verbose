```python
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def notifications(request):
    user_notifications = Notification.objects.filter(user=request.user).order_by('-date')
    return render(request, 'notifications.html', {'notifications': user_notifications})

@login_required
def read_notification(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    if request.user == notification.user:
        notification.read = True
        notification.save()
    return render(request, 'notification.html', {'notification': notification})
```