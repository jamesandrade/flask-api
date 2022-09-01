import cryptocode

from __main__ import app
from src.modules.users.models.user import User
from app import db

class DestroyUserService():
    def execute(self, data, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user is None:
           return False
        if cryptocode.decrypt(user.password, "wow") != data["password"]:
            return False
        db.session.delete(user)
        db.session.commit()

        return True

destroyUserService = DestroyUserService()
