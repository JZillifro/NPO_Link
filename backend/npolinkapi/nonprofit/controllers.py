# Import flask dependencies
from flask import Blueprint, request, jsonify

# Import the database object from the main app module
from npolinkapi import db
from sqlalchemy import inspect

# Import module models (i.e. User)
from npolinkapi.nonprofit.models import Nonprofit

# Define the blueprint: 'auth', set its url prefix: app.url/auth
nonprofits_blueprint = Blueprint('nonprofits', __name__, url_prefix='/nonprofits')

# Set the route and accepted methods
@nonprofits_blueprint.route('/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
