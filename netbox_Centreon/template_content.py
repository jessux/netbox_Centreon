from extras.plugins import PluginTemplateExtension
from .models import CentreonObjectStatus

class SiteCentreonCount(PluginTemplateExtension):
    model = 'dcim.site'

    def right_page(self):
        return self.render('netbox_Centreon/status.html', extra_context={
            'CentreonObjectStatus': CentreonObjectStatus.objects.all(),
        })

template_extensions = [SiteCentreonCount]