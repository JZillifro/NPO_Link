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
                category['parent_code'] = key[0]

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


    loc_data = {}
    for loc in location_list:
        id = loc['id']
        loc_data[id] = {'orgs': [], 'cats': []}

    cat_data = {}
    for cat in category_list:
        id = cat['id']
        cat_data[id] = {'orgs': [], 'locs': []}

    for npo in org_list:
        npo_id = npo['id']
        loc_id = npo['location_id']
        cat_id = npo['category_id']

        if npo_id not in loc_data[loc_id]['orgs']:
            loc_data[loc_id]['orgs'].append(npo_id)

        if cat_id not in loc_data[loc_id]['cats']:
            loc_data[loc_id]['cats'].append(cat_id)

        if npo_id not in cat_data[cat_id]['orgs']:
            cat_data[cat_id]['orgs'].append(npo_id)

        if loc_id not in cat_data[cat_id]['locs']:
            cat_data[cat_id]['locs'].append(loc_id)

    for loc in location_list:
        id = loc['id']
        loc['nonprofits'] = loc_data[id]['orgs']
        loc['categories'] = loc_data[id]['cats']

    for cat in category_list:
        id = cat['id']
        cat['nonprofits'] = cat_data[id]['orgs']
        cat['locations'] = cat_data[id]['locs']

    # with open('../results/org-results.json', 'w') as org_outfile:
    #     json.dump(org_list, org_outfile)
    #
    # with open('../results/loc-results.json', 'w') as location_outfile:
    #     json.dump(location_list, location_outfile)

    with open('../results/cat-results.json', 'w') as category_outfile:
        json.dump(category_list, category_outfile)

    # with open('../results/vol-results.json', 'w') as volunteer_outfile:
    #     json.dump(volunteer_list, volunteer_outfile)


if __name__ == "__main__":
    generate()
