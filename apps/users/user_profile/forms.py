import os

from django import forms

from apps.users.user_profile.models import UserProfile
from django_example import settings


def delete_picture(picture_path):
    full_path = os.path.join(settings.MEDIA_ROOT, picture_path)

    if os.path.exists(full_path):
        os.remove(full_path)


class UserProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.has_changed() and 'profile_image' in self.changed_data and instance.pk:
            original_instance = self._meta.model.objects.get(pk=instance.pk)
            if original_instance.profile_image:
                delete_picture(original_instance.profile_image.path)
        if commit:
            instance.save()
        return instance
