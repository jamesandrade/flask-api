from flask import Flask, Response, make_response, jsonify
from src.utils.FormValidator import FormValidator
from src.modules.users.services.createUserService import createUserService  
from src.modules.users.services.showUserService import showUserService  
from src.modules.users.services.destroyUserService import destroyUserService
class UsersController():
    def get(data):
        if data is None:
            return make_response({"message": "Request is missing arguments"}, 400)
        showUser = showUserService.execute(data)

        return make_response(showUser, 200)

    def post(data):
        validator = FormValidator.validator('username', 'email', 'phone', 'password', data=data)
        if validator is False:
            return make_response({"message": "Request is missing arguments"}, 400)
        createUser = createUserService.execute(data)
        if createUser is False:
            return make_response({"message": "User user already exists"}, 401)

        return make_response(jsonify(createUser), 200)
    
    def delete(data, user_id):       
        validator = FormValidator.validator('password', data=data)
        if validator is False:
            return make_response({"message": "Request is missing arguments"}, 400)
        if user_id is None:
            return make_response({"message": "Request is missing arguments"}, 400)
        deleteUser = destroyUserService.execute(data=data, user_id=user_id)
        if deleteUser is False:
            return make_response({"message": "Incorrect password or User does not Exists!"}, 401)

        return make_response({"message": "Success!"}, 200)