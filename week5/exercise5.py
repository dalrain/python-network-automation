#!/usr/bin/env/python

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

template_vars = {
    "ntp_servers" : [
        "130.126.24.24","152.2.21.1", 
    ],
    "clock_settings" : { 
         "timezone" : "PST",
         "timezone_offset" : -8,
         "timezone_dst" : "PDT",
    }
}

template_file = "cisco3_config.j2"
template = env.get_template(template_file)
output = template.render(**template_vars)

print(output)
