from flask import Flask
#from flask_restx import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import Column, Integer, String

from src.infra.orm.models import db
from src.infra.DatabaseConfig import DatabaseConfig
from src.infra.JwtConfig import JwtConfig
from flask_jwt_extended import JWTManager

app = Flask(__name__)

DatabaseConfig.init(app)
db.init_app(app)
migrate = Migrate(app, db) 
JwtConfig.init(app)
jwt = JWTManager(app)
#import all models
import src.modules.registerModels 

if __name__ == "__main__":
    
    
    CORS(app)
    #import all routes
    import src.modules.registerRoutes
    app.run(debug=True)
