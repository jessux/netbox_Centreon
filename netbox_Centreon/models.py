from django.db import models
import requests

class CentreonObjectStatus(models.Model):
    name = models.CharField(max_length=16)
    imported = models.BooleanField(default=False)
    state= models.BooleanField(default=False)

    def getHosts(self):
        payload = {'username': 'gabriel','password': '5UtGqvY5'}
        response = requests.request("POST", "http://192.168.1.201/centreon/api/index.php?action=authenticate", data=payload)
        if response.status_code == 200:
            url = "http://192.168.1.201/centreon/api/index.php?action=action&object=centreon_clapi"

            payload = "{\r\n  \"action\": \"show\",\r\n  \"object\": \"host\"\r\n}"
            headers = {
                'Content-Type': 'application/json',
                'centreon-auth-token': response.json()["authToken"],
                'Content-Type': 'text/plain'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            return response.json()

        else:
            return ""

    def __str__(self):
        return self.name

    def isimported(self):
        return self.imported

    def isactivated(self):
        return self.state