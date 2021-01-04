from flask import render_template
from app import setup

@app.route("/index")
@app.route("/")
def index():
    return "ola"

