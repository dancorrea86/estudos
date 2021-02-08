from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/page/<string:user>')
def page(user):
    return 'User: ' + user

