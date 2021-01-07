from flask import render_template
from setup import app

@app.route("/index")
@app.route("/")
def index():
    return "ola"

