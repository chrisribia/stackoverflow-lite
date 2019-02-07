from flask import Blueprint
from flask_restful import Api

from app.api.v2.users.views import UserSignUp, UserSignIn
from app.api.v2.questions.views import Questions,squestion,delQuest,update_question
from app.api.v2.answers.views import Answer,singleAnswer,upDateSingleAnswer,answer_Accept,get_All_Answers


VERSION_DOS = Blueprint('apiv2', __name__, url_prefix='/api/v2')
API = Api(VERSION_DOS)

API.add_resource(UserSignUp, '/auth/signup')
API.add_resource(UserSignIn, '/auth/signin')
API.add_resource(Questions, '/questions')
API.add_resource(squestion, '/questions/<int:question_id>')
API.add_resource(delQuest, '/questions/<int:question_id>')
API.add_resource(Answer, '/questions/<int:question_id>/answer')
API.add_resource(get_All_Answers, '/answers')
API.add_resource(singleAnswer, '/answers/<int:answer_id>')
API.add_resource(upDateSingleAnswer, '/answers/<int:answer_id>/answer')
API.add_resource(answer_Accept, '/answers/<int:answer_id>/user_preferred')


 