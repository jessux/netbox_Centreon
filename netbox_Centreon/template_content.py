from extras.plugins import PluginTemplateExtension
from .models import CentreonObjectStatus

class SiteCentreonObjectStatus(PluginTemplateExtension):
    model = 'ipam.ipaddress'

    def right_page(self):
        return self.render('netbox_Centreon/status.html', extra_context={
            'imported': CentreonObjectStatus.isimported(),
            'state' : CentreonObjectStatus.isactivated()
        })

template_extensions = [SiteCentreonObjectStatus]