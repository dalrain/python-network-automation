from pprint import pprint
import requests
import os

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

BASE_URL = "https://netbox.lasthop.io/api"

if __name__ == "__main__":

    token = os.environ["NETBOX_TOKEN"]

    #This is supposed to use proper headers, in which we send that we're looking for a JSON response
    http_headers = {}
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"
    response = requests.get(f"{BASE_URL}/dcim/devices", headers=http_headers, verify=False)

    results = response.json()["results"]

    devices = []
    for device in results:
        devices.append(device["display_name"])

    pprint(devices)
