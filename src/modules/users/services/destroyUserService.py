import cryptocode

from __main__ import app
from src.modules.users.models.user import User
from app import db

class DestroyUserService():
    def execute(self, user_id):
        try:
            user = User.query.filter_by(id=user_id).first()
            db.session.delete(user)
            db.session.commit()

        except:
            return False

        return True

destroyUserService = DestroyUserService()
