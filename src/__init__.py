from flask import Flask
from flask_cors import CORS

from src.routes.root import mod as root_mod
from src.routes.images import mod as images_mod


# We want to be flexible with regards to trailing slashes
class RelaxedFlask(Flask):

    def add_url_rule(self, *args, **kwargs):
        if 'strict_slashes' not in kwargs:
            kwargs['strict_slashes'] = False
        super(RelaxedFlask, self).add_url_rule(*args, **kwargs)


def create_flask_app():
    app = RelaxedFlask(__name__)
    app.config['CORS_HEADERS'] = 'Content-Type'
    CORS(app)

    app.register_blueprint(root_mod, url_prefix="/")
    app.register_blueprint(images_mod, url_prefix="/images")

    return app
