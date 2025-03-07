import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client()

    def test_home_route(self):
        response = self.tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), "Hello, CI/CD!")

    def test_status_route(self):
        response = self.tester.get('/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), "App is running!")

if __name__ == "__main__":
    unittest.main()
