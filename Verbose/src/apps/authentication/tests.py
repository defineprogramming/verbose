```python
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import User

class UserTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='12345')

    def test_user_creation(self):
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.__str__(), 'testuser')

    def test_user_login(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': '12345'})
        self.assertEqual(response.status_code, 302)

    def test_user_logout(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_user_register(self):
        response = self.client.post(reverse('register'), {'username': 'newuser', 'password1': 'abcdef', 'password2': 'abcdef'})
        self.assertEqual(response.status_code, 302)
        new_user = get_user_model().objects.get(username='newuser')
        self.assertIsInstance(new_user, User)
```
