from rest_framework.serializers import ModelSerializer
from netbox_Centreon.models import CentreonObjectStatus

class CentreonObjectStatusSerializer(ModelSerializer):

    class Meta:
        model = CentreonObjectStatus
        fields = ('id', 'name', 'imported','state')