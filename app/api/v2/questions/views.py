"""Views for posting questions"""
from flask import jsonify, request
from flask_restful import Resource
from app.api.v2.questions.modules import QuestionsModel,singleQuestion
from app.api.v2.token_decorator import require_token
from app.api.v2.users.models import UserModel


class Questions(Resource):
    """This class deals with posting and reading questions"""

    def __init__(self):
        """
        executes when the class is being initiated
        used to assign values to object properties
        self parameter is a reference to tha class instance itself & is used 
        to access variables that belong to that class
        """
        self.db = QuestionsModel()
    @require_token
    def post(current_user, self):
        """method for posting a question"""
        question = self.db.save(current_user['user_id'])
        return jsonify({
            "status": 201,
            "data": question,
            "message": "Created a question _"+str(current_user['password'])
        })

    @require_token
    def get(current_user, self):
        """method for getting all the questions posted by users"""
        questions = self.db.find_all()
        return jsonify({
            "status": 200,
            "data": questions
            }) 
class squestion(Resource):
    def __init__(self):
        self.db = singleQuestion()

    @require_token
    def get(current_user,self,question_id):
        """method to find a single question"""
        """ owner=self.db.find_question_owner(question_id)
        if owner != current_user['user_id']:
            return jsonify({
                "status":400,
                "message":"you have no authority to view the question"
            }) """
        question=self.db.find_single_question(question_id)
        return jsonify({
            "status":200,
            "data":question
        })

   
class delQuest(Resource):
    def __init__(self):
        self.my = singleQuestion()
        
    @require_token
    def delete(current_user,self,question_id):
        """method to delete a single question"""
        question = self.my.dequestion(question_id)
        return jsonify({
            "status":200,
            "data":question
        })
class update_question(Resource):
    def __init__(self):
        self.db = singleQuestion()
    @require_token
    def patch(current_user,self,question_id):
        question = self.db.update_question(question_id)
        return jsonify({
            "status":200,
            "data":question

        })