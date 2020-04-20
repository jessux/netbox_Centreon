from extras.plugins import PluginTemplateExtension
from .models import CentreonObjectStatus

class SiteCentreonObjectStatus(PluginTemplateExtension):
    model = 'ipam.ipaddress'

    def right_page(self):
        c = CentreonObjectStatus()
        return self.render('netbox_Centreon/status.html', extra_context={
            'c': CentreonObjectStatus.objects,
        })

template_extensions = [SiteCentreonObjectStatus]