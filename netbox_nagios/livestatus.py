import json
import socket
import requests

TIMEOUT = 3  # seconds
BUFFER_SIZE = 4096  # bytes


def hoststatus(hostname: str, livestatus_host: str, livestatus_port: int):
    payload = {'username': 'admin','password': 'centreon'}
    response = requests.request("POST", "http://digsflrp1k.dig.intra.groupama.fr/centreon/api/index.php?action=authenticate", data=payload)
    if response.status_code == 200:
        url = "http://digsflrp1k/centreon/api/index.php?object=centreon_realtime_hosts&action=list"
        headers = {
            'Content-Type': 'application/json',
            'centreon-auth-token': response.json()["authToken"],
        }
        response = requests.request("GET", url, headers=headers)
        data=response.json()
        if not data or len(data) <= 1:
                return None
        return data
    return {}
