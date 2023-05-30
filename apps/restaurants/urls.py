from django.urls import path
from .views import RestaurantList, RestaurantDetail

urlpatterns = [
    path('', RestaurantList.as_view(), name='restaurant-list'),
    path('<int:pk>/', RestaurantDetail.as_view(), name='restaurant-detail')
]
