import requests
import sys

LIST_ACTION = "LIST"
ADD_ACTION = "ADD"
REMOVE_ACTION = "REMOVE"

actions = [LIST_ACTION, ADD_ACTION, REMOVE_ACTION]
ADDRESS_MAPPING = "ADDRESSMAPPINGS"

action = sys.argv[1]
mapping = sys.argv[2]
host = sys.argv[3]
port = sys.argv[4]

if action == LIST_ACTION and mapping == ADDRESS_MAPPING:
    # do something
    # get path and use requests lib to send to JAMES
    print("1")

if action == ADD_ACTION and mapping == ADDRESS_MAPPING:
    # do something
    print("2")

if action == REMOVE_ACTION and mapping == ADDRESS_MAPPING:
    # do something
    print("3")

if action not in actions:
    if mapping == ADDRESS_MAPPING:
        print("Invalid request action on %.") % (ADDRESS_MAPPING)
    else:
        print("Invalid request action and mapping.")