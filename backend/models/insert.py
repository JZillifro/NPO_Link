from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://gerardomares:@localhost/npolink'
db = SQLAlchemy(app)


class Nonprofit(db.Model):
    __tablename__ = 'nonprofit'
    """
    json data:
    {
       "id": 1,
       "name": "",
       "ein": "",
       "address": "",
       "mission": "",
       "logo": "",
       "category_id": 1,
       "location_id": 1
    }
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    ein = db.Column(db.String(80), unique=False, nullable=False)
    logo = db.Column(db.String(80), unique=True, nullable=True)
    description = db.Column(db.String(25600), unique=False, nullable=True)
    address = db.Column(db.String(80), unique=False, nullable=True)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    location = db.relationship("Location")
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship("Category")

class Location(db.Model):
    __tablename__ = 'location'
    """
    json data:
    {
       "name": "Portland, OR",
       "city": "Portland",
       "state": "OR",
       "id": 1,
       "description": ""
    }
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    state = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(25600), unique=False, nullable=False)
    nonprofits = db.relationship("Nonprofit", back_populates="location")

class Category(db.Model):
    __tablename__ = 'category'
    """
    json data:
    {
       "id": 1,
       "name": "",
       "code": "",
       "description": ""
    }
    """
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(25600), unique=False, nullable=False)
    code = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    nonprofits = db.relationship("Nonprofit", back_populates="category")



def insert():
    locations = []
    with open('files/data/loc-results.json') as json_data:
        data = json.load(json_data)
        for location in data:
            loc = Location(id=location['id'],name=location['name'], city=location['city'], state=location['state'], description=location['description'])
            locations.append(loc)
        db.session.add_all(locations)
        db.session.flush()
        db.session.commit()

    categories = []
    with open('files/data/cat-results.json') as json_data:
        data = json.load(json_data)
        for category in data:
            cat = Category(id=category['id'],name=category['title'], description=location['description'], code=category['code'])
            categories.append(cat)
        db.session.add_all(categories)
        db.session.flush()
        db.session.commit()


    nonprofits = []
    with open('files/data/org-results.json') as json_data:
        data = json.load(json_data)
        for nonprofit in data:
            org = Nonprofit(id=nonprofit['id'],name=nonprofit['name'], description=nonprofit['description'], ein=nonprofit['ein'], logo=nonprofit['logo'], address=nonprofit['address'], location_id=nonprofit['location_id'], category_id=nonprofit['category_id'])
            nonprofits.append(org)
        db.session.add_all(nonprofits)
        db.session.flush()
        db.session.commit()


if __name__ == "__main__":
    db.init_app(app)
    db.create_all()
    insert()
