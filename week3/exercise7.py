#!/usr/bin/env/python

from pprint import pprint
from ciscoconfparse import CiscoConfParse

neighbors_string = """
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
"""

parse_object = CiscoConfParse(neighbors_string.splitlines())

bgp_peers = []

peer_object = parse_object.find_objects_w_parents(
    parentspec=r"router bgp", childspec=r"neighbor"
)

for peer in peer_object:
    _, peer_ip = peer.text.split()
    for child in peer.children:
        if "remote-as" in child.text:
            _, remote_as = child.text.split()
    bgp_peers.append((peer_ip, remote_as))

print()
print("BGP peers are: ")
pprint(bgp_peers)

