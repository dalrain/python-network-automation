#!/usr/bin/env/python

from lxml import etree

with open("show_security_zones.xml", "r") as f:
    show_security_zones = etree.fromstring(f.read())

# Exercise 1a

print("This is the xml variable and its type")
print(show_security_zones)
print(type(show_security_zones))

# Exercise 1b

print("Print the entire XML tree")
print(etree.tostring(show_security_zones).decode())

# Exercise 1c

print("Print the root element's tag")
print(show_security_zones.tag)
print("And the number of direct children of the root")
print(len(show_security_zones))

# Exercise 1d

print("Obtain first child with index")
print(show_security_zones[0].tag)
print("Obtain first child with getchildren()")
print(show_security_zones.getchildren()[0].tag)

# Exercise 1e

print("Assign trust_zone to contain the first element of the zones")
trust_zone = show_security_zones[0]
print("security zone:" + trust_zone[0].text)

# Exercise 1f

print("Iterate through children of trust zone and print tag and text")
for child in trust_zone:
    print(child.tag + " : " + child.text)
