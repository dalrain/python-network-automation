#!/usr/bin/env/python

from pprint import pprint
from my_devices import network_devices
from my_functions import open_napalm_connection, create_backup

if __name__ == "__main__":
    connections = []
    for device in network_devices:
        connection = open_napalm_connection(device)
        connections.append(connection)

    print("Printing the ARP table of all the devices")

    for connection in connections:
        pprint(connection.get_arp_table())

    print("Now print NTP peers if any")

    for connection in connections:
        try:
            pprint(connection.get_ntp_peers())
        except NotImplementedError:
            print("NTP peers not available on the platform {}".format(connection.platform))

    print("Make a backup of the running configurations")
    for connection in connections:
        create_backup(connection)
        connection.close()

