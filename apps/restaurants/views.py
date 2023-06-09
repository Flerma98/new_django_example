from rest_framework import viewsets
from drf_query_filter import fields
from rest_framework.filters import OrderingFilter

from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    model = Restaurant
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()

    filter_backends = [OrderingFilter]
    ordering_fields = {
        'id': 'id'
    }

    query_params = [
        fields.Field('name', 'name__icontains')
    ]
