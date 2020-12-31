from flask import render_template
from ./ import app

@app.route("/index")
@app.route("/")
def index():
    return "ola"

