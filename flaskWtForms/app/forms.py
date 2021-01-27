"""Form object declaration."""
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length


class ContactForm(FlaskForm):
    """Contact form."""
    name = StringField('Name',[DataRequired()])
    email = StringField('Email', [DataRequired()])
    body = TextField('Message', [DataRequired()])

    submit = SubmitField('Submit')