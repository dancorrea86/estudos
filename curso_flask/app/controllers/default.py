from flask import render_template
from app import app, db

from app.models.tables import User
from app.models.forms import LoginForm

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    else:
        print(form.errors)
    return render_template('login.html',
                            form=form)

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