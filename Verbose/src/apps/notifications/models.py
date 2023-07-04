```python
from django.db import models
from django.conf import settings

class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ('Like', 'Like'),
        ('Comment', 'Comment'),
        ('Retweet', 'Retweet'),
    )

    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_notifications')
    tweet = models.ForeignKey('tweets.Tweet', on_delete=models.CASCADE, related_name='related_notifications')
    type = models.CharField(max_length=10, choices=NOTIFICATION_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.sender} {self.type}d your tweet'
```