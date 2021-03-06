# Import flask dependencies
from flask import Blueprint, request, jsonify

# Import the database object from the main app module
from npolinkapi import db
from sqlalchemy import inspect, or_, and_
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
    #Parse args
    search_words,filters = request.args.get("search_words", default=None), request.args.get("filters", default = "{}")
    search_key = request.args.get('search_key', default = None)
    try:
        if search_words is not None:
            search_words = search_words.split(" ")
        filters = json.loads(filters)
    except Exception as e:
        return "Error parsing args" + str(e)

    try:
        #default values to search for
        category_search_queries = True
        attributes_to_search = [Category.name, Category.code, Category.description]
        #Any search terms given
        if search_words is not None and len(search_words):
            #Search all available attributes
            if search_key is None:
                #construct queries
                #for all query terms search name, descrption and address
                category_search_queries = or_(
                    *[attr.ilike('%' + str(x) + '%') for x in search_words for attr in attributes_to_search],
                    *[attr.ilike(      str(x) + '%') for x in search_words for attr in attributes_to_search],
                    *[attr.ilike('%' + str(x)      ) for x in search_words for attr in attributes_to_search]

                )
            #Search only one attribute
            else:
                #Determine the attribute to search
                #Default to name
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
                #Constrcut queries for attribute to search
                category_search_queries = or_(
                *[search_column.ilike('%' + str(x) + '%') for x in search_words],
                *[search_column.ilike(      str(x) + '%') for x in search_words],
                *[search_column.ilike('%' + str(x)      ) for x in search_words]
                )


        category_filters = True
        #If a filter is specified
        if filters is not None and len(filters):
            filter_queries = []
            #Filter by all provided filters
            if "Parent_code" in filters:
                filter_queries.append(Category.parent_category.like(filters["Parent_code"]))
            if "Has_nonprofits" in filters:
                if filters["Has_nonprofits"]:
                    filter_queries.append(Category.nonprofit_amount >= filters["Has_nonprofits"])
                else:
                    filter_queries.append(Category.nonprofit_amount <= filters["Has_nonprofits"])

            category_filters = and_(*filter_queries)
    except Exception as e:
        return "Error in constructing queries" + str(e)

    try:
        #Apply queries
        categories = Category.query.filter(and_(category_filters,category_search_queries))
        #Determine arguments for sorting
        sort = request.args.get('sort', 'asc')
        sort_key = request.args.get('sort_key', 'name')
        #Determine attribute to sort by
        if sort_key == 'code':
            sort_column = Category.code
        elif sort_key == 'id':
            sort_column = Category.id
        else:
            sort_column = Category.name

        #Determine and apply sorting method
        if sort == 'asc':
            categories = categories.order_by(sort_column.asc())
        else:
            categories = categories.order_by(sort_column.desc())


    except Exception as e:
        return "Error in applying queries" + str(e)

    #output formatting
    try:
        page_size = int(request.args.get("page_size", default=3))
        categories = categories.paginate(page,page_size,error_out=False)
    except Exception as e:
        return "Error in paginating" + str(e)

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
