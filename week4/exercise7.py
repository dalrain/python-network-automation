#!/usr/bin/env/python

from pprint import pprint
import textfsm

template_to_load = "exercise2.tpl"

textfsm_template = open(template_to_load)

with open("show_interface_status.txt") as handle:
    text_to_parse = handle.read()

# Give the textfsm object a file handle directly

fsm_table = textfsm.TextFSM(textfsm_template)

# This is a string, as read in by read()
data = fsm_table.ParseText(text_to_parse)
textfsm_template.close()

# This returns the top level "variables" from the template
table_keys = fsm_table.header
final_result = []

# Data is a Parse object that brought together the table with a template and the raw text to parse, so it contains an item per successful parse
for fsm_list in data:
    #This puts together each key along with the items from the list, so for EACH entry we'll have a consistent key into it, matched with the actual parsed data
    fsm_dict = dict(zip(table_keys, fsm_list))
    #A single dict is made each run, so tag that onto the end of the final result
    final_result.append(fsm_dict)

print()
pprint(final_result)
print()
