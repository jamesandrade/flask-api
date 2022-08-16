from __main__ import app
from flask import Flask, request, Response, make_response, jsonify
import json
from src.modules.users.services.authenticateUserService import authenticateUserService  



@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        content = request.json
        email = content.get('email')
        password = content.get('password')
        userResponse = authenticateUserService.execute(email=email, password=password)
        
        if userResponse:
            return make_response(jsonify(token=userResponse), 200)

        return Response(status=400)
