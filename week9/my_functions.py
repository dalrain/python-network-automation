from napalm import get_network_driver


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

def create_backup(connection):
    """This function uses a napalm config getter and saves a text file with the full output"""
    backup = connection.get_config()
    filename = f"{connection.hostname}-running-config.log"

    with open(filename, "w") as file_handle:
        # "running" is the key to reach into the returned get_config output, which may have multiple configs returned
        file_handle.write(backup["running"])

def create_checkpoint(connection):
    """This function pulls the current checkpoint if available and writes it as a text file to disk"""
    if "nxos" in connection.platform:
        filename = f"{connection.hostname}-checkpoint-config.log"
        backup = connection._get_checkpoint_file()

        with open(filename, "w") as f:
            f.write(backup)

    else:
        raise ValueError("Saving a checkpoint requires device to be NX-OS")
