from flask import Blueprint
from flask_restful import Api


from .questions.views import  Quest,Quests,UpdateTitle,UpdateQuestion
VERSION_ONE = Blueprint('api', __name__, url_prefix='/api/v1')
API = Api(VERSION_ONE)
API.add_resource(Quest, '/questions')
API.add_resource(Quests, '/questions/<int:question_id>')
API.add_resource(UpdateTitle, '/questions/<int:question_id>/title')
API.add_resource(UpdateQuestion, '/questions/<int:question_id>/question')

