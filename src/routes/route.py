from ..api.v1.user.endpoints import user as user_v1


def register_blueprints(app):
    # Register your blueprints here
    app.register_blueprint(user_v1, url_prefix='/api/v1/user')
