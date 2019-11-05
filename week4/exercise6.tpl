Value Filldown LOCAL_AS (\d+)
Value Filldown BGP_ROUTER_ID ([0-9\.]+)
Value NEIGHBOR (\S+)
Value REMOTE_AS (\d+)
Value UP_DOWN (\S+)
Value STATE_PFXRECEIVED ((Active|Idle|\d+))

Start
  ^BGP router identifier ${BGP_ROUTER_ID}, local AS number ${LOCAL_AS}\s*$$
  ^Neighbor.*State.PfxRcd$$ -> Table

Table
  ^${NEIGHBOR}\s+4\s+${REMOTE_AS}\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+${UP_DOWN}\s+${STATE_PFXRECEIVED} -> Record

EOF

