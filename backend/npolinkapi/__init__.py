# Import flask and template operators
from flask import Flask, redirect, session, render_template

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from npolinkapi.location.controllers import mod_location as location_module
from npolinkapi.category.controllers import mod_category as category_module
from npolinkapi.nonprofit.controllers import mod_nonprofit as nonprofit_module

# Register blueprint(s)
app.register_blueprint(location_module)
app.register_blueprint(category_module)
app.register_blueprint(nonprofit_module)



# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
