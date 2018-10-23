import os
# Import flask and template operators
from flask import Flask, redirect, session, render_template
from flask.cli import FlaskGroup

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from npolinkapi.location.controllers import locations_blueprint
from npolinkapi.category.controllers import categories_blueprint
from npolinkapi.nonprofit.controllers import nonprofits_blueprint

# Register blueprint(s)
app.register_blueprint(locations_blueprint)
app.register_blueprint(categories_blueprint)
app.register_blueprint(nonprofits_blueprint)
