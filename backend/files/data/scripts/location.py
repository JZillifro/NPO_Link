import json
import requests
from pprint import pprint

GOOGLE_KEY = 'AIzaSyBLZSNg1-dw_h_R8VlX0MQ84-p_27XFgNk'

PHOTO_API = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&key=AIzaSyBLZSNg1-dw_h_R8VlX0MQ84-p_27XFgNk&photoreference='

def getdata():
    wikipedia_api = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro&explaintext&redirects&format=json&titles='

    place_search_api = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?inputtype=textquery&key=' + GOOGLE_KEY
    place_details_api = 'https://maps.googleapis.com/maps/api/place/details/json?key=' + GOOGLE_KEY

    static_map_api = 'https://maps.googleapis.com/maps/api/staticmap?zoom=12&size=600x600&maptype=roadmap&key=AIzaSyBLZSNg1-dw_h_R8VlX0MQ84-p_27XFgNk'

    locations = []
    with open('../results/loc-results.json') as location_json_data:
        locations = json.load(location_json_data)
    #
    #
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


            # r = requests.get(place_search_api + '&input=' + location)
            # json_result = r.json()
            # candidates = json_result.get('candidates')
            #
            # if len(candidates) > 0:
            #     candidate = candidates[0]
            #     place_id = candidate.get('place_id')
            #     r = requests.get(place_details_api + '&placeid=' + place_id + '&fields=photo')
            #     details_json = r.json()
            #     photo_results = details_json.get('result').get('photos')
            #     if len(photo_results) > 0:
            #         for photo in photo_results:
            #             print(photo.get('html_attributions'))
            #     else:
            #         print('no photo results for ' + location )
            #     break
            #
            # else:
            #     print('no results for ' + location )

            # r = requests.get(static_map_api + '&center=' + location)
            # json_result = r.json()
            # print(r)




    with open('../results/loc-results-desc.json', 'w') as outfile:
        json.dump(locations, outfile)


    # PLACES_API = 'https://maps.googleapis.com/maps/api/place/details/json?key=AIzaSyBLZSNg1-dw_h_R8VlX0MQ84-p_27XFgNk&placeid='
    # placeid = 'ChIJLwPMoJm1RIYRetVp1EtGm10'
    # r = requests.get(PLACES_API + placeid)


if __name__ == "__main__":
    getdata()
