import cryptocode

from __main__ import app
from src.modules.users.models.user import User
from app import db

class ShowUserService():
    def execute(self, user_id):
        try:
            user = User.query.filter_by(id=user_id).first()
        except:
            return False

        userResponse = {
                        'username':user.username,
                        'email':user.email,
                        'phone':user.phone
                    }

        return userResponse
        
showUserService = ShowUserService()
