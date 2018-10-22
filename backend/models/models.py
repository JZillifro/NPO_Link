from npolinkapi import app
from flask_sqlalchemy import SQLAlchemy

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

def create(app):
    db.init_app(app)
    db.create_all()
