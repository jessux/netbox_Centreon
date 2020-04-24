from extras.plugins import PluginTemplateExtension
from .models import CentreonObjectStatus
import requests
from __init__ import config


class SiteCentreonObjectStatus(PluginTemplateExtension):
    model = 'ipam.ipaddress'
    centreon_url = getattr(config.required_settings, 'centreon_url', None)

    def getAllHosts(self):
        payload = {'username': 'gabriel','password': '5UtGqvY5'}
        response = requests.request("POST", "http://"+self.centreon_url+"/centreon/api/index.php?action=authenticate", data=payload)
        if response.status_code == 200:
            url = "http://"+self.centreon_url+"/centreon/api/index.php?action=action&object=centreon_clapi"

            payload = "{\r\n  \"action\": \"show\",\r\n  \"object\": \"host\"\r\n}"
            headers = {
                'Content-Type': 'application/json',
                'centreon-auth-token': response.json()["authToken"],
                'Content-Type': 'text/plain'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            return response.text.encode("utf-8")

        else:
            return ""

    def getHostsByName(self,name):
        payload = {'username': 'gabriel','password': '5UtGqvY5'}
        response = requests.request("POST", "http://"+self.centreon_url+"/centreon/api/index.php?action=authenticate", data=payload)
        if response.status_code == 200:
            url = "http://"+self.centreon_url+"/centreon/api/index.php?action=action&object=centreon_clapi"

            payload = "{\r\n  \"action\": \"show\",\r\n  \"object\": \"host\",\r\n  \"values\": \""+name+"\"\r\n}"
            headers = {
                'Content-Type': 'application/json',
                'centreon-auth-token': response.json()["authToken"],
                'Content-Type': 'text/plain'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            return response.json()

        else:
            return ""

    def updateStatus(self,object):
        return

    def buttons(self):
        print(self.centreon_url)
        print(config.required_settings)
        return '<a href="/api/plugins/centreon/CentreonObjectStatus/" class="btn"><span class="fa fa-plus" aria-hidden="true"></span> Refresh status</a>'

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
