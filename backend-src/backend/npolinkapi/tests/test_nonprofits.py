import json
import unittest

from npolinkapi.tests.base import BaseTestCase

class TestNonprofitService(BaseTestCase):
    """Tests for the Nonprofit API endpoints."""

    def test_nonprofits(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/v1.0/nonprofits/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

    def test_get_all_nonprofits(self):
        """Ensure the /nonprofits/all route behaves correctly."""
        response = self.client.get('/v1.0/nonprofits/all')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        nonprofits = data['data']['nonprofits']
        self.assertEqual(2, len(nonprofits))

    def test_get_all_nonprofits_paged(self):
        """Ensure the /nonprofits/<page_id> route behaves correctly."""
        response = self.client.get('/v1.0/nonprofits/1')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        nonprofits = data['data']['nonprofits']
        self.assertEqual(2, len(nonprofits))
        self.assertEqual(1, data['pages'])
        self.assertFalse(data['has_next'])
        self.assertFalse(data['has_prev'])

    def test_get_all_nonprofits_paged_no_data(self):
        """Ensure the /nonprofits/<page_id> route behaves correctly with bad input"""
        response = self.client.get('/v1.0/nonprofits/2')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        nonprofits = data['data']['nonprofits']
        self.assertEqual(0, len(nonprofits))
        self.assertEqual(1, data['pages'])
        self.assertTrue(data['has_prev'])
        self.assertFalse(data['has_next'])

    def test_get_nonprofit(self):
        """Ensure the /nonprofits/nonprofit/<nonprofit_id> route behaves correctly."""
        response = self.client.get('/v1.0/nonprofits/nonprofit/1')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        nonprofit = data['data']['nonprofit']
        self.assertEqual(1, nonprofit['id'])

    def test_search_nonprofit(self):
        """Ensure the /nonprofits/search/?search_words=words route behaves."""
        query = "help" 
        response = self.client.get('/v1.0/nonprofits/search/1?search_words=' + query)
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        nonprofits = data['data']['nonprofits']
        #searches name, address, description
        for nonprofit in nonprofits:
            self.assertEqual(query in nonprofit['name'] 
            or query in nonprofit['address']
            or query in nonprofit['description'],
            True
            )
    
    def test_search_nonprofit_filter(self):
        """Ensure the /nonprofits/search/?filters={} route behaves."""
        #Fiters by state(foreign key) and number of projects("Range")
        response = self.client.get('/v1.0/nonprofits/search/1?filters={"Range":6}')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        nonprofits = data['data']['nonprofits']
        for nonprofit in nonprofits:
            self.assertGreaterEqual(len(nonprofit["projects"]),6)
 

    def test_get_nonprofit_bad_input(self):
        """ Ensure the /nonprofits/nonprofit/<nonprofit_id> route behaves correctly on
            bad user input.
        """
        response = self.client.get('/v1.0/nonprofits/nonprofit/badid')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)
        self.assertEqual('fail',data['status'])

    def test_get_nonprofit_not_found(self):
        """ Ensure the /nonprofits/nonprofit/<nonprofit_id> route behaves correctly on
            bad user input when not found.
        """
        response = self.client.get('/v1.0/nonprofits/nonprofit/100')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)
        self.assertEqual('fail',data['status'])

    def test_get_nonprofit_by_category_id(self):
        """Ensure the /nonprofits/category/<category_id> route behaves correctly."""
        response = self.client.get('/v1.0/nonprofits/category/1')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        nonprofits = data['data']['nonprofits']
        self.assertEqual(1, len(nonprofits))
        self.assertEqual(1, nonprofits[0]['id'])

    def test_get_nonprofit_by_location_id(self):
        """Ensure the /nonprofits/location/<location_id> route behaves correctly."""
        response = self.client.get('/v1.0/nonprofits/location/1')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        nonprofits = data['data']['nonprofits']
        self.assertEqual(2, len(nonprofits))
        self.assertEqual(1, nonprofits[0]['id'])
        self.assertEqual(2, nonprofits[1]['id'])

    def test_get_nonprofit_by_city(self):
        """Ensure the /nonprofits/location/city/<city> route behaves correctly."""
        response = self.client.get('/v1.0/nonprofits/location/city/Austin, TX')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        nonprofits = data['data']['nonprofits']
        self.assertEqual(2, len(nonprofits))
        self.assertEqual(1, nonprofits[0]['id'])

    def test_get_nonprofit_by_city_not_found(self):
        """ Ensure the /nonprofits/location/city/<city> route behaves correctly on
            city not found.
        """
        response = self.client.get('/v1.0/nonprofits/location/city/testnotfound, test')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)
        self.assertEqual('fail',data['status'])
        self.assertEqual('No location was found for given city', data['message'])


    def test_get_nonprofit_by_state(self):
        """Ensure the /nonprofits/location/state/<state> route behaves correctly."""
        response = self.client.get('/v1.0/nonprofits/location/state/TX')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        nonprofits = data['data']['nonprofits']
        self.assertEqual(2, len(nonprofits))
        self.assertEqual(1, nonprofits[0]['id'])
        self.assertEqual(2, nonprofits[1]['id'])

    def test_get_nonprofit_by_state_not_found(self):
        """ Ensure the /nonprofits/location/state/<state> route behaves correctly on
            city not found.
        """
        response = self.client.get('/v1.0/nonprofits/location/state/teststatenotfound')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        nonprofits = data['data']['nonprofits']
        self.assertEqual(0, len(nonprofits))

    def test_get_nonprofit_by_location_and_category(self):
        """ Ensure the /location/<location_id>/category/<category_id> route behaves correctly."""
        response = self.client.get('/v1.0/nonprofits/location/1/category/1')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        nonprofits = data['data']['nonprofits']
        self.assertEqual(1, len(nonprofits))
        self.assertEqual(1, nonprofits[0]['id'])

    def test_get_nonprofit_by_state_and_category(self):
        """ Ensure the /location/state/<state>/category/code/<category_code> route behaves correctly."""
        response = self.client.get('/v1.0/nonprofits/location/state/TX/category/code/A')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        nonprofits = data['data']['nonprofits']
        self.assertEqual(1, len(nonprofits))
        self.assertEqual(1, nonprofits[0]['id'])


if __name__ == '__main__':
    unittest.main()
