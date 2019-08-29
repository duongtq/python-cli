import sys
import requests as req
import json

BASE_PATH = "http://127.0.0.1:8000/"

action = sys.argv[1].lower()


def print_json(obj):
    parsed = json.loads(obj.text)
    print(json.dumps(parsed, indent=4, sort_keys=True))


def get_all_domains():
    res = req.get(BASE_PATH + "domains")
    print_json(res)


def add_domain(domain_name):
    res = req.put(BASE_PATH + "domains/" + domain_name)

    if res.status_code == 204:
        print("New domain is added.")
    elif res.status_code == 400:
        print("Invalid request for domain creation.")
    else:
        print("Internal server error!")


def delete_domain(domain_name):
    res = req.delete(BASE_PATH + "domains/" + domain_name)

    if res.status_code == 204:
        print("Domain is removed.")
    elif res.status_code == 500:
        print("Internal server error!")


def test_domain_existence(domain_name):
    res = req.get(BASE_PATH + "domains/" + domain_name)
    if res.status_code == 204:
        print("Domain does exists.")
    elif res.status_code == 404:
        print("Domain does not exists.")
    else:
        print("Internal server error.")


def get_domain_aliases(domain_name):
    res = req.get(BASE_PATH + "domains/" + domain_name + "/aliases")
    if res.status_code == 200:
        print("OK")
        print_json(res)
    elif res.status_code == 404:
        print("The domain does not exist.")
    else:
        print("Internal server error.")


def add_alias_for_domain(source_domain, destination_domain):
    add_domain(source_domain)
    res = req.put(BASE_PATH + "domains/" + destination_domain + "/aliases/" + source_domain)
    if res.status_code == 204:
        print("Alias has been added for domain %s") % (destination_domain)
    elif res.status_code == 404:
        print(source_domain + " does not exist.")
    else:
        print("Internal server error.")


def remove_alias_for_domain(source_domain, destination_domain):
    res = req.delete(BASE_PATH + "domains/" + destination_domain + "/aliases/" + source_domain)
    if res.status_code == 204:
        print("Alias have been removed for domain %s") % (destination_domain)
    elif res.status_code == 404:
        print(source_domain + " does not exist.")
    else:
        print("Internal server error.")


def main(action):
    if action == "getdomains":
        get_all_domains()
    elif action == "adddomain":
        domain_name = sys.argv[2]
        add_domain(domain_name)
    elif action == "deletedomain":
        domain_name = sys.argv[2]
        delete_domain(domain_name)
    elif action == "testdomainexistence":
        domain_name = sys.argv[2]
        test_domain_existence(domain_name)
    elif action == "getdomainaliases":
        domain_name = sys.argv[2]
        get_domain_aliases(domain_name)
    elif action == "adddomainaliases":
        destination_domain = sys.argv[2]
        source_domain = sys.argv[3]
        add_alias_for_domain(source_domain, destination_domain)
    elif action == "deletedomainaliases":
        destination_domain = sys.argv[2]
        source_domain = sys.argv[3]
        remove_alias_for_domain(source_domain, destination_domain)

main(sys.argv[1])