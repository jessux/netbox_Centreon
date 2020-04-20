from extras.plugins import PluginTemplateExtension
from .models import CentreonObjectStatus
import json

class SiteCentreonObjectStatus(PluginTemplateExtension):
    model = 'ipam.ipaddress'

    def right_page(self):
        c = CentreonObjectStatus()
        list =  json.dumps(CentreonObjectStatus.objects)
        return self.render('netbox_Centreon/status.html', extra_context={
            'c': c,
        })

template_extensions = [SiteCentreonObjectStatus]