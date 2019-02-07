import datetime
import json
import os
import unittest

import jwt

from ... import create_app
from app.api.db_config import create_tables, super_user, destroy_tables
from app.tests.v2.test_data import test_user,answer_data, question_data

secret = os.getenv('SECRET_KEY')

class QuestionsTestCase(unittest.TestCase):
    """
    This class represents the questions test cases
    """

    def setUp(self):
        APP = create_app(config_name="testing")
        APP.testing = True
        self.app = APP.test_client()
        create_tables()
        super_user()

        self.test_user = test_user

        payload = {
            "user_name": self.test_user['user_name'],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
        }

        token = jwt.encode(
            payload=payload, key=secret, algorithm='HS256')

        self.headers = {'Content-Type': 'application/json',
                        'token': token
                        }

        self.headers_invalid = {
            'Content-Type': 'application/json', 'token': 'Tokenmbaya'}
        self.answer = answer_data
        self.question = question_data
      
        
    def test_post_answer(self):
        """Test post  question"""
        self.app.post("/api/v2/questions", headers=self.headers,
                      data=json.dumps(self.question))        
        response = self.app.post(
            "/api/v2/questions/1/answer", headers=self.headers, data=json.dumps(self.answer))
        json.loads(response.data)
        self.assertEqual(response.status_code, 200)

        
    def test_post_question(self):
        """Test post a question"""
        response = self.app.post(
            "/api/v2/questions", headers=self.headers, data=json.dumps(self.question))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['status'], 201)
    def test_answers(self):
        """Test get all answers"""
        self.app.post("/api/v2/answers", headers=self.headers,
                      data=json.dumps(self.question))        
        response = self.app.get(
            "/api/v2/answers", headers=self.headers, data=json.dumps(self.answer))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['status'], 200)

    def test_single_answer(self):
        """Test get all single"""
        self.app.post("/api/v2/answers/1", headers=self.headers,
                      data=json.dumps(self.answer))        
        response = self.app.get(
            "/api/v2/answers/1", headers=self.headers, data=json.dumps(self.answer))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['status'], 200)

    def test_update_answer(self):
        """Test get all single"""
        self.app.post("/api/v2/answers/1/answer", headers=self.headers,
                      data=json.dumps(self.answer))        
        response = self.app.patch(
            "/api/v2/answers/1/answer", headers=self.headers, data=json.dumps(self.answer))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['status'], 200)

    def test_accept_answer(self):
        """Test get all single"""
        self.app.post("/api/v2/answers/1/user_preferred", headers=self.headers,
                      data=json.dumps(self.answer))        
        response = self.app.patch(
            "/api/v2/answers/1/user_preferred", headers=self.headers, data=json.dumps(self.answer))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['status'], 200)
    
    def tearDown(self):
        destroy_tables()   


 

 
  