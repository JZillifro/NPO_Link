from npolinkapi import db

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
    nonprofits = db.relationship("Nonprofit", back_populates="category")

    def __init__(self, id, name, code, parent_category, image, description):
        self.id = id
        self.name = name
        self.code = code
        self.parent_category = parent_category
        self.image = image
        self.description = description

    def __repr__(self):
        return '<Category %r>' % (self.name)
