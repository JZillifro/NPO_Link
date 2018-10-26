# Import flask dependencies
from flask import Blueprint, request, jsonify

# Import the database object from the main app module
from npolinkapi import db
from sqlalchemy import inspect
from sqlalchemy.orm import load_only

# Import module models (i.e. User)
from npolinkapi.api.models import Location, Category

# Define the blueprint: 'auth', set its url prefix: app.url/auth
locations_blueprint = Blueprint('locations', __name__, url_prefix='/v1.0/locations')


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
    response_object = {
        'status': 'success',
        'data': {
            'locations' : [location.to_json() for location in locations]
        }
    }
    return jsonify(response_object), 200

@locations_blueprint.route('/<int:page>',methods=['GET'])
def view(page=1):
    per_page = 12
    locations = Location.query.order_by(Location.id.asc()).paginate(page,per_page,error_out=False)
    paged_response_object = {
        'status': 'success',
        'data': {
            'locations': [location.to_json() for location in locations.items]
        },
        'has_next': locations.has_next,
        'has_prev': locations.has_prev,
        'next_page': locations.next_num,
        'pages': locations.pages
    }
    return jsonify(paged_response_object), 200

@locations_blueprint.route('/location/<id>', methods=['GET'])
def get_by_location_by_id(id):
    response_object = {
        'status': 'fail',
        'message': 'No location for given id'
    }

    try:
        location = Location.query.filter_by(id=int(id)).one()
        if not location:
            response_object = {
                'status': 'fail',
                'message': 'No location for given id'
            }
            return jsonify(response_object), 404
        else:
            response_object = {
                'status': 'success',
                'data': {
                    'location' : location.to_json()
                }
            }

            return jsonify(response_object), 200

    except ValueError:
        return jsonify(response_object), 404

# Get all locations which include NPOs of this category
# Will need this for category pages
@locations_blueprint.route('/category/<category_id>', methods=['GET'])
def get_location_by_category(category_id):
    response_object = {
        'status': 'fail',
        'message': 'No locations found'
    }

    try:
        category = Category.query.filter_by(id=int(category_id)).options(load_only("location_list")).one()

        if not category:
            response_object['message'] = 'Invalid category'
            return jsonify(response_object), 404
        else:
            location_ids = category.to_json()['locations']
            if len(location_ids) == 0:
                response_object = {
                    'status': 'success',
                    'data': {
                        'locations': []
                    }
                }
            else:
                locations = Location.query.filter(Location.id.in_(location_ids)).all()
                response_object = {
                    'status': 'success',
                    'data': {
                        'locations': [location.to_json() for location in locations]
                    }
                }

            return jsonify(response_object), 200
    except ValueError:
        response_object['message'] = 'Invalid category'
        return jsonify(response_object), 404

# Will need this for category pages
@locations_blueprint.route('/category/<category_code>', methods=['GET'])
def get_location_by_category_code(category_code):
    response_object = {
        'status': 'fail',
        'message': 'No locations found'
    }

    try:
        category = Category.query.filter_by(code=str(category_code)).options(load_only("location_list")).one()

        if not category:
            response_object['message'] = 'Invalid category'
            return jsonify(response_object), 404
        else:
            location_ids = category.to_json()['locations']
            if len(location_ids) == 0:
                response_object = {
                    'status': 'success',
                    'data': {
                        'locations': []
                    }
                }
            else:
                locations = Location.query.filter(Location.id.in_(location_ids)).all()
                response_object = {
                    'status': 'success',
                    'data': {
                        'locations': [location.to_json() for location in locations]
                    }
                }

            return jsonify(response_object), 200
    except ValueError:
        response_object['message'] = 'Invalid category'
        return jsonify(response_object), 404
# Below are technically not specific to locations

# Return locations that have NPOs for a specific state?
# @locations_blueprint.route('/state/<id>', methods=['GET'])
# def get_locations_by_state(id):
#
# @locations_blueprint.route('/city/<id>', methods=['GET'])
# def get_locations_by_city(id):
