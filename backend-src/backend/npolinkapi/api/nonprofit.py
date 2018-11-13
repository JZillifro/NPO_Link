# Import flask dependencies
from flask import Blueprint, request, jsonify


# Import the database object from the main app module
from npolinkapi import db
from sqlalchemy import inspect, and_, or_
from sqlalchemy.orm import load_only
from sqlalchemy.orm.exc import NoResultFound

# Import module models (i.e. nonprofit)
from npolinkapi.api.models import Nonprofit, Location, Category

import json
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

@nonprofits_blueprint.route('/search/<int:page>', methods=['GET'])
def search(page=1):
    #Parse args
    search_words,filters = request.args.get("search_words", default=None), request.args.get("filters", default = "{}")
    try:
        if search_words is not None:
            search_words = search_words.split(" ")
        filters = json.loads(filters)
    except Exception as e:
        return "Error parsing args" + str(e)

    try:
        nonprofit_search_queries = True
        if search_words is not None and len(search_words):
            #for all query terms search name, descrption and address
            nonprofit_search_queries = or_(
            *[Nonprofit.name.ilike('%' + str(x) + '%') for x in search_words],
            *[Nonprofit.name.ilike(      str(x) + '%') for x in search_words],
            *[Nonprofit.name.ilike('%' + str(x)      ) for x in search_words],

            *[Nonprofit.address.ilike('%' + str(x) + '%') for x in search_words],
            *[Nonprofit.address.ilike(      str(x) + '%') for x in search_words],
            *[Nonprofit.address.ilike('%' + str(x)      ) for x in search_words],

            *[Nonprofit.description.ilike('%' + str(x) + '%') for x in search_words],
            *[Nonprofit.description.ilike(      str(x) + '%') for x in search_words],
            *[Nonprofit.description.ilike('%' + str(x)      ) for x in search_words]

             )
        nonprofit_filters = True
        if filters is not None and len(filters):
            filter_queries = []
            #Filter by all provided filters
            #Filters are State, Range
            if "State" in filters:
                filter_queries.append(Location.state.like(filters["State"]))
            if "Range" in filters:
                filter_queries.append(Nonprofit.num_projects.isnot(None))

            nonprofit_filters = and_(*filter_queries)
    except Exception as e:
        return "Error in constructing queries" + str(e)
        
    try:
        #Apply queries
        nonprofits = Nonprofit.query.filter(and_(nonprofit_filters,nonprofit_search_queries ))
        sort = request.args.get('sort', 'asc')

        if sort == 'asc':
            nonprofits = nonprofits.order_by(Nonprofit.name.asc())
        else:
            nonprofits = nonprofits.order_by(Nonprofit.name.desc())


    except Exception as e:
        return "Error in applying queries" + str(e)

    #output formatting
    try:
        nonprofits = nonprofits.paginate(page,3,error_out=False)
    except Exception as e:
        return "Error in paginating" + str(e)

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

@nonprofits_blueprint.route('/<int:page>',methods=['GET'])
def view(page=1):
    """Get all nonprofits paged"""
    per_page = 12

    search_key = request.args.get('search_key', 'name')
    if search_key == 'name':
        search_column = Nonprofit.name
    elif search_key == 'ein':
        search_column = Nonprofit.ein
    elif search_key == 'desc':
        search_column = Nonprofit.description
    else:
        search_column = Nonprofit.name

    sort_key = request.args.get('sort_key', 'name')
    if sort_key == 'ein':
        sort_column = Nonprofit.ein
    elif sort_key == 'id':
        sort_column = Nonprofit.id
    else:
        sort_column = Nonprofit.name

    searchword = request.args.get('q', '')
    if len(searchword) > 0:
        searchwordl = "{}%".format(searchword)
        searchwordm = "%{}%".format(searchword)
        searchwordr = "%{}".format(searchword)
        nonprofits = Nonprofit.query.filter(or_(search_column.ilike(searchwordl),
                                              search_column.ilike(searchwordm),
                                              search_column.ilike(searchwordr)))
    else:
        searchword = "%"
        nonprofits = Nonprofit.query.filter(search_column.like(searchword))

    sort = request.args.get('sort', 'asc')

    if sort == 'asc':
        nonprofits = nonprofits.order_by(sort_column.asc())
    else:
        nonprofits = nonprofits.order_by(sort_column.desc())

    nonprofits = nonprofits.paginate(page,per_page,error_out=False)

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
