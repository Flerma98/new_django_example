from rest_framework import routers

from apps.restaurants.views import RestaurantViewSet

router = routers.SimpleRouter()
router.register(r'', RestaurantViewSet, 'users')
urlpatterns = router.urls
