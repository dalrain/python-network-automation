#!/usr/bin/env/python

import re
from pprint import pprint

arp_entries = """
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""

arp_entries = arp_entries.strip()
arp_entries = arp_entries.splitlines()

result_list = []

for item in arp_entries:
    if re.search(r"^Protocol.*Interface", item):
        continue
    _, ip_address, _, mac_address, _, interface = item.split()
    result_list.append({"mac_addr":mac_address, "ip_addr":ip_address, "interface":interface})

pprint(result_list) 
