#!/usr/bin/env/python

from lxml import etree

with open("show_security_zones.xml", "r") as f:
    show_security_zones = etree.fromstring(f.read())

# exercise 4a

print("Find tag of the first zones-security element")
print(show_security_zones.find("./zones-security").tag)

print("Find the tag of all the child elements in zones-security")
for child in show_security_zones.find("./zones-security").getchildren():
    print(child.tag)

# exercise 4b

print("Use the find() method to find the first instance of zones-security-zonename even in children then print the text in the element")
print(show_security_zones.find(".//zones-security-zonename").text)

# exercise 4c

print("Use the findall() method to find all zones-security, then print out the zone name text (look inside children, grab the text of a specific element zones-security-zonename")
for zone in show_security_zones.findall(".//zones-security"):
    print(zone.find(".//zones-security-zonename").text)
