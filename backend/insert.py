from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

from npolinkapi import app
from npolinkapi import db
from npolinkapi.location.models import Location
from npolinkapi.category.models import Category
from npolinkapi.nonprofit.models import Nonprofit


locations = []
with open('files/data/loc-results.json') as json_data:
    data = json.load(json_data)
    for location in data:
        loc = Location(id=location['id'],name=location['name'], city=location['city'], state=location['state'], description=location['description'], image=location['image'])
        locations.append(loc)

categories = []
with open('files/data/cat-results.json') as json_data:
    data = json.load(json_data)
    for category in data:
        cat = Category(id=category['id'],name=category['title'], description=location['description'], code=category['code'], image=category['image'], parent_category=category['parent_code'])
        categories.append(cat)

nonprofits = []
with open('files/data/org-results.json') as json_data:
    data = json.load(json_data)
    for nonprofit in data:
        org = Nonprofit(id=nonprofit['id'],name=nonprofit['name'], description=nonprofit['description'], ein=nonprofit['ein'], logo=nonprofit['logo'], address=nonprofit['address'], location_id=nonprofit['location_id'], category_id=nonprofit['category_id'])
        nonprofits.append(org)

db.session.add_all(locations)
db.session.add_all(categories)
db.session.add_all(nonprofits)

db.session.flush()
db.session.commit()
