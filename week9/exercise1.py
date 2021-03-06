#!/usr/bin/env/python

from napalm import get_network_driver
from pprint import pprint
from my_devices import network_devices


#This takes a single device and returns a connection handle that can be manipulated as desired
def open_napalm_connection(device):
    """Open the connection and return a network object"""
    #Create a copy of the device that was passed in so that we can safely pop the copy instead of potentially harming the original device def
    device = device.copy()
    #Pop the platform, but we'll need it as part of the device connection driver idenfification
    platform = device.pop("platform")
    driver = get_network_driver(platform)
    connection_handle = driver(**device)
    connection_handle.open()
    return connection_handle


if __name__ == "__main__":
    connections = []
    for device in network_devices:
        connection = open_napalm_connection(device)
        connections.append(connection)

    print("Print the facts for all the devices")

    for connection in connections:
        print(connection)
        pprint("{} facts".format(connection.platform))
        print(connection.get_facts())
        connection.close()

    print()
