from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include
from django.urls import path

from django_example import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurants/', include('apps.restaurants.urls')),
    path('foods/', include('apps.foods.urls')),
    path('users/', include('apps.users.urls')),
    path('auth/', include('apps.auth_users.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
