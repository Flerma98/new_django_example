from rest_framework import serializers

from apps.users.validators import (
    UniqueUsernameValidator, PasswordStrengthValidator,
)
from .models import User
from .user_profile.serializers import UserProfileSerializer


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

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
            'user_type': {
                'read_only': True
            },
            'date_time_created': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        model = self.Meta.model
        normal_password = validated_data.pop('password')
        user_created = model.objects.create(**validated_data)
        user_created.set_password(normal_password)
        user_created.save()
        return user_created
