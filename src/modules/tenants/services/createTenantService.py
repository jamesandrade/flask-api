import cryptocode
from __main__ import app
from src.modules.tenants.models.tenant import Tenant
from app import db
from sqlalchemy import exc

class CreateTenantService():
    def execute(self, data):
        try:
            newTenant = Tenant(**data)
            db.session.add(newTenant)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
            return False

        return data

createTenantService = CreateTenantService()
