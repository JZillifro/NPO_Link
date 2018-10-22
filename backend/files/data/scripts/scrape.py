import requests
import json
from pprint import pprint

organizations_list = []
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS",
          "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

categories = {"A":"Arts, Culture, and Humanities", "B":"Education", "C": "Environment and Animals", "D":"Environment and Animals", "E":"Health", "F":"Health", "G":"Health","H":"Health", "I":"Human Services", "J":"Human Services", "K":"Human Services", "L":"Human Services", "M":"Human Services", "N":"Human Services", "O":"Human Services", "P":"Human Services", "Q":"International, Foreign Affairs", "R":"Public, Societal Benefit", "S":"Public, Societal Benefit", "T":"Public, Societal Benefit", "U":"Public, Societal Benefit", "V":"Public, Societal Benefit", "W":"Public, Societal Benefit", "X":"Religion Related", "Y":"Mutual/Membership Benefit", "Z":"Unknown, Unclassified "}

def getCode(ein):

    if ein == None:
        return None
    # global organizations_list
    propublica_api = 'https://projects.propublica.org/nonprofits/api/v2/organizations/'
    # for org in organizations_list:
    try:
        ein_number = ''.join( c for c in ein if  c not in '-' )
        r = requests.get(propublica_api + ein_number +  '.json')
        json_result = r.json()

        o = json_result.get('organization')
        return o.get("ntee_code")
        # code = org['category_code']

    except:
        return None

    # print(json.dumps(organizations_list))

def getdata():
    global organizations_list
    globalgiving_api = 'https://api.globalgiving.org/api/public/orgservice/all/organizations?api_key=e3204078-23de-484c-a9ad-8211c89b12d1'
    headers = {'Content-Type' : 'application/json', 'Accept': 'application/json'}
    projects_api = 'https://api.globalgiving.org/api/public/projectservice/organizations/'

    count = 0
    has_next = True
    nextId = 500 #500 -> 1233 = 101 ;1233 -> 3346 = 203
    while(has_next):
        try:
            if count >= 200:
                # print(nextId)
                break
            r = requests.get(globalgiving_api + '&nextOrgId=' + str(nextId), headers=headers)
            json_result = r.json()

            organizations = json_result.get('organizations')
            org = organizations.get('organization')
            for o in iter(org):
                id = o.get('id')
                ein = o.get('ein')
                state = o.get('state')
                logo = o.get('logoUrl')

                # projectLink title summary

                projects_request = requests.get(projects_api + str(id) + '/projects/?api_key=e3204078-23de-484c-a9ad-8211c89b12d1', headers=headers)
                project_result = projects_request.json()
                projects = project_result.get('projects').get('project')
                code = getCode(ein)
                if state in states and ein != None and logo != None and code != None:
                    org = {}
                    org['ein'] = ein
                    org['logo'] = logo
                    org['category_code'] = code
                    org['name'] = o.get('name')
                    org['city'] = o.get('city')
                    org['state'] = o.get('state')
                    org['address'] = o.get('addressLine1')
                    org['mission'] = o.get('mission')
                    org['projects'] = []

                    for p in iter(projects):
                        proj = {}
                        proj['title'] = p.get('title')
                        proj['summary'] = p.get('summary')
                        proj['projectLink'] = p.get('projectLink')
                        org['projects'].append(proj)


                    organizations_list.append(org)
                    count += 1

            has_next = organizations.get('hasNext')
            nextId = organizations.get('nextOrgId')
        except:
            break

    print(json.dumps(organizations_list))

if __name__ == "__main__":
    getdata()
