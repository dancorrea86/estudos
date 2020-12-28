from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user
from app import app, db, login_manager

from app.models.tables import User
from app.models.forms import LoginForm
from app import login_manager

@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        print(user)
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("index"))
            flash("Logged in")
        else: 
            flash("Invalid login")
    return render_template('login.html',
                            form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out")
    return redirect(url_for("index"))


# @app.route("/teste/<info>")
# @app.route("/teste", defaults={"info": None})
# def teste(info):
#     i = User("dancorre2", "1234d5d", "Daniel", "dan@gmail.com")
#     db. session.add(i)
#     db.session.commit()
#     return "Ok"

# @app.route("/teste/<info>")
# @app.route("/teste", defaults={"info": None})
# def teste(info):
#     r = User.query.filter_by(password="1234d5d").first()
#     print (r.username, r.name)
#     return "Ok"

# @app.route("/teste/<info>")
# @app.route("/teste", defaults={"info": None})
# def teste(info):
#     r = User.query.filter_by(username="dancorrea86").first()
#     r.username = "dancorrea"
#     db. session.add(r)
#     db.session.commit()
#     return "Ok"

@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
    r = User.query.filter_by(username="dancorrea").first()
    db. session.delete(r)
    db.session.commit()
    return "Ok"