import json
import unittest

from flask.cli import FlaskGroup

from npolinkapi import create_app, db   # new
from npolinkapi.api.models import Category, Location, Nonprofit

app = create_app()  # new
cli = FlaskGroup(create_app=create_app)  # new


@cli.command()
def seed_db():
    """Seeds the database."""
    with open('files/data/loc-results.json') as json_data:
        data = json.load(json_data)
        for location in data:
            exists = Location.query.filter_by(id=location['id']).first()
            if not exists:
                nonprofits = location['nonprofits']
                categories = location['categories']
                loc = Location(id=location['id'],name=location['name'], city=location['city'],
                               state=location['state'], description=location['description'],
                               image=location['image'], category_list=categories, nonprofit_list=nonprofits)

                db.session.add(loc)
                db.session.commit()

        db.session.flush()

    with open('files/data/cat-results.json') as json_data:
        data = json.load(json_data)
        for category in data:
            exists = Category.query.filter_by(id=category['id']).first()
            if not exists:
                nonprofits = category['nonprofits']
                locations = category['locations']
                cat = Category(id=category['id'],name=category['title'], description=category['description'],
                               code=category['code'], image=category['image'], parent_category=category['parent_code'],
                               location_list=locations, nonprofit_list=nonprofits)
                db.session.add(cat)
                db.session.commit()

        db.session.flush()

    with open('files/data/org-results.json') as json_data:
        data = json.load(json_data)
        for nonprofit in data:
            exists = Nonprofit.query.filter_by(id=nonprofit['id']).first()
            if not exists:
                org = Nonprofit(id=nonprofit['id'],name=nonprofit['name'], description=nonprofit['description'],
                                ein=nonprofit['ein'], logo=nonprofit['logo'], address=nonprofit['address'],
                                location_id=nonprofit['location_id'], category_id=nonprofit['category_id'],
                                projects=nonprofit['projects'])

                db.session.add(org)
                db.session.commit()

        db.session.flush()


@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def test():
    """ Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('npolinkapi/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    cli()
