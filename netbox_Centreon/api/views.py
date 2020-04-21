from rest_framework.viewsets import ModelViewSet
from netbox_Centreon.models import CentreonObjectStatus
from .serializers import CentreonObjectStatusSerializer

class CentreonObjectStatusViewSet(ModelViewSet):
    queryset = CentreonObjectStatus.objects.all()
    serializer_class = CentreonObjectStatusSerializer