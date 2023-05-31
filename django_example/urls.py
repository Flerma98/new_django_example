from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurants/', include('apps.restaurants.urls')),
    path('foods/', include('apps.foods.urls')),
    path('users/', include('apps.users.urls')),
    path('auth/', include('apps.auth_users.urls'))
]
