from django.core.exceptions import BadRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.users.serializers import UserSerializer
from apps.users.user_profile.serializers import UserProfileSerializer
from apps.users.values import user_type
from apps.users.values.user_type import UserType
from django.utils.translation import gettext_lazy as _


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    profile_serializer = UserProfileSerializer(data=request.data.get('profile'))
    if not profile_serializer.is_valid():
        return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer.save(profile=profile_serializer.save(), user_type=UserType.CLIENT)
    return Response(serializer.data)
