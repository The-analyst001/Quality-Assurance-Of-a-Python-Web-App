# test_app.py
import unittest
from app import app # this permits us to import the app object from the instruction flake8 app.py


class TestApp(unittest.TestCase): # defines a new class that inherits from the unittest
    def setUp(self): # this is a stars of setup method which is a special method in the unittest that is run before each test method in the class 
        self.app = app.test_client() #This method defines a test method that start with the word test

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello level 400 FET, Quality Assurance!"}) 


if __name__ == '__main__':
    unittest.main()