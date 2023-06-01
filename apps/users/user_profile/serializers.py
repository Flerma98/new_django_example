from rest_framework import serializers

from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

    @staticmethod
    def delete(instance: UserProfile):
        instance.delete_picture()
        instance.delete()
