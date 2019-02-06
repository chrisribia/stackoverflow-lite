import datetime
from flask import jsonify, make_response, request
from flask_restful import Resource

from app.api.validator import parser,parser_edit_question,parser_edit_title

questions = []


class QuestionModel():
    """Class with methods to perform CRUD operations on the DB"""

    def __init__(self):
        self.db = questions
        if len(self.db)  == 0:
            self.id = 1
        else: 
            self.id = len(self.db)+1

        

    def save(self):
        parser.parse_args()        
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

        return "question does not exist"

    def delete(self, question):
        self.db.remove(question)
        return "deleted"

    def edit_question(self, question):
        "Method to edit a question"
        question['question'] = request.json.get('question')
        return "updated"
        
    def edit_question_title(self, question):
        "Method to edit a questions title"
        parser_edit_title.parse_args()
        question['title'] = request.json.get('title')
        return "updated"
    def edit_quest(self, question):
        "Method to edit a question"
        parser_edit_question.parse_args()
        question['question'] = request.json.get('question')
        return "updated"