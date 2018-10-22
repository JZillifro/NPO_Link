import json
from pprint import pprint

category_results = dict()
org_list = []

def generate():
    global category_results
    global org_list

    with open('codes.json') as category_json_data:
        category_results = json.load(category_json_data)
        id = 1
        for key in category_results:
            category = category_results[key]
            category.pop('keywords', None)
            category['id'] = id
            category['code'] = key
            id += 1

    with open('proj_results-2.json') as org_json_data:
        org_list = json.load(org_json_data)
        org_id = 1
        for org in org_list:
            code = org['category_code'][:3]


            if code in category_results:
                category = category_results[code]
            else:
                code = 'P80'

            org['category_code'] = code
            org['category_id'] = category['id']
            org['id'] = org_id
            org_id += 1


    category_list = []
    for key in category_results:
        cat = category_results[key]
        category_list.append(cat)


    location_dict = {}
    location_list = []

    volunteer_list = []
    volunteer_id = 1

    city_id = 1
    for org in org_list:
        city = org['city']
        state = org['state']
        name = city + ", " + state

        c = {}
        c['name'] = name
        c['city'] = city
        c['state'] = state

        if name not in location_dict:
            c['id'] = city_id
            location_dict[name] = c
            location_list.append(c)
            org['location_id'] = city_id
            city_id += 1
        else:
            org['city_id'] = location_dict[name]['id']

        volunteer_events = org['projects']

        for ve in volunteer_events:
            ve['organization_id'] = org['id']
            ve['id'] = volunteer_id
            volunteer_id += 1
            volunteer_list.append(ve)
        org.pop('projects', None)

    with open('org-results.json', 'w') as org_outfile:
        json.dump(org_list, org_outfile)

    with open('loc-results.json', 'w') as location_outfile:
        json.dump(location_list, location_outfile)

    with open('cat-results.json', 'w') as category_outfile:
        json.dump(category_list, category_outfile)

    with open('vol-results.json', 'w') as volunteer_outfile:
        json.dump(volunteer_list, volunteer_outfile)


if __name__ == "__main__":
    generate()