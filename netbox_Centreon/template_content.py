from extras.plugins import PluginTemplateExtension
from .models import CentreonObjectStatus

class SiteCentreonObjectStatus(PluginTemplateExtension):
    model = 'ipam.ipaddress'

    def right_page(self):
        c = CentreonObjectStatus()
        for i in CentreonObjectStatus.objects.all():
            if str(self.context['object']) == i.name:
                c.setStatus(i)
        return self.render('netbox_Centreon/status.html', extra_context={
            'c': c,
            'context': self.context
        })

template_extensions = [SiteCentreonObjectStatus]