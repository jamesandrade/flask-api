from __main__ import app
from flask import Flask, request
from src.modules.tenants.controllers.tenants import TenantsController
from src.utils.UserJwt import UserJwt
class TenantsRoute():
    @app.route('/tenants', methods=['POST'])
    def tenantsPostRoute():
        res = TenantsController.post(request.json)
        return res
