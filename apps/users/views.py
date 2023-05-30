from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from apps.users.models import User
from apps.users.serializers import UserSerializer
from apps.users.user_profile.serializers import UserProfileSerializer
from apps.users.values.user_type import UserType


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


def get_item(pk):
    try:
        return User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise NotFound(_('User not found'))


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_user(request, pk):
    user = get_item(pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)
