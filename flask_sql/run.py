from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialization of Flask
app = Flask(__name__)

# Configuration Flask SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    
    def __repr__(self):
        return '<User %r %r>' % (self.id, self.username)