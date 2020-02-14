#!/usr/bin/env/python

from getpass import getpass
from netmiko import ConnectHandler

def netmiko_connect():
    """Creates a connection object to the arista lab device and returns the handle"""
    password = getpass()
    arista1 = {
        "device_type" : "arista_eos",
        "host": "arista1.lasthop.io",
        "username": "pyclass",
        "password": password,
    }
    return ConnectHandler(**arista1)

def test_prompt():
    """Look for a command prompt, make sure the connection was successful"""
    connection_handle = netmiko_connect()
    assert connection_handle.find_prompt() == "arista1#"

def test_show_version():
    """Get show version from the device"""
    connection_handle = netmiko_connect()
    assert "4.20.10M" in connection_handle.send_command("show version")

