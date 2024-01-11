from src.api.v1.user.route import user as user_v1
from src.api.v1.auth.route import auth as auth_v1


def register_blueprints(app):
    # Register your blueprints here
    app.register_blueprint(user_v1, url_prefix='/api/v1/user')
    app.register_blueprint(auth_v1, url_prefix='/api/v1/auth')
