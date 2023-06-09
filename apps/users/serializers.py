from rest_framework import serializers

from apps.users.validators import (
    UniqueUsernameValidator, PasswordStrengthValidator,
)
from .models import User
from .user_profile.models import UserProfile
from .user_profile.serializers import UserProfileSerializer


class BaseUserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=False)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'username': {
                'required': True,
                'validators': (UniqueUsernameValidator(User.objects.all()),)
            },
            'password': {
                'required': True,
                'write_only': True,
                'validators': (PasswordStrengthValidator(),)
            },
            'date_time_created': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)

        # create user
        normal_password = validated_data.pop('password')
        user_created = User.objects.create(**validated_data)
        user_created.set_password(normal_password)

        # create profile if exist
        if profile_data:
            profile_saved = UserProfile.objects.create(**profile_data)
            user_created.profile = profile_saved

        user_created.save(update_fields=('password', 'profile'))
        return user_created

    def update(self, instance: User, validated_data):
        validated_data.pop('password', None)

        profile_data = validated_data.pop('profile', {})
        if profile_data:
            profile_serializer = self.fields['profile']
            profile_instance = instance.profile
            if profile_instance:
                profile_serializer.update(profile_instance, profile_data)

        return super().update(instance, validated_data)


class UserSerializer(BaseUserSerializer):
    pass


class UserClientCreationSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['username', 'password', 'profile']
        extra_kwargs = {
            **BaseUserSerializer.Meta.extra_kwargs,
            'user_type': {
                'read_only': True
            }
        }


class UserCreationSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['username', 'password', 'profile', 'user_type']
        extra_kwargs = {
            **BaseUserSerializer.Meta.extra_kwargs,
            'user_type': {
                'read_only': False
            }
        }


class UserEditionSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['username', 'profile']
