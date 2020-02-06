from pprint import pprint
import requests

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if __name__ == "__main__":
    response = requests.get("https://netbox.lasthop.io/api", verify=False)

    print(f"Response code: {response.status_code}")

    print("Response text was:")
    pprint(response.text)

    print("The response in JSON was:")
    pprint(response.json())

    print("Finally, the response headers included:")
    pprint(dict(response.headers))
