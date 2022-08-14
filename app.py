from flask import Flask
#from flask_restx import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import Column, Integer, String

from src.infra.orm.models import db
from database import Database

app = Flask(__name__)

Database.init(app)
db.init_app(app)
migrate = Migrate(app, db) 

#import all models
import src.modules.registerModels 

if __name__ == "__main__":
    CORS(app)
    #import all routes
    import src.modules.registerRoutes
    app.run(debug=True)
