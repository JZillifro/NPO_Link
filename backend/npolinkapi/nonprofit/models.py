from npolinkapi import db

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
