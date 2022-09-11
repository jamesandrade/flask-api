import cryptocode
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from flask import Flask, jsonify
from flask_serialize import FlaskSerialize
from __main__ import app
from src.modules.tenants.models.tenant import Tenant
from app import db

class ShowTenantService():
    def execute(self, data):
        tenant = Tenant.query.filter_by(id=data).first()
         
        return jsonify(tenant.as_dict())

showTenantService = ShowTenantService()
