Value DEVID (\S+)
Value LOCAL_INT (Eth[0-9/]+)
Value CAPABILITY ((BR))
Value PORT_ID (Eth[0-9/]+)

Start
  ^Device ID.*Port ID -> LLDPTable

LLDPTable
  ^${DEVID}\s+${LOCAL_INT}\s+\d+\s+${CAPABILITY}\s+${PORT_ID} -> Record
