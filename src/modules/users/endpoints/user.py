#get, post, put, patch, delete
from __main__ import app
from flask import Flask, request, jsonify, Response
import json

from src.modules.users.models.user import User
from app import db
import cryptocode

#feat: login required for this
@app.route('/user/<user_id>', methods=['GET', 'DELETE'])
def getOrDelete(user_id):
    if request.method == 'GET':
        user = User.query.filter_by(id=user_id).first()
    
        userResponse = {
                    'username':user.username,
                    'email':user.email,
                    'phone':user.phone
                    }

        userResponse = json.dumps(userResponse)
        return userResponse
    else:
        try:
            user = User.query.filter_by(id=user_id).first()
            db.session.delete(user)
            db.session.commit()
            return Response(status=200)
        except:
            return Response(status=400)

@app.route('/user', methods=['POST', 'PUT','PATCH', 'DELETE'])
def user():
    #feat: construct function, verify if alread Exists
    if request.method == 'POST':
        content = request.json
        username = content.get('username')
        email = content.get('email')
        phone = content.get('phone')
        password = content.get('password')

        hashedPassword = cryptocode.encrypt(password, "wow")
        newUser = User(username=username,
                  email=email,
                  phone=phone,
                  password=hashedPassword)
        db.session.add(newUser)
        db.session.commit()

        return jsonify(request.json)
    