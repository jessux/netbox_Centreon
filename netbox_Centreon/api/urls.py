from rest_framework import routers
from .views import CentreonViewSet

router = routers.DefaultRouter()
router.register('Centreon', CentreonViewSet)
urlpatterns = router.urls