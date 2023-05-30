from django.urls import path

from . import views

urlpatterns = [
    path('create_client/', views.create_user, name='create_user'),
    path('', views.get_users, name='get_users'),
    path('<int:pk>/', views.get_user, name='get_user')
]
