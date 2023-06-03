from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include
from django.urls import path

from django_example import settings
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('restaurants/', include('apps.restaurants.urls')),
                  path('foods/', include('apps.foods.urls')),
                  path('users/', include('apps.users.urls')),
                  path('auth/', include('apps.auth_users.urls')),
                  # ...
                  path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
                  path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
                  path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
                  # ...
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
