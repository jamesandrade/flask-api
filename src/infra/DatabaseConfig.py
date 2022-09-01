class DatabaseConfig():

    def init(app):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://docker:docker@localhost:5432/flask-postgres'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False