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

        """docstring for getting a specific question"""
        specificQuest = self.db.find(question_id)
        if specificQuest == "question does not exist":
               return make_response(jsonify({
                    "status": 404,
                    "error": "question does not exist"
                }), 404)
       
        return make_response(jsonify({
            "status": 200,
            "data": specificQuest
        }), 200)

    def delete(self, question_id):
        """docstring for deleting a question"""
        incident = self.db.find(question_id)
        if incident == "question does not exist":
            return make_response(jsonify({
                "status": 404,
                "error": "question does not exist"
            }), 404)
        delete_status = self.db.delete(incident)
        if delete_status == "deleted":
            return make_response(jsonify({
                "status": 200,
                "data": 'question  has been deleted'
        }), 200)



        

class UpdateTitle(Resource):
    """class to update question title"""

    def __init__(self):
        self.db = QuestionModel()

    def patch(self, question_id):
        """method to update question's title"""
        question = self.db.find(question_id)

        if question == "question does not exist":
            return  make_response(jsonify({
                "status": 404,
                "error": "question does not exist"
            }), 404)
        edit_status = self.db.edit_question_title(question)
        if edit_status == "updated":
            return jsonify({
                "status": 200,
                "data": {
                    "id": question_id,
                    "message": "Updated question's title"
                }
               })

class UpdateQuestion(Resource):
    """class to update question title"""

    def __init__(self):
        self.db = QuestionModel()

    def patch(self, question_id):
        """method to update question"""
        question = self.db.find(question_id)

        if question == "question does not exist":
            return  make_response(jsonify({
                "status": 404,
                "error": "question does not exist"
            }), 404)
        edit_status = self.db.edit_quest(question)
        if edit_status == "updated":
            return jsonify({
                "status": 200,
                "data": {
                    "id": question_id,
                    "message": "Updated question"
                }
               })
