from __main__ import app
from flask import Flask, request, jsonify, Response
import json
import jwt
import cryptocode
from cryptography.hazmat.primitives import serialization
from src.modules.users.models.user import User
from app import db


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        content = request.json
        email = content.get('email')
        password = content.get('password')

        user = User.query.filter_by(email=email).first()
        
        if user is None:
            return Response(status=400)

        if cryptocode.decrypt(user.password, "wow") != password:
            return Response(status=400)
        
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
        return jsonify(token=token)
