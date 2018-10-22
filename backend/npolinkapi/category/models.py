from npolinkapi import db

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
