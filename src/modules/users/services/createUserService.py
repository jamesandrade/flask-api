import cryptocode

from __main__ import app
from src.modules.users.models.user import User
from app import db

class CreateUserService():
    def execute(self, username, email, phone, password):
        try:

            hashedPassword = cryptocode.encrypt(password, "wow")
            newUser = User(username=username,
                           email=email,
                           phone=phone,
                           password=hashedPassword
                           )

            db.session.add(newUser)
            db.session.commit()

        except:
            return False
        
        userResponse = {
            'username':newUser.username,
            'email':newUser.email,
            'phone':newUser.phone,
        }

        return userResponse

createUserService = CreateUserService()
