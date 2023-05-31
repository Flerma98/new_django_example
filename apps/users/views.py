from rest_framework import status, viewsets
from rest_framework.response import Response

from apps.users.models import User
from apps.users.serializers import UserSerializer
from apps.users.user_profile.serializers import UserProfileSerializer
from apps.users.values.user_type import UserType


class UserViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        profile_serializer = UserProfileSerializer(data=request.data.get('profile'))
        if not profile_serializer.is_valid():
            return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        profile_saved = profile_serializer.save()
        try:
            serializer.save(profile=profile_saved, user_type=UserType.CLIENT)
        except:
            profile_saved.delete()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        if instance.profile:
            instance.profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
