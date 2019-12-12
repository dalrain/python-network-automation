#!/usr/bin/env/python

from lxml import etree

# The open needs b because the file specifies its own encoding

with open("show_version.xml", "rb") as f:
    show_version = etree.fromstring(f.read())

print("Print the default namespace")
print("Document default namespace is:\n {}".format(show_version.nsmap))

print("Extracting the proc_board_id element, star will give us a wildcard for the namespace, effectively ignoring it. Two slashes also search into the tree.")
print(show_version.find(".//{*}proc_board_id").text)
