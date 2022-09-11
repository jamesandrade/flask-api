from __main__ import app
from flask import Flask, request
from flask_jwt_extended import jwt_required
from src.modules.tenants.controllers.tenants import TenantsController
from src.utils.UserJwt import UserJwt
class TenantsRoute():
    @app.route('/tenants/<id>', methods=['GET'])
    @jwt_required()
    def tenantsGetRoute(id):  
        res = TenantsController.get(id)
        return res

    @app.route('/tenants', methods=['POST'])
    def tenantsPostRoute():
        res = TenantsController.post(request.json)
        return res
