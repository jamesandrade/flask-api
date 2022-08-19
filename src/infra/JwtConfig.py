class JwtConfig():

    def init(app):
        app.config["JWT_SECRET_KEY"] = "super-secret"
