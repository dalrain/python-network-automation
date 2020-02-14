import pytest
from getpass import getpass
from netmiko import ConnectHandler

@pytest.fixture(scope="module")
def netmiko_connect(request):
    """Creates a connection object to the arista lab device and returns the handle"""
    password = getpass()
    arista1 = {
        "device_type" : "arista_eos",
        "host": "arista1.lasthop.io",
        "username": "pyclass",
        "password": password,
    }
    connection_handle = ConnectHandler(**arista1)

    def fin():
        connection_handle.disconnect()

    request.addfinalizer(fin)
    return connection_handle
