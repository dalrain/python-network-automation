#!/usr/bin/env/python

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

template_vars = {
    "device" : {
        "nxos1" : {
            "interfaces" : {
                "Ethernet1/1" : {
                    "ip_address" : "10.100.1.1",
                    "netmask" : 24,
                }
            },
            "local_as" : 22,
            "peer_ip" : "10.1.100.2"
        },
        "nxos2" : { 
            "interfaces" : { 
                "Ethernet1/1" : { 
                    "ip_address" : "10.100.1.2",
                    "netmask" : 24, 
                }   
            },
            "local_as" : 22,
            "peer_ip" : "10.1.100.1"
        },
    }
}

template_file = "exercise2b.j2"
template = env.get_template(template_file)
output = template.render(**template_vars)

print(output)
