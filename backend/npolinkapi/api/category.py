# Import flask dependencies
from flask import Blueprint, request, jsonify

# Import the database object from the main app module
from npolinkapi import db
from sqlalchemy import inspect
from sqlalchemy.orm import load_only

import json

# Import module models (i.e. User)
from npolinkapi.api.models import Category, Location

# Define the blueprint: 'auth', set its url prefix: app.url/auth
categories_blueprint = Blueprint('categories', __name__, url_prefix='/v1.0/categories')

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

@categories_blueprint.route('/<int:page>',methods=['GET'])
def view(page=1):
    per_page = 16
    categories = Category.query.order_by(Category.id.asc()).paginate(page,per_page,error_out=False)
    paged_response_object = {
        'status': 'success',
        'data': {
            'categories': [category.to_json() for category in categories.items]
        },
        'has_next': categories.has_next,
        'has_prev': categories.has_prev,
        'next_page': categories.next_num,
        'pages': categories.pages
    }
    return jsonify(paged_response_object), 200


@categories_blueprint.route('/category/<id>', methods=['GET'])
def get_by_id(id):
    return jsonify( [cat.to_json() for cat in Category.query.filter_by(id=id)])
    response_object = {
        'status': 'fail',
        'message': 'No location for given id'
    }

    try:
        category = Location.query.filter_by(id=int(id)).one()
        if not category:
            response_object = {
                'status': 'fail',
                'message': 'No category for given id'
            }
            return jsonify(response_object), 404
        else:
            response_object = {
                'status': 'success',
                'data': {
                    'category' : category.to_json()
                }
            }

            return jsonify(response_object), 200

    except ValueError:
        return jsonify(response_object), 404

@categories_blueprint.route('/location/<location_id>', methods=['GET'])
def get_category_by_location(location_id):
    response_object = {
        'status': 'fail',
        'message': 'Location id invalid'
    }

    try:
        location = Location.query.filter_by(id=int(location_id)).options(load_only("category_list")).one()

        if not location:
            response_object['message'] = 'Invalid location'
            return jsonify(response_object), 404
        else:
            category_ids = location.to_json()['categories']
            if len(category_ids) == 0:
                response_object = {
                    'status': 'success',
                    'data': {
                        'categories': []
                    }
                }
            else:
                categories = Category.query.filter(Category.id.in_(category_ids)).all()
                response_object = {
                    'status': 'success',
                    'data': {
                        'categories': [category.to_json() for category in categories]
                    }
                }

        return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404
