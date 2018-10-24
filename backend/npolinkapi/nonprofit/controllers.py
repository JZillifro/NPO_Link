# Import flask dependencies
from flask import Blueprint, request, jsonify

# Import the database object from the main app module
from npolinkapi import db
from sqlalchemy import inspect

# Import module models (i.e. User)
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
def get_all():
    nonprofits = Nonprofit.query.all()
    if not nonprofits:
        return jsonify({"result": "no results"})

    return jsonify([nonprofit.to_json() for nonprofit in nonprofits])
