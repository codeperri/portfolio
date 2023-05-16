import unittest
from flask import Flask
from api_implementation.api import ShoppingStatisticsAPI, get_statistics


class ShoppingStatisticsAPITest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_get_statistics_with_category(self):
        with self.app.test_request_context('/api/v1/shopping/statistics?category=Food', method='GET'):
            api = ShoppingStatisticsAPI()
            response = api.get_statistics()
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            self.assertIn('data', data)
            self.assertIn('Food', data['data'])
            self.assertIsInstance(data['data']['Food'], float)

    def test_get_statistics_without_category(self):
        with self.app.test_request_context('/api/v1/shopping/statistics', method='GET'):
            api = ShoppingStatisticsAPI()
            response = api.get_statistics()
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            self.assertIn('data', data)
            self.assertIsInstance(data['data'], dict)

    def test_get_statistics_invalid_category(self):
        with self.app.test_client() as client:
            response = client.get('/api/v1/shopping/statistics?category=InvalidCategory')
            self.assertEqual(response.status_code, 404)

    def test_get_statistics_function(self):
        with self.app.test_request_context('/api/v1/shopping/statistics', method='GET'):
            response = get_statistics()
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            self.assertIn('data', data)
            self.assertIsInstance(data['data'], dict)

if __name__ == '__main__':
    unittest.main()
