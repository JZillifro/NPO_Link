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
@categories_blueprint.route('/all', methods=['GET'])
def get_all():
    return jsonify([cat.to_json() for cat in Category.query.all()])

@categories_blueprint.route('/<id>', methods=['GET'])
def get_by_id(id):
    return jsonify( [cat.to_json() for cat in Category.query.filter_by(code=id)])

@categories_blueprint.rout('/npos/<category_id>', methods=['GET'])
def get_npos_by_location(category_id):
    npos = Category.query.filter_by(id=category_id).options(load_only("npo_ids")).one().to_json()['npo_ids']

    npo_id_list = json.loads(npos)

    npo_list = Nonprofit.query.filter(Nonprofit.id.in_(npo_id_list)).all()

    return jsonify(npo.to_json() for npo in npo_list)
