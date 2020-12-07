from rest_framework.serializers import ModelSerializer
from netbox_Centreon.models import CentreonObjectStatus

class CentreonSerializer(ModelSerializer):

    class Meta:
        model = CentreonObjectStatus
        fields = ('name', 'imported', 'state')