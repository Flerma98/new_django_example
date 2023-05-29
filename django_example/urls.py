from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurants/', include('restaurants.urls')),
    path('foods/', include('foods.urls'))
]
