# Import flask dependencies
from flask import Blueprint, request, jsonify

# Import the database object from the main app module
from npolinkapi import db
from sqlalchemy import inspect
from sqlalchemy.orm import load_only
from sqlalchemy.orm.exc import NoResultFound

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
    """Get all categories"""
    categories = Category.query.all()
    response_object = {
        'status': 'success',
        'data': {
            'categories' : [cat.to_json() for cat in categories]
        }
    }
    return jsonify(response_object), 200

@categories_blueprint.route('/<int:page>',methods=['GET'])
def view(page=1):
    """Get all categories paged"""
    per_page = 12
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
    """Get a category by it"""
    response_object = {
        'status': 'fail',
        'message': 'Invalid id provided'
    }

    try:
        category = Category.query.filter_by(id=int(id)).one()
        response_object = {
            'status': 'success',
            'data': {
                'category' : category.to_json()
            }
        }

        return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404
    except NoResultFound:
        response_object['message'] = 'No category found for given id'
        return jsonify(response_object), 404

@categories_blueprint.route('/location/<location_id>', methods=['GET'])
def get_category_by_location(location_id):
    """Get categories by location"""

    response_object = {
        'status': 'fail',
        'message': 'Location id invalid'
    }

    try:
        location = Location.query.filter_by(id=int(location_id)).options(load_only("category_list")).one()
        categories = Category.query.filter(Category.id.in_(location.category_list)).all()
        response_object = {
            'status': 'success',
            'data': {
                'categories': [category.to_json() for category in categories]
            }
        }

        return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404
    except NoResultFound:
        response_object['message'] = 'No location found for given location id'
        return jsonify(response_object), 404
