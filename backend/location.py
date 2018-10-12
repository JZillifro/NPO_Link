import json
import requests

def getdata():
    wikipedia_api = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro&explaintext&redirects&format=json&titles='

    locations = []
    with open('loc-results.json') as location_json_data:
        locations = json.load(location_json_data)


        for loc in locations:
            city = loc['city']
            state = loc['state']
            location = city + ',_' + state

            if location == 'Barrytown,_NY':
                location = 'Barrytown,_New_York'

            r = requests.get(wikipedia_api + location)
            json_result = r.json()
            pages = json_result.get('query').get('pages')

            page_iter = iter(pages)
            page = pages[next(page_iter)]
            page_id = page['pageid']
            loc['description'] = page['extract']

    with open('loc-results-desc.json', 'w') as outfile:
        json.dump(locations, outfile)

if __name__ == "__main__":
    getdata()
