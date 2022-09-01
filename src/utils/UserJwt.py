from flask_jwt_extended import verify_jwt_in_request, get_jwt
from flask import request
class UserJwt():
    def getId():
        verify_jwt_in_request()
        user = get_jwt()
        user_id = user["sub"]
        return user_id