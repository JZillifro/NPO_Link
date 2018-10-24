import json
import unittest

from npolinkapi.tests.base import BaseTestCase


class TestNonprofitService(BaseTestCase):
    """Tests for the Users Service."""

    def test_nonprofits(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/nonprofits/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])


if __name__ == '__main__':
    unittest.main()
