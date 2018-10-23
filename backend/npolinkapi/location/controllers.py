# Import flask dependencies
from flask import Blueprint, request, jsonify

# Import the database object from the main app module
from npolinkapi import db
from sqlalchemy import inspect

# Import module models (i.e. User)
from npolinkapi.location.models import Location

# Define the blueprint: 'auth', set its url prefix: app.url/auth
locations_blueprint = Blueprint('locations', __name__, url_prefix='/locations')


# Set the route and accepted methods
@locations_blueprint.route('/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
# route 'all', methods='GET'
@locations_blueprint.route('/all', methods=['GET'])
def get_all_locations():
    locations = Location.query.all()
    return jsonify(location.to_json() for location in locations)


# Get all locations which include NPOs of this category
# Will need this for category pages
@locations_blueprint.route('/category/<id>', methods=['GET'])
def get_location_by_category(id):
    pass

# Below are technically not specific to locations

# Return locations that have NPOs for a specific state?
# @locations_blueprint.route('/state/<id>', methods=['GET'])
# def get_locations_by_state(id):
#
# @locations_blueprint.route('/city/<id>', methods=['GET'])
# def get_locations_by_city(id):
