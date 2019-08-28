import sys
import requests as rq

LIST_ACTION     = "LIST"
ADD_ACTION      = "ADD"
REMOVE_ACTION   = "REMOVE"
actions         = [LIST_ACTION, ADD_ACTION, REMOVE_ACTION]

ADDRESS_MAPPING = "ADDRESSMAPPINGS"
REGEX_MAPPING   = "REGEXMAPPINGS"
USER_MAPPING    = "USERMAPPINGS"
mappings        = [ADDRESS_MAPPING, REGEX_MAPPING, USER_MAPPING]

host            = sys.argv[1]
port            = sys.argv[2]
action          = sys.argv[3]
mapping         = sys.argv[4] 
# source          = sys.argv[5]
# destination     = sys.argv[6]

PATH            = 'http://' + host + ':' + port

# if action == ADD_ACTION:
#     if mapping == ADDRESS_MAPPING:
#         rq.put(PATH + "/domains/domain.tld")
#         response = rq.post(PATH + "/mappings/address/source@domain.tld/targets/alice@domain.tld")
#         print(response.status_code)

if action == LIST_ACTION:
    if mapping == USER_MAPPING:
        response = rq.get(PATH + "/mappings")
        print(response.status_code)
