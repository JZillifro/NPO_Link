# Import flask dependencies
from flask import Blueprint, request, jsonify

# Import the database object from the main app module
from npolinkapi import db
from sqlalchemy import inspect, and_
from sqlalchemy.orm import load_only


# Import module models (i.e. nonprofit)
from npolinkapi.api.models import Nonprofit, Location, Category

# Define the blueprint: 'auth', set its url prefix: app.url/auth
nonprofits_blueprint = Blueprint('nonprofits', __name__, url_prefix='/v1.0/nonprofits')

# Set the route and accepted methods
@nonprofits_blueprint.route('/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })

@nonprofits_blueprint.route('/all', methods=['GET'])
def get_all_nonprofits():
    """Get all nonprofits"""
    nonprofits = Nonprofit.query.all()
    response_object = {
        'status': 'success',
        'data': {
            'nonprofits': [nonprofit.to_json() for nonprofit in nonprofits]
        }
    }
    return jsonify(response_object), 200

@nonprofits_blueprint.route('/<nonprofit_id>', methods=['GET'])
def get_nonprofit_by_id(nonprofit_id):
    """Get single nonprofit details"""
    response_object = {
        'status': 'fail',
        'message': 'Invalid nonprofit id provided'
    }
    try:
        nonprofit = Nonprofit.query.filter_by(id=int(nonprofit_id)).first()
        if not nonprofit:
            response_object = {
                'status': 'fail',
                'message': 'Nonprofit not found'
            }
            return jsonify(response_object), 404
        else:
            response_object = {
                'status': 'success',
                'data': nonprofit.to_json()
            }
            return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404


@nonprofits_blueprint.route('/category/<category_id>', methods=['GET'])
def get_nonprofits_by_category(category_id):
    response_object = {
        'status': 'fail',
        'message': 'Invalid category id provided'
    }

    try:
        nonprofits = Nonprofit.query.filter_by(category_id=int(category_id)).all()
        if nonprofits:
            response_object = {
                'status': 'success',
                'data': {
                    'nonprofits': [nonprofit.to_json() for nonprofit in nonprofits]
                }
            }

        return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404


@nonprofits_blueprint.route('/location/<location_id>', methods=['GET'])
def get_nonprofits_by_location(location_id):
    response_object = {
        'status': 'fail',
        'message': 'Invalid location id provided'
    }

    try:
        nonprofits = Nonprofit.query.filter_by(location_id=int(location_id)).all()
        if nonprofits:
            response_object = {
                'status': 'success',
                'data': {
                    'nonprofits': [nonprofit.to_json() for nonprofit in nonprofits]
                }
            }

        return jsonify(response_object), 200
    except:
        return jsonify(response_object), 404


@nonprofits_blueprint.route('/location/city/<city>', methods=['GET'])
def get_nonprofits_by_city(city):
    response_object = {
        'status': 'fail',
        'message': 'Invalid request'
    }

    try:
        location_id = Location.query.filter_by(name=str(city)).options(load_only("id")).one().to_json()['id']
        if not location_id:
            return jsonify(response_object), 404
        else:

            nonprofits =  Nonprofit.query.filter_by(location_id=int(location_id)).all()
            response_object = {
                'status': 'success',
                'data': {
                    'nonprofits': [nonprofit.to_json() for nonprofit in nonprofits]
                }
            }

            return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404

@nonprofits_blueprint.route('/location/state/<state>', methods=['GET'])
def get_nonprofits_by_state(state):
    response_object = {
        'status': 'fail',
        'message': 'Invalid request'
    }

    try:
        location_ids = [loc.id for loc in Location.query.filter_by(state=str(state)).options(load_only('id')).all()]
        if not location_ids:
            return jsonify(response_object), 404
        else:
            if len(location_ids) == 0:
                response_object = {
                    'status': 'success',
                    'data': {
                        'nonprofits': []
                    }
                }
            else:
                nonprofits =  Nonprofit.query.filter(Nonprofit.location_id.in_(location_ids)).all()
                response_object = {
                    'status': 'success',
                    'data': {
                        'nonprofits': [nonprofit.to_json() for nonprofit in nonprofits]
                    }
                }

            return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404


@nonprofits_blueprint.route('/location/<location_id>/category/<category_id>', methods=['GET'])
def get_nonprofits_by_state_and_category_ids(location_id, category_id):
    response_object = {
        'status': 'fail',
        'message': 'Invalid request'
    }

    try:
        nonprofits =  Nonprofit.query.filter_by(location_id=int(location_id)).filter_by(category_id=int(category_id)).all()
        response_object = {
            'status': 'success',
            'data': {
                'nonprofits': [nonprofit.to_json() for nonprofit in nonprofits]
            }
        }

        return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404


@nonprofits_blueprint.route('/location/state/<state>/category/code/<category>', methods=['GET'])
def get_nonprofits_by_state_and_category(state, category):
    response_object = {
        'status': 'fail',
        'message': 'Invalid request'
    }

    try:
        location_ids = [loc.id for loc in Location.query.filter_by(state=str(state)).options(load_only('id')).all()]
        category = Category.query.filter_by(code=str(category)).one()
        if not location_ids or not category:
            return jsonify(response_object), 404
        else:
            if len(location_ids) == 0:
                response_object = {
                    'status': 'success',
                    'data': {
                        'nonprofits': []
                    }
                }
            else:
                nonprofits =  Nonprofit.query.filter(Nonprofit.location_id.in_(location_ids)).filter_by(category_id=int(category.id)).all()
                response_object = {
                    'status': 'success',
                    'data': {
                        'nonprofits': [nonprofit.to_json() for nonprofit in nonprofits]
                    }
                }

            return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404
