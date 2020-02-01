#!/usr/bin/env/python

#This is the paralell process data gatherer; will find info via netmiko and time the operation

import time
from concurrent.futures import ProcessPoolExecutor, wait, as_completed
from my_devices import network_devices
from my_functions import ssh_command2


if __name__ == "__main__":
    """
    Use "concurrent futures" process-based threading to send "show version" to each device and record the time.
    Differs from the other approach in that wait can collect all the threads, and ssh2 is getting info back from the func rather than printing in the func
    """
    start_time =  time.time()
    max_threads = 5

    # Pre-create the thread pool we'll pull from, give it a max thread based on definition above
    with ProcessPoolExecutor(max_threads) as pool:

        #A list for the threads to be collected in
        futures = []

        #Set up a command list to be populated as the same size as the list of devices, specialized command per device type
        cmd_list = []

        for device in network_devices:
            if "junos" in device["device_type"]:
                cmd_list.append("show arp")
            else:
                cmd_list.append("show ip arp")
        #Instead of pool.submmit, we'll use pool.map, which will map a command to each device
        results = pool.map(ssh_command2, network_devices, cmd_list) 

        #In futures threads, the wait gathers each thread to complete then puts them all together
        #But this time, we won't wait, instead we'll gather as_completed and output immediately

        for result in results:
            print(f"Thread with ssh2 show arp or show ip arp returned {result}")

        end_time = time.time()

        print(f"Finished in {end_time - start_time} seconds")
