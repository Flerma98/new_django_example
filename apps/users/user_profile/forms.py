from django import forms

from apps.users.user_profile.models import UserProfile


class UserProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image']
