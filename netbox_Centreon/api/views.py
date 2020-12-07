from rest_framework.viewsets import ModelViewSet
from netbox_Centreon.models import CentreonObjectStatus
from .serializers import CentreonSerializer

class CentreonViewSet(ModelViewSet):
    queryset = CentreonObjectStatus.objects.all()
    serializer_class = CentreonSerializer