import json
from pprint import pprint

category_results = dict()
org_list = []

def generate():
    global category_results
    global org_list

    with open('../data/codes.json') as category_json_data:
        category_results = json.load(category_json_data)
        id = 1
        images = {}
        for key in category_results:
            category = category_results[key]
            category.pop('keywords', None)
            category['id'] = id
            category['code'] = key
            if len(key) == 1:
                images[key] = category['image']
                category['parent_code'] = key
            else:
                code = key[0]
                category['image'] = images[code]
                category['parent_code'] = code

            id += 1

    with open('../data/proj_results-2.json') as org_json_data:
        org_list = json.load(org_json_data)
        org_id = 1
        for org in org_list:
            code = org['category_code'][:3]


            if code in category_results:
                category = category_results[code]
            else:
                code = 'P80'

            # org['category_code'] = code
            org.pop('category_code', None)
            org['description'] = org['mission']
            org.pop('mission')
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
            org['location_id'] = location_dict[name]['id']

        org.pop('city', None)
        org.pop('state', None)

        volunteer_events = org['projects']

        for ve in volunteer_events:
            ve['organization_id'] = org['id']
            ve['id'] = volunteer_id
            volunteer_id += 1
            volunteer_list.append(ve)
        org.pop('projects', None)

    location_data = {}
    for location in location_list:
        id = location['id']
        data = {}
        data['orgs'] = []
        data['categories'] = []
        location_data[id] = data

    category_data = {}
    for category in category_list:
        id = category['id']
        data = {}
        data['locations'] = []
        data['orgs'] = []
        category_data[id] = data


    for nonprofit in org_list:
        nonprofit_id = nonprofit['id']
        location_id = nonprofit['location_id']
        category_id = nonprofit['category_id']

        data = location_data[location_id]
        if nonprofit_id not in data['orgs']:
            data['orgs'].append(nonprofit_id)

        if category_id not in data['categories']:
            data['categories'].append(category_id)

        data2 = category_data[category_id]

        if nonprofit_id not in data2['orgs']:
            data2['orgs'].append(nonprofit_id)

        if location_id not in data2['locations']:
            data2['locations'].append(location_id)


        for location in location_list:
            location['orgs'] = location_data[location['id']]['orgs']
            location['categories'] = location_data[location['id']]['categories']


        for category in category_list:
            category['orgs'] = category_data[category['id']]['orgs']
            category['locations'] = category_data[category['id']]['locations']



    with open('../results/org-results.json', 'w') as org_outfile:
        json.dump(org_list, org_outfile)

    with open('../results/loc-results.json', 'w') as location_outfile:
        json.dump(location_list, location_outfile)

    with open('../results/cat-results.json', 'w') as category_outfile:
        json.dump(category_list, category_outfile)

    with open('../results/vol-results.json', 'w') as volunteer_outfile:
        json.dump(volunteer_list, volunteer_outfile)


if __name__ == "__main__":
    generate()
