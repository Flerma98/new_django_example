from django.utils.translation import gettext as _
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.users.models import User
from apps.users.permissions import IsAdmin
from apps.users.serializers import UserSerializer
from apps.users.user_profile.serializers import UserProfileSerializer
from apps.users.values.user_type import UserType


class UserViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'list', 'retrieve', 'delete', 'update', 'partial_update']:
            permission_classes = (IsAuthenticated, IsAdmin,)
        elif self.action in ['my_user']:
            # permission_classes = (AllowAny,)
            permission_classes = (IsAuthenticated,)
        else:
            permission_classes = (IsAuthenticated,)

        return [permission() for permission in permission_classes]

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

    @action(detail=False, methods=['get'], url_path=r'my_user')
    def my_user(self, request, **kwargs):
        try:
            user_authenticated = request.user
            instance = User.objects.get(pk=user_authenticated.id)
            serializer = self.get_serializer(instance=instance)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({
                'error': _('User not found')
            }, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        instance: User = self.get_object()
        self.perform_destroy(instance)
        if instance.profile:
            instance.profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
