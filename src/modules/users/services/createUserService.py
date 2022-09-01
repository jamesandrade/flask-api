import cryptocode
from __main__ import app
from src.modules.users.models.user import User
from app import db
from sqlalchemy import exc

class CreateUserService():
    def execute(self, data):
        hashedPassword = cryptocode.encrypt(data.get('password'), "wow")
        data["password"] = hashedPassword
        try:
            newUser = User(**data)
            db.session.add(newUser)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
            return False
        
        userResponse = {
            'username':newUser.username,
            'email':newUser.email,
            'phone':newUser.phone,
        }

        return userResponse

createUserService = CreateUserService()
