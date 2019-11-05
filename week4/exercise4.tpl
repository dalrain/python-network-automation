Value MAC_ADDR ([0-9a-f:]+)
Value IP_ADDR ([0-9\.]+)
Value NAME (\S+)
Value INTERFACE (\S+)

Start
  ^MAC Address.*Flags.*$$ -> TabularData

TabularData
  ^${MAC_ADDR}\s+${IP_ADDR}\s+${NAME}\s+${INTERFACE}\s+ -> Record
