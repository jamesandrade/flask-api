from __main__ import app
from flask import Flask, request, Response, make_response, jsonify
import json
from src.utils.FormValidator import FormValidator
from src.modules.users.services.authenticateUserService import authenticateUserService  

class UserLoginController():
    def post(data):
        validator = FormValidator.validator('email', 'password', data=data)
        if validator is False:
            return make_response({"message": "Request is missing arguments"}, 400)
        userResponse = authenticateUserService.execute(data)
        if userResponse is False:
            return make_response({"message":"Incorrect email or password"}, 401)
        
        return make_response(userResponse, 200)