from flaskModules import db
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))

    create_dttm = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    products = relationship("Product", secondary="orders")

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))

    create_dttm = db.Column(db.DateTime, default=datetime.utcnow)

    users = relationship("User", secondary="orders")

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    dttm = db.Column(db.DateTime, default=datetime.utcnow)

    user = relationship(User, backref=backref("orders", cascade="all, delete-orphan"))
    produtct = relationship(Product, backref("orders", cascade="all, delete-orphan"))