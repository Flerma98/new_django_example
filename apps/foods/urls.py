from django.urls import path

from .views import FoodsFreeView, FoodsSpecificView

urlpatterns = [
    path('', FoodsFreeView.as_view(), name='food-free'),
    path('<int:pk>/', FoodsSpecificView.as_view(), name='food-detail')
]
