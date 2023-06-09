from rest_framework import viewsets
from drf_query_filter import fields

from knox.auth import TokenAuthentication as KnoxTokenAuth
from rest_framework.authentication import TokenAuthentication as RestFrameworkTokenAuth

from rest_framework.filters import OrderingFilter

from .models import Restaurant
from .serializers import RestaurantSerializer, RestaurantCreationSerializer, RestaurantEditionSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    model = Restaurant
    queryset = Restaurant.objects.all()
    authentication_classes = [KnoxTokenAuth, RestFrameworkTokenAuth]

    def get_serializer_class(self):
        if self.action == 'create':
            return RestaurantCreationSerializer
        if self.action in ['update', 'partial_update']:
            return RestaurantEditionSerializer
        return RestaurantSerializer

    filter_backends = [OrderingFilter]
    ordering_fields = {
        'id': 'id'
    }

    query_params = [
        fields.Field('name', 'name__icontains')
    ]
