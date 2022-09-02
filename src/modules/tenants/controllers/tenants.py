from src.utils.FormValidator import FormValidator
from flask import Flask, Response, make_response, jsonify
from src.modules.tenants.services.createTenantService import createTenantService
class TenantsController():
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