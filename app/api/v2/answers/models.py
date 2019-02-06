"""mdules for questions"""
import re

import psycopg2.extras
from flask import request
from flask_restful import reqparse

from app.api.db_config import DATABASE_URL as url
from app.api.db_config import connection
from app.api.validator import parser

result=[]

def non_existance_of_question():
    return "question id does not exists"

class answerModel:
    """Class with methods to perform CRUD operations on the DB"""

    def __init__(self):
        self.db = connection(url)  
        self.bank=result


    def save(self, user_id,question_id):
        #parser.parse_args()
        data = {
            'question_id': question_id,
            'user_id': user_id,
            'answer': request.json.get('answer')         
            
         }

        query = """INSERT INTO answers (question_id,user_id, answer) VALUES({0},{1},'{2}');""".format(
             data['question_id'], data['user_id'], data['answer'])
        conn = self.db
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        return data

    def find_all(self):
        """method to find all questions"""
        query = """SELECT answer_id,user_preferred,question_id from answers"""
        conn = self.db
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        answers = cursor.fetchall()
        return answers

    def find_Answer_by_id(self,answer_id):
        """method to find all questions"""
        query = """SELECT answer_id, answer,question_id,user_preferred from answers where answer_id={0}""".format(answer_id)
        conn = self.db
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        answer = cursor.fetchone()
        if not answer:
            return non_existance_of_question()
        return answer

    def update_My_Answer(self,answer_id):
        """method to find all questions""" 
          
        new_Answer=request.json.get('answer')    
        query = """UPDATE answers set answer='{0}' where answer_id={1}""".format(new_Answer,answer_id)
        conn = self.db
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()       
        return "updated"
    def accept_Answer(self,answer_id):
        """method to accept answer"""
        user_preferred=True
        query = """SELECT question_id from answers where answer_id={0}""".format(answer_id)
        conn = self.db
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchone()
        if results == None:
            return non_existance_of_question()
        else:
            question_id=results[0]
            query = """SELECT * from answers where user_preferred = '{0}' and  question_id = {1}""".format(user_preferred,question_id)
            conn = self.db
            cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) 
            cursor.execute(query)
            allQ = cursor.fetchone()

            self.status1="false"
            self.status2="true"
            if allQ != None:
                querry1 = """UPDATE answers SET user_preferred='{0}' WHERE question_id = {1}""".format(self.status1,question_id)
                con = self.db
                cursor = con.cursor()
                cursor.execute(querry1)
                con.commit()
            else:
                querry1 = """UPDATE answers SET user_preferred='{0}' WHERE answer_id = {1}""".format(self.status2,answer_id)
                con = self.db
                cursor = con.cursor()
                cursor.execute(querry1)
                con.commit()
        return "task complete"
