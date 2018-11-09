# Import flask dependencies
from flask import Blueprint, request, jsonify

# Import the database object from the main app module
from npolinkapi import db
from sqlalchemy import inspect, or_
from sqlalchemy.orm import load_only
from sqlalchemy.orm.exc import NoResultFound

# Import module models (i.e. User)
from npolinkapi.api.models import Location, Category, Nonprofit

# Define the blueprint: 'auth', set its url prefix: app.url/auth
locations_blueprint = Blueprint('locations', __name__, url_prefix='/v1.0/locations')


# Set the route and accepted methods
@locations_blueprint.route('/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })

# route 'all', methods='GET'
@locations_blueprint.route('/all', methods=['GET'])
def get_all_locations():
    """Get all locations"""
    locations = Location.query.all()
    response_object = {
        'status': 'success',
        'data': {
            'locations' : [location.to_json() for location in locations]
        }
    }
    return jsonify(response_object), 200

@locations_blueprint.route('/<int:page>',methods=['GET'])
def view(page=1):
    """Get all locations paged"""
    per_page = 12

    search_key = request.args.get('search_key', 'name')
    if search_key == 'city':
        search_column = Location.city
    elif search_key == 'state':
        search_column = Location.state
    elif search_key == 'desc':
        search_column = Location.description
    else:
        search_column = Location.name

    sort_key = request.args.get('sort_key', 'name')
    if sort_key == 'city':
        sort_column = Location.city
    elif sort_key == 'state':
        sort_column = Location.state
    elif sort_key == 'id':
        sort_column = Location.id
    else:
        sort_column = Location.name

    searchword = request.args.get('q', '')
    if len(searchword) > 0:
        searchwordl = "{}%".format(searchword)
        searchwordm = "%{}%".format(searchword)
        searchwordr = "%{}".format(searchword)
        locations = Location.query.filter(or_(search_column.ilike(searchwordl),
                                              search_column.ilike(searchwordm),
                                              search_column.ilike(searchwordr)))
    else:
        searchword = "%"
        locations = Location.query.filter(search_column.like(searchword))

    sort = request.args.get('sort', 'asc')

    if sort == 'asc':
        locations = locations.order_by(sort_column.asc())
    else:
        locations = locations.order_by(sort_column.desc())

    locations = locations.paginate(page,per_page,error_out=False)

    paged_response_object = {
        'status': 'success',
        'data': {
            'locations': [location.to_json() for location in locations.items]
        },
        'has_next': locations.has_next,
        'has_prev': locations.has_prev,
        'next_page': locations.next_num,
        'pages': locations.pages
    }
    return jsonify(paged_response_object), 200

@locations_blueprint.route('/location/<id>', methods=['GET'])
def get_by_location_by_id(id):
    """Get a sigle location by id"""
    response_object = {
        'status': 'fail',
        'message': 'Invalid id provided'
    }

    try:
        location = Location.query.filter_by(id=int(id)).one()
        response_object = {
            'status': 'success',
            'data': {
                'location' : location.to_json()
            }
        }

        return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404
    except NoResultFound:
        response_object = {
            'status': 'fail',
            'message': 'No location for given id was found'
        }
        return jsonify(response_object), 404

# Get all locations which include NPOs of this category
# Will need this for category pages
@locations_blueprint.route('/category/<category_id>', methods=['GET'])
def get_location_by_category(category_id):
    """Get all locations for a category"""

    response_object = {
        'status': 'fail',
        'message': 'Invalid category id provided'
    }

    try:
        category = Category.query.filter_by(id=int(category_id)).options(load_only("location_list")).one()
        locations = Location.query.filter(Location.id.in_(category.location_list)).all()
        response_object = {
            'status': 'success',
            'data': {
                'locations': [location.to_json() for location in locations]
            }
        }

        return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404
    except NoResultFound:
        response_object['message'] = 'The category id provided does not exist'
        return jsonify(response_object), 404

# Will need this for category pages
@locations_blueprint.route('/category/code/<category_code>', methods=['GET'])
def get_location_by_category_code(category_code):
    response_object = {
        'status': 'fail',
        'message': 'Invalid category code'
    }

    try:
        category = Category.query.filter_by(code=str(category_code)).options(load_only("location_list")).one()
        locations = Location.query.filter(Location.id.in_(category.location_list)).all()
        response_object = {
            'status': 'success',
            'data': {
                'locations': [location.to_json() for location in locations]
            }
        }

        return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404
    except NoResultFound:
        response_object['message'] = 'The category code provided does not exist'
        return jsonify(response_object), 404

@locations_blueprint.route('/nonprofit/<nonprofit_id>', methods=['GET'])
def get_location_for_nonprofit(nonprofit_id):
    """Get location for a nonprofit"""

    response_object = {
        'status': 'fail',
        'message': 'Invalid nonprofit id provided'
    }

    try:
        nonprofit = Nonprofit.query.filter_by(id=int(nonprofit_id)).options(load_only("location_id")).one()
        location = Location.query.filter_by(id=nonprofit.location_id).one()
        response_object = {
            'status': 'success',
            'data': {
                'location': location.to_json()
            }
        }

        return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404
    except NoResultFound:
        response_object['message'] = 'The nonprofit id provided does not exist'
        return jsonify(response_object), 404


# Below are technically not specific to locations

# Return locations that have NPOs for a specific state?
# @locations_blueprint.route('/state/<id>', methods=['GET'])
# def get_locations_by_state(id):
#
# @locations_blueprint.route('/city/<id>', methods=['GET'])
# def get_locations_by_city(id):
