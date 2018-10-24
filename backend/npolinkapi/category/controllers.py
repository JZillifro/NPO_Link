# Import flask dependencies
from flask import Blueprint, request, jsonify

# Import the database object from the main app module
from npolinkapi import db
from sqlalchemy import inspect

# Import module models (i.e. User)
from npolinkapi.api.models import Category

# Define the blueprint: 'auth', set its url prefix: app.url/auth
categories_blueprint = Blueprint('categories', __name__, url_prefix='/categories')

# Set the route and accepted methods
@categories_blueprint.route('/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
@categories_blueprint.route('/', methods=['GET'])
def get_all():
    return jsonify([cat.to_json() for cat in Category.query.all()])

@categories_blueprint.route('/<id>', methods=['GET'])
def get_by_id(id):
    return "Trying to query for %s\n" % (id)
    return jsonify( [cat.to_json() for cat in Category.query.filter_by(code=id)])