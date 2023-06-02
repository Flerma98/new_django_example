from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import UserProfile
from ..models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

    @staticmethod
    def delete(instance: UserProfile):
        instance.delete_picture()
        instance.delete()


class UserProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['profile_image']
        extra_kwargs = {
            'profile_image': {
                'required': True
            }
        }

    def validate(self, attrs):
        if 'profile_image' not in attrs:
            raise ValidationError(_('You must provide an image.'))
        return attrs

    def save(self, **kwargs):
        instance: User = super().save(**kwargs)
        instance.profile.delete_picture()
        instance.profile.profile_image = self.initial_data['profile_image']
        instance.profile.save()
        return super().save(**kwargs)
