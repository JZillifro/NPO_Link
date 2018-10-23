from npolinkapi import app, db
from npolinkapi.location.models import Location
from npolinkapi.category.models import Category
from npolinkapi.nonprofit.models import Nonprofit
import click
from flask.cli import FlaskGroup


cli = FlaskGroup(app)

@cli.command()
def seed_db():
    """Seeds the database."""
    with open('files/data/loc-results.json') as json_data:
        data = json.load(json_data)
        for location in data:
            exists = Location.query.filter_by(id=location['id']).first()
            if not exists:
                loc = Location(id=location['id'],name=location['name'], city=location['city'], state=location['state'], description=location['description'], image=location['image'])
                db.session.add(loc)
                db.session.commit()

        db.session.flush()

    with open('files/data/cat-results.json') as json_data:
        data = json.load(json_data)
        for category in data:
            exists = Category.query.filter_by(id=category['id']).first()
            if not exists:
                cat = Category(id=category['id'],name=category['title'], description=location['description'], code=category['code'], image=category['image'], parent_category=category['parent_code'])
                db.session.add(cat)
                db.session.commit()

        db.session.flush()

    with open('files/data/org-results.json') as json_data:
        data = json.load(json_data)
        for nonprofit in data:
            exists = Nonprofit.query.filter_by(id=nonprofit['id']).first()
            if not exists:
                org = Nonprofit(id=nonprofit['id'],name=nonprofit['name'], description=nonprofit['description'], ein=nonprofit['ein'], logo=nonprofit['logo'], address=nonprofit['address'], location_id=nonprofit['location_id'], category_id=nonprofit['category_id'])
                db.session.add(org)
                db.session.commit()

        db.session.flush()

@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()
