# Import flask dependencies
from flask import Blueprint, request, jsonify

# Import the database object from the main app module
from npolinkapi import db
from sqlalchemy import inspect

# Import module models (i.e. User)
from npolinkapi.api.models import Location, Category, Nonprofit

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


# Get all categories for this location
# Will need this for location pages
@locations_blueprint.route('/category/<location_id>', methods=['GET'])
def get_categories_by_location(location_id):
    categories = Location.query.filter_by(id=location_id).options(load_only("category_ids")).one().to_json()['category_ids']

    category_id_list = json.loads(categories)

    category_list = Category.query.filter(Category.id.in_(category_id_list)).all()

    return jsonify(category.to_json() for category in category_list)

@locations_blueprint.route('/npos/<location_id>', methods=['GET'])
def get_npos_by_location(location_id):
    npos = Location.query.filter_by(id=location_id).options(load_only("npo_ids")).one().to_json()['npo_ids']

    npo_id_list = json.loads(npos)

    npo_list = Nonprofit.query.filter(Nonprofit.id.in_(npo_id_list)).all()

    return jsonify(npo.to_json() for npo in npo_list)

# Below are technically not specific to locations

# Return locations that have NPOs for a specific state?
# @locations_blueprint.route('/state/<id>', methods=['GET'])
# def get_locations_by_state(id):
#
# @locations_blueprint.route('/city/<id>', methods=['GET'])
# def get_locations_by_city(id):
