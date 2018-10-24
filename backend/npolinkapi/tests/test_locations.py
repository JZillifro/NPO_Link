import json
import unittest

from npolinkapi.tests.base import BaseTestCase


class TestLocationService(BaseTestCase):
    """Tests for the Location Service."""

    def test_locations(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/locations/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])


if __name__ == '__main__':
    unittest.main()
