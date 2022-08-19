#get, post, put, patch, delete
from __main__ import app
from flask import Flask, request, jsonify, Response
import json
from flask_jwt_extended import jwt_required

from src.middlewares.login import me_required
from src.modules.users.services.createUserService import createUserService  
from src.modules.users.services.showUserService import showUserService  
from src.modules.users.services.destroyUserService import destroyUserService  

@app.route('/user/<user_id>', methods=['GET', 'DELETE'])
@jwt_required()
@me_required()
def getOrDelete(user_id):
    if request.method == 'GET':
        userResponse = showUserService.execute(user_id)
        if userResponse:
            return json.dumps(userResponse)

        return Response(status=400)

    else:
        res = destroyUserService.execute(user_id)
        if res:
            return Response(status=200)
        else:
            return Response(status=400)

@app.route('/user', methods=['POST', 'PUT','PATCH', 'DELETE'])
def user():
    if request.method == 'POST':
        content = request.json
        username = content.get('username')
        email = content.get('email')
        phone = content.get('phone')
        password = content.get('password')

        newUser = createUserService.execute(username=username,
                                            email=email,
                                            phone=phone,
                                            password=password
                                            )

        if newUser:
            return json.dumps(newUser)

        return Response(status=400)
