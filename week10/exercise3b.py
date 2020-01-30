#!/usr/bin/env/python

#This is the serial data gatherer; will find info via netmiko and time the operation

import time
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
from my_devices import network_devices
from my_functions import ssh_command2


if __name__ == "__main__":
    """
    Use "concurrent futures" threading to send "show version" to each device and record the time.
    Differs from the other approach in that wait can collect all the threads, and ssh2 is getting info back from the func rather than printing in the func
    """
    start_time =  time.time()
    max_threads = 5

    # Pre-create the thread pool we'll pull from, give it a max thread based on definition above
    pool = ThreadPoolExecutor(max_threads)

    #A list for the threads to be collected in
    futures = []


    for device in network_devices:
        futures.append(pool.submit(ssh_command2, device, "show version")) 

    #In futures threads, the wait gathers each thread to complete then puts them all together
    #But this time, we won't wait, instead we'll gather as_completed and output immediately
    #wait(futures)

    for future in as_completed(futures):
        print(f"Thread with ssh2 show version returned {future.result()}")

    end_time = time.time()

    print(f"Finished in {end_time - start_time} seconds")
