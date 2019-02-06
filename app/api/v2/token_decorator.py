import datetime
import os
from functools import wraps

import jwt
from flask import jsonify, request

from app.api.v2.users.models import UserModel

secret = os.getenv('SECRET_KEY')

def require_token(f):
    @wraps(f)
    def secure(*args, ** kwargs):
        token = None

        if 'token' in request.headers:
            token = request.headers['token']
        if not token:
            
            return jsonify({
                "status":401,
                "message": "Token is missing"
            })

        try:
            data = jwt.decode(token, secret)
            current_user = UserModel().find_user_by_username(data['user_name'])

        except jwt.ExpiredSignatureError:
            return jsonify({
                "status":401,
                "message": "Token is exipired"
            })
        except jwt.InvalidTokenError:
            return jsonify({
                "status":401,
                "message": "Token is invalid"
            })
        return f(current_user, *args, **kwargs)
    return secure