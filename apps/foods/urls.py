from rest_framework import routers

from apps.foods.views import FoodViewSet

router = routers.SimpleRouter()
router.register(r'', FoodViewSet, 'users')
urlpatterns = router.urls
