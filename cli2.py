import sys
import requests as req
import json

BASE_PATH = "http://127.0.0.1:8000/"

action  = sys.argv[1].lower()

def print_json(obj):
    parsed = json.loads(obj.text)
    print(json.dumps(parsed, indent=4, sort_keys=True))

def list_all_user_mappings():
    res = req.get(BASE_PATH + "mappings")
    print_json(res)

def list_user_mappings(source):
    res = req.get(BASE_PATH + "mappings/user/" + source)
    print_json(res)

def add_address_mapping(source, destination):
    res = req.post(BASE_PATH + "mappings/address/" + source + "/targets/" + destination)

    if res.status_code == 204:
        print(destination + " is successfully added to " + source)
    elif res.status_code == 400:
        print("Invalid parameters or input domain is not added")
    else:
        print("Internal server error!")

def remove_address_mapping(source, destination): 
    res = req.delete(BASE_PATH + "mappings/address/" + source + "/targets/" + destination)
    if res.status_code == 204:
        print(destionation + " is successfully removed from " + source)
    elif res.status_code == 400:
        print("Invalid parameter values")
    else:
        print("Internal server error!")

def create_domain(domain):
    res = req.put(BASE_PATH + "domains/" + domain)
    if res.status_code == 204:
        print("The domain was successfully added")
    elif res.status_code == 400:
        print("Invalid domain")
    else:
        print("Internal error!")

def main(action):
    if action == "createdomain":
        create_domain(sys.argv[2])
    elif action == "listmappings" and len(sys.argv) == 2:
        list_all_user_mappings()
    elif action == "listmappings" and len(sys.argv) > 2:
        source = sys.argv[2]
        list_user_mappings(source)
    elif action == "addaddressmapping":
        source = sys.argv[2]
        destination = sys.argv[3]
        add_address_mapping(source, destination) 
    elif action == "removeaddressmapping":
        source = sys.argv[2]
        destination = sys.argv[3]
        remove_address_mapping(source, destination)

main(sys.argv[1])
