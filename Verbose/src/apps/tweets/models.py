```python
from django.db import models
from django.conf import settings

class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='tweet_likes')
    retweets = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='tweet_retweets')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content[:50]

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, related_name='comments', on_delete=models.CASCADE)
    content = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content[:50]
```