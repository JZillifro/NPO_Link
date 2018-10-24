# Import flask dependencies
from flask import Blueprint, request, jsonify

# Import the database object from the main app module
from npolinkapi import db
from sqlalchemy import inspect

# Import module models (i.e. nonprofit)
from npolinkapi.api.models import Nonprofit

# Define the blueprint: 'auth', set its url prefix: app.url/auth
nonprofits_blueprint = Blueprint('nonprofits', __name__, url_prefix='/nonprofits')

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
    response_object = {
        'status': 'success',
        'data': {
            'nonprofits': [nonprofit.to_json() for nonprofit in Nonprofit.query.all()]
        }
    }
    return jsonify(response_object), 200

@nonprofits_blueprint.route('/<nonprofit_id>', methods=['GET'])
def get_nonprofit_by_id(nonprofit_id):
    """Get single nonprofit details"""
    response_object = {
        'status': 'fail',
        'message': 'Nonprofit does not exist'
    }
    try:
        nonprofit = Nonprofit.query.filter_by(id=int(nonprofit_id)).first()
        if not nonprofit:
            return jsonify(response_object), 404
        else:
            response_object = {
                'status': 'success',
                'data': nonprofit.to_json()
            }
            return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404
