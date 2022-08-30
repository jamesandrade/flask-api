class DatabaseConfig():

    def init(app):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://userx:passw@postgres/appdb'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False