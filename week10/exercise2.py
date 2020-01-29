#!/usr/bin/env/python

#This is the serial data gatherer; will find info via netmiko and time the operation

import time
import threading
from my_devices import network_devices
from my_functions import ssh_command


if __name__ == "__main__":
    """
    Use "legacy" threading to send "show version" to each device and record the time.
    """
    start_time =  time.time()

    #A list for the threads to be collected in
    threads = []


    for device in network_devices:
        t = threading.Thread(target=ssh_command, args=(device, "show version"))
        threads.append(t)
        t.start()

    #In legacy threads, the join waits for each thread to complete then puts them all together
    for t in threads:
        t.join()

    end_time = time.time()

    print(f"Finished in {end_time - start_time} seconds")
