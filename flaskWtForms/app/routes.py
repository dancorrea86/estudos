from flask import (
    Flask,
    url_for,
    render_template,
    redirect
)
from app import app

from .forms import ContactForm



print ("ola")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "contact.jinja2",
        form=form,
        template="form-template"
    )

@app.route("/")
def home():
    return "ola"