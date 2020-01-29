#!/usr/bin/env/python

from my_functions import open_napalm_connection, create_checkpoint

from my_devices import nxos1

#This program will do a full configuration replace on the nxos1 device, changing the state of the device all at once

#This is needed just to get the error to handle because the device is using an unsigned certificate
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

NXOS_REPLACE_CANDIDATE_FILE = "nxos1_replacement_cfg"

if __name__ == "__main__":
    connection_handle = open_napalm_connection(nxos1)

    # Checkpoint the currently existing config so that we can roll back

    create_checkpoint(connection_handle)

    connection_handle.load_replace_candidate(NXOS_REPLACE_CANDIDATE_FILE)

    print("Replacement config staged, diff between existing and new config follows for {}".format(connection_handle.hostname))

    print(connection_handle.compare_config())

    #Don't actually apply any changes(!)

    print("Discarding the config changes for {}".format(connection_handle.hostname))

    connection_handle.discard_config()

    print("Diff of changes after discarding the proposed changes (should be none) for {}".format(connection_handle.hostname))

    print(connection_handle.compare_config())

    connection_handle.close()
