from flask_testing import TestCase

from npolinkapi import create_app, db
from npolinkapi.api.models import Nonprofit, Category, Location

app = create_app()

class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('npolinkapi.config.TestingConfig')
        return app

    def setUp(self):
        db.init_app(self.create_app())
        db.create_all()

        nonprofit = Nonprofit(id=1, name='nonprofit 2', description='nonprofit #1 description',
                              ein='123456789', logo='/logo1', address='123 nonprofit way',
                              location_id=1, category_id=1, projects=[])

        nonprofit2 = Nonprofit(id=2, name='nonprofit 1', description='nonprofit #2 description',
                              ein='123456790', logo='/logo2', address='456 nonprofit way',
                              location_id=1, category_id=2, projects=[])

        location = Location(id=1,name='Austin, TX', city='Austin', state='TX', description='Austin, TX',
                            image='/image', category_list=[1, 2], nonprofit_list=[1, 2])

        category = Category(id=1, name='category1', description='category #1', code='A', image='/image1',
                            parent_category='A', location_list=[1], nonprofit_list=[1])

        category2 = Category(id=2,name='category2', description='category #2', code='B', image='/image2',
                             parent_category='B', location_list=[1], nonprofit_list=[2])

        db.init_app(self.create_app())
        db.session.add(location)
        db.session.add(category)
        db.session.add(category2)
        db.session.add(nonprofit)
        db.session.add(nonprofit2)

        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
