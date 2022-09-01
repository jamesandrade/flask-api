import cryptocode
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from __main__ import app
from src.modules.users.models.user import User
from app import db

class ShowUserService():
    def execute(self, data):
        user = User.query.filter_by(id=data).first()
        if user:
            userResponse = {
                            'username':user.username,
                            'email':user.email,
                            'phone':user.phone,
            }
        else:
            userResponse = []
        return userResponse
showUserService = ShowUserService()
