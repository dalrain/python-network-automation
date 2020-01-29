#!/usr/bin/env/python


from my_functions import open_napalm_connection
from my_devices import network_devices

if __name__ == "__main__":

    connection_handles = []

    for device in network_devices:
        connection = open_napalm_connection(device)
        connection_handles.append(connection)

    for connection in connection_handles:

        connection.load_merge_candidate(filename="{}-loopbacks".format(connection.hostname))
        print("Showing a diff of the proposed changes for device {}".format(connection.hostname))
        diff = connection.compare_config()

        print(diff) 

        #If there is a diff (meaning that there are changes) let's actually make them

        if diff:
            connection.commit_config()

        print("Now showing the diff after committing the config for device {}".format(connection.hostname))

        print(connection.compare_config())

        #Clean up the connections as we hit the end of the device loop
        connection.close()
