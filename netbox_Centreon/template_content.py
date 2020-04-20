from extras.plugins import PluginTemplateExtension
from .models import CentreonObjectStatus

class SiteCentreonObjectStatus(PluginTemplateExtension):
    model = 'ipam.ipaddress'

    def right_page(self):
        a=super()
        c = CentreonObjectStatus()
        return self.render('netbox_Centreon/status.html', extra_context={
            'c': c,
            'a': a
        })

template_extensions = [SiteCentreonObjectStatus]