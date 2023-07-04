```python
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    verbose_score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile', kwargs={'username': self.user.username})

    def increase_verbose_score(self):
        self.verbose_score += 1
        self.save()

    def decrease_verbose_score(self):
        if self.verbose_score > 0:
            self.verbose_score -= 1
            self.save()
```
