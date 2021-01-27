from flask import Flask
from config import Config

# Create Flask's `app` object
app = Flask(__name__)
app.config.from_object(Config)

from app import routes