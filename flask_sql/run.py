from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialization of Flask
app = Flask(__name__)

# Configuration Flask SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

books = db.Table('tags',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    tags = db.relationship('Book', secondary=tags, lazy='subquery',
        backref=db.backref('users', lazy=True))
    
    def __repr__(self):
        return '<User %r %r>' % (self.id, self.username)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    author = db.Column(db.String(30))
    
    def __repr__(self):
        return '<Book %r %r>' % (self.id, self.title)
