```python
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, bio='Verbose user')

    def test_profile_created(self):
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.bio, 'Verbose user')

    def test_profile_str(self):
        self.assertEqual(str(self.profile), 'testuser')

    def test_profile_following(self):
        user2 = User.objects.create_user(username='testuser2', password='12345')
        profile2 = Profile.objects.create(user=user2, bio='Another Verbose user')
        self.profile.followers.add(profile2)
        self.assertTrue(self.profile.is_following(profile2))
        self.assertTrue(profile2.is_followed_by(self.profile))
```