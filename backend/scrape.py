import requests
import json
from pprint import pprint

organizations_list = []
states = ["TX", "NY", "CA", "NJ", "DC", "PA", "MA", "OR", "IL", "OH", "FL", "MI", "VA", "MN", "GA", "NC", "MD", "MO", "WA", "WI", "IN", "CT", "TN", "CO"]
categories = {"A":"Arts, Culture, and Humanities", "B":"Education", "C": "Environment and Animals", "D":"Environment and Animals", "E":"Health", "F":"Health", "G":"Health","H":"Health", "I":"Human Services", "J":"Human Services", "K":"Human Services", "L":"Human Services", "M":"Human Services", "N":"Human Services", "O":"Human Services", "P":"Human Services", "Q":"International, Foreign Affairs", "R":"Public, Societal Benefit", "S":"Public, Societal Benefit", "T":"Public, Societal Benefit", "U":"Public, Societal Benefit", "V":"Public, Societal Benefit", "W":"Public, Societal Benefit", "X":"Religion Related", "Y":"Mutual/Membership Benefit", "Z":"Unknown, Unclassified "}

def getMore():
    global organizations_list
    propublica_api = 'https://projects.propublica.org/nonprofits/api/v2/organizations/'
    for org in organizations_list:
        try:
            ein = ''.join( c for c in org['ein'] if  c not in '-' )
            r = requests.get(propublica_api + ein +  '.json')
            json_result = r.json()

            o = json_result.get('organization')
            org['category_code'] = o.get("ntee_code")
            code = org['category_code']
            if code != None:
                org['category'] = categories[code[0]]

            pprint(org)
        except:
            break

    # pprint(json.dumps(organizations_list))

def getdata():
    global organizations_list
    globalgiving_api = 'https://api.globalgiving.org/api/public/orgservice/all/organizations?api_key=e3204078-23de-484c-a9ad-8211c89b12d1'
    headers = {'Content-Type' : 'application/json', 'Accept': 'application/json'}

    count = 0
    has_next = True
    nextId = 1233 #500 -> 1233 = 101 ;1233 -> 3346 = 203
    while(has_next):
        try:
            if count >= 10:
                # print(nextId)
                break
            r = requests.get(globalgiving_api + '&nextOrgId=' + str(nextId), headers=headers)
            json_result = r.json()

            organizations = json_result.get('organizations')
            org = organizations.get('organization')
            for o in iter(org):
                ein = o.get('ein')
                state = o.get('state')
                logo = o.get('logoUrl')
                if state in states and ein != None and logo != None:
                    org = {}
                    org['ein'] = ein
                    org['logo'] = logo
                    org['name'] = o.get('name')
                    org['city'] = o.get('city')
                    org['state'] = o.get('state')
                    org['address'] = o.get('addressLine1')
                    org['mission'] = o.get('mission')
                    organizations_list.append(org)
                    count += 1

            has_next = organizations.get('hasNext')
            nextId = organizations.get('nextOrgId')
        except:
            break

if __name__ == "__main__":
    getdata()
    getMore()
