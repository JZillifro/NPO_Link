# Import flask dependencies
from flask import Blueprint, request, jsonify

# Import the database object from the main app module
from npolinkapi import db
from sqlalchemy import inspect, and_
from sqlalchemy.orm import load_only
from sqlalchemy.orm.exc import NoResultFound

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

@nonprofits_blueprint.route('/<int:page>',methods=['GET'])
def view(page=1):
    """Get all nonprofits paged"""
    per_page = 12
    nonprofits = Nonprofit.query.order_by(Nonprofit.id.asc()).paginate(page,per_page,error_out=False)
    paged_response_object = {
        'status': 'success',
        'data': {
            'nonprofits': [nonprofit.to_json() for nonprofit in nonprofits.items]
        },
        'has_next': nonprofits.has_next,
        'has_prev': nonprofits.has_prev,
        'next_page': nonprofits.next_num,
        'pages': nonprofits.pages
    }
    return jsonify(paged_response_object), 200

@nonprofits_blueprint.route('/nonprofit/<nonprofit_id>', methods=['GET'])
def get_nonprofit_by_id(nonprofit_id):
    """Get single nonprofit details"""
    response_object = {
        'status': 'fail',
        'message': 'Invalid nonprofit id provided'
    }
    try:
        nonprofit = Nonprofit.query.filter_by(id=int(nonprofit_id)).one()
        response_object = {
            'status': 'success',
            'data': {
                'nonprofit' :  nonprofit.to_json()
            }
        }
        return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404
    except NoResultFound:
        response_object['message'] = 'No nonprofit found for given id'
        return jsonify(response_object), 404

@nonprofits_blueprint.route('/category/<category_id>', methods=['GET'])
def get_nonprofits_by_category(category_id):
    """Get all nonprofits for a given category"""

    response_object = {
        'status': 'fail',
        'message': 'Invalid category id provided'
    }

    try:
        nonprofits = Nonprofit.query.filter_by(category_id=int(category_id)).all()
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
    """Get all nonprofits for a given location"""

    response_object = {
        'status': 'fail',
        'message': 'Invalid location id provided'
    }

    try:
        nonprofits = Nonprofit.query.filter_by(location_id=int(location_id)).all()

        response_object = {
            'status': 'success',
            'data': {
                'nonprofits': [nonprofit.to_json() for nonprofit in nonprofits]
            }
        }

        return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404

@nonprofits_blueprint.route('/location/city/<city>', methods=['GET'])
def get_nonprofits_by_city(city):
    """"Get all nonprofits in a city, state"""
    response_object = {
        'status': 'fail',
        'message': 'Invalid request'
    }

    try:
        location = Location.query.filter_by(name=str(city)).options(load_only("id")).one()
        nonprofits =  Nonprofit.query.filter_by(location_id=int(location.id)).all()
        response_object = {
            'status': 'success',
            'data': {
                'nonprofits': [nonprofit.to_json() for nonprofit in nonprofits]
            }
        }

        return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404
    except NoResultFound:
        response_object['message'] = 'No location was found for given city'
        return jsonify(response_object), 404

@nonprofits_blueprint.route('/location/state/<state>', methods=['GET'])
def get_nonprofits_by_state(state):
    """Get all nonprofits in a given state"""

    response_object = {
        'status': 'fail',
        'message': 'Invalid request'
    }

    try:
        location_ids = [loc.id for loc in Location.query.filter_by(state=str(state)).options(load_only('id')).all()]
        if len(location_ids) == 0:
            response_object = {
                'status': 'success',
                'data': {
                    'nonprofits': []
                }
            }
        else :
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
    """Get all nonprofits for a given location and category"""

    response_object = {
        'status': 'fail',
        'message': 'Invalid ids provided'
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
        if len(location_ids) == 0:
            response_object = {
                'status': 'success',
                'data': {
                    'nonprofits': []
                }
            }
        else:
            category = Category.query.filter_by(code=str(category)).one()
            if category == None:
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