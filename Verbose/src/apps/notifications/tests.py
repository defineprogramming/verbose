```python
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Notification

User = get_user_model()

class NotificationModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')
        self.notification = Notification.objects.create(sender=self.user1, receiver=self.user2, message="Hello Verbose!")

    def test_notification_creation(self):
        self.assertEqual(Notification.objects.count(), 1)
        self.assertEqual(self.notification.sender, self.user1)
        self.assertEqual(self.notification.receiver, self.user2)
        self.assertEqual(self.notification.message, "Hello Verbose!")

class NotificationViewTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')
        self.notification = Notification.objects.create(sender=self.user1, receiver=self.user2, message="Hello Verbose!")
        self.client.login(username='user1', password='password')

    def test_notification_view(self):
        response = self.client.get('/notifications/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello Verbose!")
```
