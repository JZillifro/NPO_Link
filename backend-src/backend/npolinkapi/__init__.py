import os

from flask import Flask  # new
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


# instantiate the db
db = SQLAlchemy()


# new
def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)
    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # register blueprints
    from npolinkapi.api.location import locations_blueprint
    from npolinkapi.api.category import categories_blueprint
    from npolinkapi.api.nonprofit import nonprofits_blueprint
    # Register blueprint(s)
    app.register_blueprint(locations_blueprint)
    app.register_blueprint(categories_blueprint)
    app.register_blueprint(nonprofits_blueprint)

    @app.route("/")
    def greet():
        #insert any documenation/behaviour for interaction with api at default endpoint here
        return "Welcome to the NPO link api <Placeholder> <Placeholder> <Placeholder>\n"
    
    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
