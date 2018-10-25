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


if __name__ == '__main__':
    unittest.main()
