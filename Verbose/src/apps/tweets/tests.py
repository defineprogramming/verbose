```python
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Tweet

User = get_user_model()

class TweetModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(username='testuser', password='12345')
        Tweet.objects.create(content='A test tweet', user=User.objects.get(id=1))

    def test_content_label(self):
        tweet = Tweet.objects.get(id=1)
        field_label = tweet._meta.get_field('content').verbose_name
        self.assertEquals(field_label, 'content')

    def test_content_max_length(self):
        tweet = Tweet.objects.get(id=1)
        max_length = tweet._meta.get_field('content').max_length
        self.assertEquals(max_length, 280)

    def test_object_name_is_content(self):
        tweet = Tweet.objects.get(id=1)
        expected_object_name = f'{tweet.content}'
        self.assertEquals(expected_object_name, str(tweet))

class TweetViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='testuser', password='12345')
        Tweet.objects.create(content='A test tweet', user=User.objects.get(id=1))

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/tweets/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/tweets/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tweets.html')
```