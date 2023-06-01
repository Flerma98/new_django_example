import os

from django import forms

from apps.users.user_profile.models import UserProfile
from django_example import settings


class UserProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.has_changed() and 'profile_image' in self.changed_data and instance.pk:
            original_instance: UserProfile = self._meta.model.objects.get(pk=instance.pk)
            original_instance.delete_picture()
        if commit:
            instance.save()
        return instance
