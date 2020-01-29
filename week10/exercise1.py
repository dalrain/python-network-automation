#!/usr/bin/env/python

#This is the serial data gatherer; will find info via netmiko and time the operation

import time
from netmiko import ConnectHandler
from my_devices import network_devices

def ssh_command(device, command):
    """Create an SSH session, execute the show command passed in, then return the results"""
    device = ConnectHandler(**device)
    output = device.send_command(command)
    device.disconnect()
    return output

if __name__ == "__main__":

    start_time =  time.time()

    for device in network_devices:
        output = ssh_command(device, "show version")
        print(output)

    end_time = time.time()

    print(f"Finished in {end_time - start_time} seconds")
