"""mdules for questions"""
import re

import psycopg2.extras
from flask import request
from flask_restful import reqparse

from app.api.db_config import DATABASE_URL as url
from app.api.db_config import connection
from app.api.validator import parser


class QuestionsModel:
    """Class with methods to perform CRUD operations on the DB"""

    def __init__(self):
        self.db = connection(url)

    def save(self, user_id):
       # parser.parse_args()
        data = {
            'user_id': user_id,
            'title': request.json.get('title'),
            'description': request.json.get('description')
        }

        query = """INSERT INTO questions (user_id,title, description) VALUES({0},'{1}','{2}');""".format(
             data['user_id'], data['title'], data['description'])
        conn = self.db
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        return data

    def find_all(self):
        """method to find all questions"""
        query = """SELECT * from questions"""
        conn = self.db
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        questions = cursor.fetchall()
        return questions

    def find_question_by_id(self,question_id):
        """method to find all questions"""
        query = """SELECT * from questions where question_id={}""".format(question_id)
        conn = self.db
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        questions = cursor.fetchone()
        if not questions:
            return None
        return questions

   
class singleQuestion:
    def __init__(self):
        self.db=connection(url)
    def find_single_question(self,quest):
        """method to a get single question"""
        query = """SELECT * from questions where question_id = {}""".format(quest)
        conn = self.db
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        question = cursor.fetchall()
        return question
        
    def find_question_owner(self,quest):
        """method to a get  question owner"""
        query = """SELECT user_id from questions where question_id = {}""".format(quest)
        conn = self.db
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        question = cursor.fetchone()
        return question['user_id']
        
    def dequestion(self,quest):
        """method to delete single question"""
        query="""DELETE  from questions where question_id ={}""".format(quest)
        query1="""DELETE  from answers where question_id ={}""".format(quest)

        queries = [query,query1]
        for q in queries:
            conn = self.db
            cursor = conn.cursor()
            cursor.execute(q)    
            conn.commit()   
        return "deleted"

    def update_question(self,question_id):
        """update a single question"""
        description=request.json.get('description')
        query ="""UPDATE questions  SET description='{0}' WHERE question_id={1}""".format(
            description,question_id )
        conn = self.db
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        return "updated"

  
    


    