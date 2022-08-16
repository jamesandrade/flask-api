import cryptocode
from cryptography.hazmat.primitives import serialization

import jwt
from app import db

from __main__ import app
from src.modules.users.models.user import User
from app import db

class AuthenticateUserService():
    def execute(self, email, password):
        try:
            user = User.query.filter_by(email=email).first()

            if user is None:
                print("aqui")
                return False

            if cryptocode.decrypt(user.password, "wow") != password:
                print("aq2")
                return False

            ## JWT 
            payload_data = {
                "sub": str(user.id),
                "username": user.username,
            }

            private_key = open('gen', 'r').read()
            key = serialization.load_ssh_private_key(private_key.encode(), password=b'flask-api')

            token = jwt.encode(
                                payload=payload_data,
                                key=key,
                                algorithm='RS256'
                              )
        except:
            return False

        return token

authenticateUserService = AuthenticateUserService()
