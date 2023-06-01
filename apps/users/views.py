from drf_query_filter import fields
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from apps.users.models import User
from apps.users.permissions import IsAdmin, IsAdminOrIsTheOwner
from apps.users.serializers import UserSerializer
from apps.users.user_profile.forms import UserProfilePictureForm
from apps.users.values.user_type import UserType


class UserViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer

    ordering_fields = {
        'id': 'id',
        'user_type': 'user_type'
    }

    query_params = [
        fields.Field('user_type', 'user_type__icontains'),
        fields.Field('username', 'username__icontains'),
        fields.RangeDateField('date_time_created', 'date_time_created__date', equal=True),
    ]

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    def get_permissions(self):
        if self.action in ['create', 'list', 'retrieve', 'delete']:
            permission_classes = (IsAuthenticated, IsAdmin,)
        elif self.action in ['update', 'partial_update', 'upload_picture']:
            permission_classes = (IsAuthenticated, IsAdminOrIsTheOwner)
        elif self.action in ['my_user', 'update_my_picture']:
            permission_classes = (IsAuthenticated,)
        elif self.action in ['create_client']:
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAuthenticated,)

        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path=r'create_client')
    def create_client(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(user_type=UserType.CLIENT)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path=r'my_user')
    def my_user(self, request, **kwargs):
        instance = request.user
        instance.refresh_from_db()
        serializer = self.get_serializer(instance=instance)
        return Response(serializer.data)

    @action(detail=False, methods=['put'], url_path=r'upload_picture')
    def upload_picture(self, request, *args, **kwargs):
        user_instance: User = self.get_object()

        form = UserProfilePictureForm(request.data, request.FILES)
        if form.is_valid():
            user_instance.profile.profile_image = form.cleaned_data['profile_image']
            user_instance.profile.save()

        return Response(self.get_serializer(instance=user_instance).data)

    @action(detail=False, methods=['put'], url_path=r'update_my_picture')
    def update_my_picture(self, request, *args, **kwargs):
        user_authenticated: User = request.user

        form = UserProfilePictureForm(request.data, request.FILES)
        if form.is_valid():
            user_authenticated.profile.profile_image = form.cleaned_data['profile_image']
            user_authenticated.profile.save()

        instance = request.user
        instance.refresh_from_db()
        return Response(self.get_serializer(instance=instance).data)

    def destroy(self, request, *args, **kwargs):
        instance: User = self.get_object()
        profile = instance.profile
        self.perform_destroy(instance)
        if profile:
            profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
