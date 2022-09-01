from __main__ import app
from flask import Flask, request, jsonify, Response
from flask_jwt_extended import jwt_required
from src.modules.users.controllers.user import UsersController
from src.utils.UserJwt import UserJwt
class UsersRoute():
    @app.route('/user', methods=['GET'])
    @jwt_required()
    def usersGetRoute():  
        user_id = UserJwt.getId()
        res = UsersController.get(user_id)
        return res

    @app.route('/user', methods=['POST'])
    def usersPostRoute():
        res = UsersController.post(request.json)
        return res

    @app.route('/user', methods=['DELETE'])
    @jwt_required()
    def usersDeleteRoute():
        user_id = UserJwt.getId()
        res = UsersController.delete(data=request.json, user_id=user_id)
        return res