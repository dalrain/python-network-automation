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

    
    for device in results:
        print("-"*60)
        device_name = device["display_name"]
        location = device["site"]["name"]
        manufacturer = device["device_type"]["manufacturer"]["name"]
        status = device["status"]["label"]
        print(device_name)
        print("-"*10)
        print(f"Location: {location}")
        print(f"Vendor: {manufacturer}")
        print(f"Status: {status}")
        print("-"*60)

