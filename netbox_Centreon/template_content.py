from extras import PluginTemplateExtension
from .models import CentreonObjectStatus
import requests
# from __init__ import config


class SiteCentreonObjectStatus(PluginTemplateExtension):
    model = 'dcim.devices'
    def right_page(self):
        c= {"imported":True,"state":False}
        return self.render('netbox_Centreon/status.html', extra_context={
            'c': c
        })

template_extensions = [SiteCentreonObjectStatus]
