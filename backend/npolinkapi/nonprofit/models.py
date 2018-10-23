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


    def __init__(self, id, name, ein, logo, description, address, location_id, category_id):
        self.id = id
        self.name = name
        self.ein = ein
        self.logo = logo
        self.description = description
        self.address = address
        self.location_id = location_id
        self.category_id = category_id

    def __repr__(self):
        return '<Nonprofit %r>' % (self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'ein': self.ein,
            'logo': self.logo,
            'description': self.description,
            'address': self.address,
            'location_id': self.location_id,
            'category_id': self.category_id
        }
