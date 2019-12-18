#!/usr/bin/env/python

from jnpr.junos import Device

from jnpr.junos.utils.config import Config

from jnpr_devices import srx2

from exercise2 import check_connected, gather_routes

from pprint import pprint

CONFIG_FILE = "static_routes.conf"

def config_from_file(path, device, merge=True):
    config_object = Config(device)
    config_object.lock()
    #Go ahead and actually supply the config to the new config object
    config_object.load(path=path, format="text", merge=merge)
    #If a change is actually made, go ahead and commit it blindly
    if config_object.diff() is not None:
        config_object.commit()
    config_object.unlock()

def config_set_from_file(path, device, merge=True):
    config_object = Config(device)
    config_object.lock()
    #Go ahead and actually supply the config to the new config object
    config_object.load(path=path, format="set", merge=merge)
    #If a change is actually made, go ahead and commit it blindly
    if config_object.diff() is not None:
        config_object.commit()
    config_object.unlock()


def compare_routes(original_routes, updated_routes):
    print("Checking for differences between routing lists")
    new_routes = []

    for route in updated_routes.keys():
        if route not in original_routes.keys():
            new_routes.append(route)
    return new_routes

if __name__ == "__main__":

    device = Device(**srx2)
    device.open()

    check_connected(device)

    routes = gather_routes(device)

    print("The original routes:")
    pprint(list(routes))

    #Make the actual static route changes from the .conf file at the top
    config_from_file(CONFIG_FILE, device)

    print("Updated routes in all:")
    updated_routes = gather_routes(device)

    pprint(list(updated_routes))

    pprint(compare_routes(routes, updated_routes))

    #Finally, delete the static routes we added

    print("Now removing all the hard work we did")
    config_set_from_file("del_static_routes.set", device)
