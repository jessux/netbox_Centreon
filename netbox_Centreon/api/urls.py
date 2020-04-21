from rest_framework import routers
from .views import CentreonObjectStatusViewSet

router = routers.DefaultRouter()
router.register('CentreonObjectStatus', CentreonObjectStatusViewSet)
urlpatterns = router.urls