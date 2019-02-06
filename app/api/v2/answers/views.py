"""Views for posting questions"""
from flask import jsonify, request
from flask_restful import Resource

from app.api.v2.token_decorator import require_token
from app.api.v2.answers.models import answerModel
from app.api.v2.users.models import UserModel
from app.api.v2.questions.modules import QuestionsModel


class Answer(Resource):
    """This class deals with answing question"""

    def __init__(self):
        """
        executes when the class is being initiated
        used to assign values to object properties
        self parameter is a reference to tha class instance itself & is used 
        to access variables that belong to that class
        """
        self.db = answerModel()

    @require_token
    def post(current_user, self,question_id):
        """method for posting a question"""
        self.verify = QuestionsModel().find_question_by_id(question_id)
        if self.verify == None:
            return jsonify({
                "status": 404,
                "message":"question id does not exists"
            })
        question = self.db.save(current_user['user_id'],question_id)
        return jsonify({
            "status": 201,
            "data": question,
            "message": "Created a question"
        })


    @require_token
    def get(current_user, self):
        """method for getting all the answers"""
        answ = self.db.find_all()
        return jsonify({
            "status": 200,
            "data": answ
            }) 
   
class get_All_Answers(Resource):
    def __init__(self):
        self.db = answerModel()
    @require_token
    def get(current_user,self):
        """method to get all answers from database"""
        answers = self.db.find_all()
        return jsonify({
            "status":200,
            "message" : answers
        })

class singleAnswer(Resource):
    def __init__(self):
        self.db = answerModel()
    @require_token
    def get(current_user,self,answer_id):
        """method fot getting single answer"""
        answer = self.db.find_Answer_by_id(answer_id)
        return jsonify({
            "status" : 200,
            "data" : answer
        })


class upDateSingleAnswer(Resource):
    def __init__(self):
        self.db = answerModel()
    @require_token
    def patch(current_user,self,answer_id):
        """method for updating a single amswer"""
        answer = self.db.update_My_Answer(answer_id)
        return jsonify({
            "status" : 200,
            "data" : answer
        })
class answer_Accept(Resource):
    def __init__(self):
        self.db = answerModel()
    @require_token
    def patch(current_user,self,answer_id):
        results=self.db.accept_Answer(answer_id)
        return jsonify({
            "status":200,
            "message":results
        })
