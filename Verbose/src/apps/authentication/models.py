```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    verbose_score = models.IntegerField(default=0)

    def increase_verbose_score(self, increment):
        self.verbose_score += increment
        self.save()

    def decrease_verbose_score(self, decrement):
        if self.verbose_score - decrement >= 0:
            self.verbose_score -= decrement
            self.save()
        else:
            raise ValueError("Verbose score cannot be negative.")
```