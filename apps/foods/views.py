from drf_query_filter import fields
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from apps.foods.models import Food
from apps.foods.serializers import FoodSerializer, FoodCreationSerializer, FoodEditionSerializer
from apps.users.permissions import IsAdminOrIsTheOwner


# Create your views here.
class FoodViewSet(viewsets.ModelViewSet):
    model = Food
    queryset = Food.objects.all()
    authentication_classes = [TokenAuthentication]

    def get_serializer_class(self):
        if self.action == 'create':
            return FoodCreationSerializer
        if self.action in ['update', 'partial_update']:
            return FoodEditionSerializer
        return FoodSerializer

    filter_backends = [OrderingFilter]
    ordering_fields = {
        'id': 'id'
    }

    query_params = [
        fields.Field('name', 'name__icontains'),
        fields.Field('calories', 'calories__icontains'),
        fields.Field('restaurant', 'restaurant.name__icontains')
    ]

    def get_permissions(self):
        if self.action in ['create', 'delete', 'update', 'partial_update']:
            permission_classes = (IsAuthenticated, IsAdminOrIsTheOwner,)
        elif self.action in ['list', 'retrieve']:
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAuthenticated,)

        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = FoodCreationSerializer(data=request.data)
        if not serializer.is_valid():
            serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
