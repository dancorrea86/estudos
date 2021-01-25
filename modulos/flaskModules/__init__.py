from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Call the Flask in the application
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Configuration Flask SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# Run the application

from flaskModules.models import tables 