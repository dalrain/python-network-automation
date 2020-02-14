#!/usr/bin/env/python

import pytest
from getpass import getpass
from netmiko import ConnectHandler

@pytest.fixture(scope="module")
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

def test_prompt(netmiko_connect):
    """Look for a command prompt, make sure the connection was successful"""
    assert netmiko_connect.find_prompt() == "arista1#"

def test_show_version(netmiko_connect):
    """Get show version from the device"""
    assert "4.20.10M" in netmiko_connect.send_command("show version")

