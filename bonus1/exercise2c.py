from pprint import pprint
import requests

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

BASE_URL = "https://netbox.lasthop.io/api"

if __name__ == "__main__":

    #This is supposed to use proper headers, in which we send that we're looking for a JSON response
    http_headers = {}
    http_headers["accept"] = "application/json; version=2.4;"
    response = requests.get(f"{BASE_URL}/dcim", headers=http_headers, verify=False)

    print(f"Response code: {response.status_code}")

    print("Response text was:")
    pprint(response.text)

    print("The child endpoints response in JSON was:")
    pprint(response.json())

    print("Finally, the response headers included:")
    pprint(dict(response.headers))
