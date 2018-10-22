# Import flask dependencies
from flask import Blueprint, request, jsonify

# Import the database object from the main app module
from npolinkapi import db
from sqlalchemy import inspect

# Import module models (i.e. User)
from npolinkapi.nonprofit.models import Nonprofit

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_nonprofit = Blueprint('nonprofit', __name__, url_prefix='/nonprofit')

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}

# Set the route and accepted methods
@mod_nonprofit.route('/<id>/', methods=['GET'])
def getNonprofit(id):

    nonprofit = Nonprofit.query.filter_by(id=id).first()
    return jsonify(object_as_dict(nonprofit))
