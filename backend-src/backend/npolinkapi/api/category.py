# Import flask dependencies
from flask import Blueprint, request, jsonify

# Import the database object from the main app module
from npolinkapi import db
from sqlalchemy import inspect, or_
from sqlalchemy.orm import load_only
from sqlalchemy.orm.exc import NoResultFound

import json

# Import module models (i.e. User)
from npolinkapi.api.models import Category, Nonprofit, Location

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

@categories_blueprint.route('/search/<int:page>', methods=['GET'])
def search(page=1):
    search_words = request.args.get("search_words", '').split(' ')
    #nonzero query length
    if len(search_words):
        try:
            #for all query terms search name, descrption and address
            categories = Category.query.filter(or_(
                *[Category.name.ilike('%' + str(x) + '%') for x in search_words],
                *[Category.code.ilike('%'+str(x)+ '%') for x in search_words],
                *[Category.description.ilike('%'+str(x)+ '%') for x in search_words]
            ))
        except Exception as e:
            return str(e)
        #output formatting
        categories = categories.paginate(page,3,error_out=False)

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
    return "error, no args"


@categories_blueprint.route('/<int:page>',methods=['GET'])
def view(page=1):
    """Get all categories paged"""
    per_page = 12

    search_key = request.args.get('search_key', 'name')
    if search_key == 'name':
        search_column = Category.name
    elif search_key == 'code':
        search_column = Category.code
    elif search_key == 'parent':
        search_column = Category.parent_category
    elif search_key == 'desc':
        search_column = Category.description
    else:
        search_column = Category.name

    sort_key = request.args.get('sort_key', 'name')
    if sort_key == 'code':
        sort_column = Category.code
    elif sort_key == 'id':
        sort_column = Category.id
    else:
        sort_column = Category.name

    searchword = request.args.get('q', '')
    if len(searchword) > 0:
        searchwordl = "{}%".format(searchword)
        searchwordm = "%{}%".format(searchword)
        searchwordr = "%{}".format(searchword)
        categories = Category.query.filter(or_(search_column.ilike(searchwordl),
                                              search_column.ilike(searchwordm),
                                              search_column.ilike(searchwordr)))
    else:
        searchword = "%"
        categories = Category.query.filter(search_column.like(searchword))

    sort = request.args.get('sort', 'asc')

    if sort == 'asc':
        categories = categories.order_by(sort_column.asc())
    else:
        categories = categories.order_by(sort_column.desc())

    categories = categories.paginate(page,per_page,error_out=False)

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

@categories_blueprint.route('/nonprofit/<nonprofit_id>', methods=['GET'])
def get_category_for_nonprofit(nonprofit_id):
    """Get category for a nonprofit"""

    response_object = {
        'status': 'fail',
        'message': 'Invalid nonprofit id provided'
    }

    try:
        nonprofit = Nonprofit.query.filter_by(id=int(nonprofit_id)).options(load_only("category_id")).one()
        category = Category.query.filter_by(id=nonprofit.category_id).one()
        response_object = {
            'status': 'success',
            'data': {
                'category': category.to_json()
            }
        }

        return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404
    except NoResultFound:
        response_object['message'] = 'The nonprofit id provided does not exist'
        return jsonify(response_object), 404
