# Import flask dependencies
from flask import Blueprint, request, jsonify

# Import the database object from the main app module
from npolinkapi import db
from sqlalchemy import inspect
import json

# Import module models (i.e. User)
from npolinkapi.api.models import Category, Location

# Define the blueprint: 'auth', set its url prefix: app.url/auth
categories_blueprint = Blueprint('categories', __name__, url_prefix='/categories')

# Set the route and accepted methods
@categories_blueprint.route('/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })

@categories_blueprint.route('/all', methods=['GET'])
def get_all():
    return jsonify([cat.to_json() for cat in Category.query.all()])

@categories_blueprint.route('/<id>', methods=['GET'])
def get_by_id(id):
    return jsonify( [cat.to_json() for cat in Category.query.filter_by(code=id)])

@categories_blueprint.route('locations/<category_id>', methods=['GET'])
def get_locations_for_category(category_id):

    location_ids = Category.query.filter_by(id=category_id).options(load_only("location_ids")).one().to_json()['location_ids']
    location_id_list = json.loads(location_ids)

    Location.query.filter(Location.id.in_(location_id_list)).all()

    """Get all locations for a category"""
    response_object = {
        'status': 'success',
        'data': {
            'locations': [location.to_json() for location in Location.query.filter(Location.id.in_(location_id_list)).all()]
        }
    }
    return jsonify(response_object), 200
