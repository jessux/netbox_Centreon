from extras.plugins import PluginTemplateExtension
from .models import CentreonObjectStatus

class SiteCentreonObjectStatus(PluginTemplateExtension):
    model = 'ipam.ipaddress'

    def right_page(self):
        return self.render('netbox_Centreon/templates/status.html', extra_context={
            'imported': CentreonObjectStatus.imported,
            'state' : CentreonObjectStatus.state
        })

template_extensions = [SiteCentreonObjectStatus]