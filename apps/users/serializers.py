from rest_framework import serializers
from .models import User
from .user_profile.serializers import UserProfileSerializer


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = '__all__'
        write_only_fields = ['password'],
        read_only_fields = ['user_type', 'date_time_created']
