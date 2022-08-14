class Database():

    def init(app):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://docker:docker@localhost/flask-postgres'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False