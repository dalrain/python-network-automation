#!/usr/bin/env/python
from pprint import pprint
import xmltodict

with open("show_security_zones.xml", "r") as f:
    show_security_zones = xmltodict.parse(f.read())


# Exercise 2a

print("Print the xmltodict object and its type")
pprint(show_security_zones)
print(type(show_security_zones))

# Exercise 2b

print("Print the names and an index number of each security zone")
zones = show_security_zones["zones-information"]["zones-security"]
# Enumerate creates a number to go along with the iterable objects we're returning, i.e. 0,1,2
for index, zone in enumerate(zones,1):
    print(f"Security zone {index}: {zone['zones-security-zonename']}")
