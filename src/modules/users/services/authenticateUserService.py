import cryptocode
from cryptography.hazmat.primitives import serialization
from datetime import timedelta
from __main__ import app

from flask import jsonify
from src.modules.users.models.user import User

from app import db
from flask_jwt_extended import create_access_token
class AuthenticateUserService():
    def execute(self, email, password):
        user = User.query.filter_by(email=email).first()

        if user is None:
           return False

        if cryptocode.decrypt(user.password, "wow") != password:
            return False

        access_token = create_access_token(identity=user.id,
                                           expires_delta= timedelta(days=15)
                                           )
        
        return jsonify(token=access_token)

authenticateUserService = AuthenticateUserService()
