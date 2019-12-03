import pyeapi

import os

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

from getpass import getpass
from my_func import load_devices_from_yaml

from pprint import pprint

device_dict = load_devices_from_yaml("all-aristas.yml")
device_password = getpass()

# Create a Jinja2 environment in order to require variables be set
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")
template_file = "loopback_intf.j2"

for item, device_detail in device_dict.items():
    device_detail["password"] = device_password

    jinja_vars = device_detail["data"]
    pprint(jinja_vars)

    #load the actual template
    template = env.get_template(template_file)

    #Start creating config, break out any extra whitespace then split lines into separate dicts
    cfg_lines = template.render(**jinja_vars)
    cfg_lines = cfg_lines.strip()
    cfg_lines = cfg_lines.splitlines()
    
    pprint(cfg_lines)

    # This takes transport, host, username, password, and port
    connection = pyeapi.client.connect(**device_detail)

    #This takes an existing connection and creates a Node instance
    device = pyeapi.client.Node(connection)

    #Now push the config
    device.config(cfg_lines)

    #And verify it

    output = device.enable("show ip interface brief")
    pprint(output)
