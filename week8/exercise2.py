#!/usr/bin/env/python

from jnpr_devices import srx2

from pprint import pprint

from jnpr.junos import Device
#This object will actually build a table when passed the device object above
from jnpr.junos.op.routes import RouteTable
#Same for this, but for ARP
from jnpr.junos.op.arp import ArpTable

def check_connected(device):
    if device.connected:
        print(f"The device known as {device.hostname} is connected")
    else:
        print(f"The device known as {device.hostname} didn't actually connect, killing script")
        sys.exit(1)

def gather_routes(device):
    #This will return a dict-like object, but not really a list/dict
    routes = RouteTable(device)
    routes.get()
    return routes

def gather_arp_table(device):
    #This will also return a dict-like object that can be list or dict-ified
    arp_table = ArpTable(device)
    arp_table.get()
    return arp_table

def print_output(dev, routes, arp):
    #Device needs to be an empty dict to start, that way insertions into it will be dict-like
    device = {}
    device["hostname"] = dev.hostname
    device["connected_port"] = dev.port
    device["connected_user"] = dev.user
    device["route_table"] = routes.items()
    device["arp_table"] = arp.items()
    pprint(device)

if __name__ == "__main__":
    device_object = Device(**srx2)
    device_object.open()

    routes = gather_routes(device_object)

    arp = gather_arp_table(device_object)

    print_output(device_object, routes, arp)

