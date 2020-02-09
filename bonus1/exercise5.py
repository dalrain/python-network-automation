from pprint import pprint
import requests
import os
import json

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

BASE_URL = "https://netbox.lasthop.io/api/"
#This will take the addr ID, used for the URL to access the IP object directly
ADDRESS_ID = input("Enter Address ID that was created in exercise4: ")

if __name__ == "__main__":

    token = os.environ["NETBOX_TOKEN"]

    #This is supposed to use proper headers, in which we send that we're looking for a JSON response
    #For a POST, to put data on the server, we also need "Content-Type" to tell the server what we're sending
    http_headers = {}
    http_headers["Content-Type"] = "application/json; version=2.4;"
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"

    #Data to send the to server, i.e. a dict with the IP addr
    data = {"address": "192.0.2.42/32", "description": "Rest-API testing"}

    #The PUT method will alter existing data, and we form the URL using the address ID from the earlier create operations
    response = requests.put(
        f"{BASE_URL}ipam/ip-addresses/{ADDRESS_ID}/",
        headers=http_headers,
        verify=False,
        data=json.dumps(data),
    )

    print("Sending the POST data to create the IP addr object:")
    print(f"It returned response code {response.status_code}")
    print("Also returned JSON...")
    pprint(response.json())


    

