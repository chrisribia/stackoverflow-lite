from flask import jsonify, make_response, request
from flask_restful import Resource

from .models import QuestionModel

class Quest(Resource):
    """docstring for Quest class"""

    def __init__(self):
        """initiliase the Quest class"""
        self.db = QuestionModel()

    def post(self):
        """docstring for saving a Quest"""
        question_id = self.db.save()
      
        return make_response(jsonify({
            "status": 201,
            "data": {
                "id": question_id,
                "message": "question added"
            }
        }), 201)

    
    def get(self):
        """docstring for getting all the questions posted"""
        self.db.get_all()
        return make_response(jsonify({
            "status": 200,
            "data": self.db.get_all()
        }), 200)

class Quests(Resource):
    """docstring of a single question"""
    def __init__(self):
        """initiliase the questionModel class"""
        self.db = QuestionModel()

    def get(self, question_id):

        """docstring for getting a specific red-flag"""
        specificQuest = self.db.find(question_id)
        if specificQuest == "red flag does not exit":
               return make_response(jsonify({
                    "status": 404,
                    "error": "question does not exit"
                }), 404)
       
        return make_response(jsonify({
            "status": 200,
            "data": specificQuest
        }), 200)
