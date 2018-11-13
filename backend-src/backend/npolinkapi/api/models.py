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
       "location_id": 1,
       "projects": []
    }
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    ein = db.Column(db.String(80), unique=False, nullable=False)
    logo = db.Column(db.String(80), unique=True, nullable=True)
    description = db.Column(db.String(25600), unique=False, nullable=True)
    address = db.Column(db.String(80), unique=False, nullable=True)
    projects = db.Column(db.PickleType, unique=False, nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    location = db.relationship("Location")
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship("Category")


    def __init__(self, id, name, ein, logo, description, address, location_id, category_id, projects):
        self.id = id
        self.name = name
        self.ein = ein
        self.logo = logo
        self.description = description
        self.address = address
        self.location_id = location_id
        self.category_id = category_id
        self.projects = projects

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
            'category_id': self.category_id,
            'projects': self.projects
        }

class Location(db.Model):
    __tablename__ = 'location'
    """
    json data:
    {
       "name": "Portland, OR",
       "city": "Portland",
       "state": "OR",
       "id": 1,
       "description": "",
       "image": ""
    }
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    state = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(25600), unique=False, nullable=False)
    image = db.Column(db.String(20000), unique=False, nullable=False)
    nonprofit_list = db.Column(db.PickleType, unique=False, nullable=False)
    category_list = db.Column(db.PickleType, unique=False, nullable=False)
    nonprofits = db.relationship("Nonprofit", back_populates="location")

    def __init__(self, id, name, city, state, image, description, nonprofit_list, category_list):
        self.id = id
        self.name = name
        self.city = city
        self.state = state
        self.image = image
        self.description = description
        self.nonprofit_list = nonprofit_list
        self.category_list = category_list

    def __repr__(self):
        return '<Location %r>' % (self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'state': self.state,
            'description': self.description,
            'image': self.image,
            'categories': self.category_list,
            'nonprofits': self.nonprofit_list
        }

class Category(db.Model):
    __tablename__ = 'category'
    """
    json data:
    {
       "id": 1,
       "name": "",
       "code": "",
       "description": "",
       "image": "",
       "parent_category" : ""
    }
    """
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(25600), unique=False, nullable=False)
    code = db.Column(db.String(80), unique=True, nullable=False)
    parent_category = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    image = db.Column(db.String(20000), unique=False, nullable=False)
    nonprofit_list = db.Column(db.PickleType, unique=False, nullable=False)
    nonprofit_amount = db.Column(db.Integer, nullable=True)
    location_list = db.Column(db.PickleType, unique=False, nullable=False)
    nonprofits = db.relationship("Nonprofit", back_populates="category")

    def __init__(self, id, name, code, parent_category, image, description, location_list, nonprofit_list):
        self.id = id
        self.name = name
        self.code = code
        self.parent_category = parent_category
        self.image = image
        self.description = description
        self.location_list = location_list
        self.nonprofit_list = nonprofit_list
        if len(self.nonprofit_list):
            self.nonprofit_amount = len(self.nonprofit_list)
        else:
            self.nonprofit_amount = None

    def __repr__(self):
        return '<Category %r>' % (self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'image': self.image,
            'description': self.description,
            'parent_category': self.parent_category,
            'locations': self.location_list,
            'nonprofits': self.nonprofit_list
        }
