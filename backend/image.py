import requests
import json

def get_image():
    base_url = 'https://en.wikipedia.org/api/rest_v1/page/media/'
    with open("loc-results.json", 'r') as f:
        locations =  json.load(f)
        for loc in locations:
            city = loc["city"]
            state = loc["state"]
            if city == "Barrytown" and state == "NY":
                state == "New_York"
            r = requests.get(base_url + city + ",_" + state)
            try:
                print("%s, %s" % (city, state))
                print (r.json()["items"][0]["thumbnail"]["source"])# can change thumbnail for original for higher res image
                print("width: %d, height %d " % (r.json()["items"][0]["thumbnail"]["width"],r.json()["items"][0]["thumbnail"]["height"]))
                loc["image"] = r.json()["items"][0]["thumbnail"]["source"]
            except:
                print("Error finding image for %s, %s" % (city, state))
    with open("loc-image.json", 'w') as f:
        json.dump(locations, f)
if __name__ == "__main__":
    get_image()