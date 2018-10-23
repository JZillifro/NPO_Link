from npolinkapi import db

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
    nonprofits = db.relationship("Nonprofit", back_populates="location")

    def __init__(self, id, name, city, state, image, description):
        self.id = id
        self.name = name
        self.city = city
        self.state = state
        self.image = image
        self.description = description

    def __repr__(self):
        return '<Location %r>' % (self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'state': self.state,
            'description': self.description,
            'image': self.image
        }
