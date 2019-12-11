#!/usr/bin/env/python

import xmltodict

def read_xml(filename):
    with open(filename, "r") as f:
        return xmltodict.parse(f.read())

def read_xml_forcelist(filename, force_list=None):
    # Set the default to something reasonable if we didn't get an argument
    if force_list is None:
        force_list = {}
    with open(filename, "r") as f:
        return xmltodict.parse(f.read(), force_list=force_list)

show_security_zones = read_xml("show_security_zones.xml")

show_security_zones_single = read_xml("show_security_zones_single_trust.xml")

print("Here is the data type of the zones-security when multi-entries are present")
print(type(show_security_zones["zones-information"]["zones-security"]))

print("Here is the type when a single entry was present")
print(type(show_security_zones_single["zones-information"]["zones-security"]))

print("Finally, show the type when we force a list even on single entries")

show_security_zones_single = read_xml_forcelist("show_security_zones_single_trust.xml", force_list={"zones-security": True})

print(type(show_security_zones_single["zones-information"]["zones-security"]))


