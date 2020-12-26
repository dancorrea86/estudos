from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

app =  Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'login.db')
app.config['SECRET_KEY'] = 'thisissecret'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    user = User.query.filter_by(username='Anthony').first()
    login_user(user)
    return 'You are now logged in!'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return "You are now logged out"

@app.route('/home')
@login_required
def home():
    return "The corrent user is " + current_user.username

if __name__ == '__main__':
    app.run(debug=True)

    