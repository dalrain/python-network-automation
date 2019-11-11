#!/usr/bin/env/python

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

template_vars = {
    "vrfs" : {
        "blue" : {
            "rd" : "100:1",
             "ipv4_enabled" : True,
             "ipv6_enabled" : True,
        },
    }
}

template_file = "exercise3-4.j2"
template = env.get_template(template_file)
output = template.render(**template_vars)

print(output)
