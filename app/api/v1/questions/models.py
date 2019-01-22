import datetime
from flask import jsonify, make_response, request
from flask_restful import Resource

questions = []


class QuestionModel():
    """Class with methods to perform CRUD operations on the DB"""

    def __init__(self):
        self.db = questions
        if len(questions) == 0:
            self.id = 1
        else:
            self.id = questions[-1]['id'] + 1
        self.id = len(questions) + 1

    def save(self):
        
        data = {
            'id': self.id,
            'title': request.json.get('title'),
            'question':request.json.get('question'),
            'dateposted': datetime.datetime.utcnow()             
        }
        self.db.append(data)
        return self.id

    
    def get_all(self):
        return self.db

    def find(self, question_id):
        for question in self.db:
            if question['id'] == question_id:
                return question

        return "red flag does not exit"
