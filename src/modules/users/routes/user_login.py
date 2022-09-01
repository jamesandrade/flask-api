from __main__ import app
from flask import Flask, request, Response, make_response, jsonify
from src.modules.users.controllers.user_login import UserLoginController
class UserLoginRoute():
    @app.route('/login', methods=['POST'])
    def userLoginRoute():   
        res = UserLoginController.post(request.json)
        return res