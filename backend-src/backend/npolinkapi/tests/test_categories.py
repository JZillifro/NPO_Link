import json
import unittest

from npolinkapi.tests.base import BaseTestCase


class TestCategoryService(BaseTestCase):
    """Tests for the Category Service."""

    def test_categories(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/v1.0/categories/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

    def test_get_all_categories(self):
        """Ensure the /categories/all route behaves correctly."""
        response = self.client.get('/v1.0/categories/all')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        categories = data['data']['categories']
        self.assertEqual(2, len(categories))

    def test_get_all_categories_paged(self):
        """Ensure the /categories/<page_id> route behaves correctly."""
        response = self.client.get('/v1.0/categories/1')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        categories = data['data']['categories']
        self.assertEqual(2, len(categories))
        self.assertEqual(1, data['pages'])
        self.assertFalse(data['has_next'])
        self.assertFalse(data['has_prev'])

    def test_get_all_categories_paged_no_data(self):
        """Ensure the /categories/<page_id> route behaves correctly with bad input"""
        response = self.client.get('/v1.0/categories/2')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        categories = data['data']['categories']
        self.assertEqual(0, len(categories))
        self.assertEqual(1, data['pages'])
        self.assertTrue(data['has_prev'])
        self.assertFalse(data['has_next'])

    def test_get_all_categories_paged_badinput(self):
        """Ensure the /categories/<page_id> route behaves correctly with invalid user input"""
        response = self.client.get('/v1.0/categories/badid')
        self.assertEqual(response.status_code, 404)

    def test_get_category(self):
        """Ensure the /categories/category/<category_id> route behaves correctly."""
        response = self.client.get('/v1.0/categories/category/1')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        category = data['data']['category']
        self.assertEqual(1, category['id'])

    def test_search_category(self):
        """Ensure the /categories/search/?search_words=words route behaves."""
        query = "dog"
        response = self.client.get('/v1.0/categories/search/1?search_words=' + query)
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        categories = data['data']['categories']
        #searches name, code, description
        for category in categories:
            self.assertEqual(query in category['name'] 
            or query in category['code'] 
            or query in category['description'],
            True
            )
    
    def test_search_category_filter(self):
        """Ensure the /categories/search/?filters={} route behaves."""
        response = self.client.get('/v1.0/categories/search/1?filters={"Parent_code":"A"}')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        categories = data['data']['categories']
        for category in categories:
            self.assertEqual(category["parent_category"],"A")
 


    def test_get_category_bad_input(self):
        """ Ensure the /categories/category/<category_id> route behaves correctly on
            bad user input.
        """
        response = self.client.get('/v1.0/categories/category/badid')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)
        self.assertEqual('fail',data['status'])

    def test_get_category_not_found(self):
        """ Ensure the /categories/category/<category_id> route behaves correctly on
            bad user input when not found.
        """
        response = self.client.get('/v1.0/categories/category/100')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)
        self.assertEqual('fail',data['status'])

    def test_get_category_by_location_id(self):
        """Ensure the /categories/location/<location_id> route behaves correctly."""
        response = self.client.get('/v1.0/categories/location/1')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        categories = data['data']['categories']
        self.assertEqual(2, len(categories))
        self.assertEqual(1, categories[0]['id'])
        self.assertEqual(2, categories[1]['id'])

    def test_get_category_by_location_id_badinput(self):
        """Ensure the /categories/location/<location_id> route behaves correctly with invalid user input"""
        response = self.client.get('/v1.0/categories/location/badid')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
