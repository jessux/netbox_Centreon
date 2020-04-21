from extras.plugins import PluginTemplateExtension
from .models import CentreonObjectStatus

class SiteCentreonObjectStatus(PluginTemplateExtension):
    model = 'ipam.ipaddress'

    def right_page(self):
        c = CentreonObjectStatus()
        for i in CentreonObjectStatus.__dict__.items():
            if c.name == i.name:
                c.setStatus()
        return self.render('netbox_Centreon/status.html', extra_context={
            'c': c,
        })

template_extensions = [SiteCentreonObjectStatus]