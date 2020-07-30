from django.test import TestCase, Client
from .models     import User
import json

class UserTest(TestCase):
    def setUp(self):
        client = Client()
    
    def tearDown(self):
        User.objects.all().delete()

    def test_signup_textcase(self):

        user = {
            'name': '호근님',
            'email': 'ddee@gmail.com',
            'contact': '01012341234',
            'password': '12345'
        }

        response = self.client.post('/user/signup', json.dumps(user), content_type= "application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'SUCCESS'})
