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
       "description": ""
    }
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    state = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(25600), unique=False, nullable=False)
    nonprofits = db.relationship("Nonprofit", back_populates="location")

    def __init__(self, id, name, city, state, description):
        self.id = id
        self.name = name
        self.city = city
        self.state = state
        self.description = description

    def __repr__(self):
        return '<Location %r>' % (self.name)
