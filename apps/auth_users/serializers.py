from knox.settings import knox_settings
from rest_framework import serializers


class LoginUserSerializerSchema(serializers.Serializer):
    expiry = serializers.DateTimeField(
        read_only=True,
        format=knox_settings.EXPIRY_DATETIME_FORMAT
    )
    token = serializers.CharField(
        read_only=True,
        max_length=knox_settings.AUTH_TOKEN_CHARACTER_LENGTH
    )
    user = knox_settings.USER_SERIALIZER(read_only=True)
