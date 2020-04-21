from extras.plugins import PluginTemplateExtension
from .models import CentreonObjectStatus

class SiteCentreonObjectStatus(PluginTemplateExtension):
    model = 'ipam.ipaddress'

    def right_page(self):
        c = CentreonObjectStatus()
        obj = str(self.context['object']).split("/")[0] if '/' in str(self.context['object']) else str(self.context['object'])
        for i in CentreonObjectStatus.objects.all():
            if obj == i.name:
                c=i
        return self.render('netbox_Centreon/status.html', extra_context={
            'c': c,
        })

template_extensions = [SiteCentreonObjectStatus]