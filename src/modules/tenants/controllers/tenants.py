from src.utils.FormValidator import FormValidator
from flask import Flask, Response, make_response, jsonify
from src.modules.tenants.services.createTenantService import createTenantService
from src.modules.tenants.services.showTenantService import showTenantService

class TenantsController():
    def get(data=None):
        if data is None:
            return make_response({"message": "Request is missing arguments"}, 400)
        showTenant = showTenantService.execute(data)

        return make_response(showTenant, 200)

    def post(data):
        validator = FormValidator.validator('corporate_name',
                                           'fantasy_name', 
                                           'cpnj',
                                           'email',
                                           'phone',
                                           'owner',
                                           'cpf_owner',
                                           'allowed',
                                            data=data
                                           )
        if validator is False:
            return make_response({"message": "Request is missing arguments"}, 400)
        createTenant = createTenantService.execute(data)
        if createTenant is False:
            return make_response({"message": "Error on Create Tenant"}, 400)

        return make_response(jsonify(createTenant), 200)