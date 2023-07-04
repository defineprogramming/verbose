from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date', 'profile_picture']

    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        if len(bio) > 160:
            raise forms.ValidationError("Bio cannot be more than 160 characters.")
        return bio

    def clean_location(self):
        location = self.cleaned_data.get('location')
        if len(location) > 30:
            raise forms.ValidationError("Location cannot be more than 30 characters.")
        return location

    def clean_birth_date(self):
        birth_date = self.cleaned_data.get('birth_date')
        if birth_date is not None and birth_date.year < 1900:
            raise forms.ValidationError("Invalid birth date.")
        return birth_date

    def clean_profile_picture(self):
        profile_picture = self.cleaned_data.get('profile_picture')
        if profile_picture:
            if profile_picture.size > 5*1024*1024:
                raise forms.ValidationError("Image file too large ( > 5mb )")
            if not profile_picture.content_type in ["image/jpeg", "image/png"]:
                raise forms.ValidationError("Unsupported file type. Use JPEG or PNG.")
        return profile_picture