import json
import unittest

from npolinkapi.tests.base import BaseTestCase


class TestLocationService(BaseTestCase):
    """Tests for the Location Service."""

    def test_locations(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/v1.0/locations/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

    def test_get_all_locations(self):
        """Ensure the /locations/all route behaves correctly."""
        response = self.client.get('/v1.0/locations/all')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        locations = data['data']['locations']
        self.assertEqual(1, len(locations))

    def test_get_all_locations_paged(self):
        """Ensure the /locations/<page_id> route behaves correctly."""
        response = self.client.get('/v1.0/locations/1')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        locations = data['data']['locations']
        self.assertEqual(1, len(locations))
        self.assertEqual(1, data['pages'])
        self.assertFalse(data['has_next'])
        self.assertFalse(data['has_prev'])

    def test_get_all_locations_paged_no_data(self):
        """Ensure the /locations/<page_id> route behaves correctly with bad input"""
        response = self.client.get('/v1.0/locations/2')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        locations = data['data']['locations']
        self.assertEqual(0, len(locations))
        self.assertEqual(1, data['pages'])
        self.assertTrue(data['has_prev'])
        self.assertFalse(data['has_next'])

    def test_get_location(self):
        """Ensure the /locations/location/<location_id> route behaves correctly."""
        response = self.client.get('/v1.0/locations/location/1')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        location = data['data']['location']
        self.assertEqual(1, location['id'])

    def test_get_location_bad_input(self):
        """ Ensure the /locations/location/<location_id> route behaves correctly on
            bad user input.
        """
        response = self.client.get('/v1.0/locations/location/badid')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)
        self.assertEqual('fail',data['status'])

    def test_get_location_not_found(self):
        """ Ensure the /locations/location/<location_id> route behaves correctly on
            bad user input when not found.
        """
        response = self.client.get('/v1.0/locations/location/100')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)
        self.assertEqual('fail',data['status'])

    def test_get_location_by_category_id(self):
        """Ensure the /locations/category/<category_id> route behaves correctly."""
        response = self.client.get('/v1.0/locations/category/1')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        locations = data['data']['locations']
        self.assertEqual(1, len(locations))
        self.assertEqual(1, locations[0]['id'])

    def test_get_location_by_category_code(self):
        """Ensure the /locations/category/code/<category_code> route behaves correctly."""
        response = self.client.get('/v1.0/locations/category/code/B')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('success',data['status'])
        locations = data['data']['locations']
        self.assertEqual(1, len(locations))
        self.assertEqual(1, locations[0]['id'])


if __name__ == '__main__':
    unittest.main()
