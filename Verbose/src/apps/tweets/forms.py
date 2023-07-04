from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'image']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > 280:
            raise forms.ValidationError("This tweet is too verbose! Please limit your tweet to 280 characters.")
        return content

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5*1024*1024:
                raise forms.ValidationError("This image is too large! Please limit your image size to 5MB.")
        return image