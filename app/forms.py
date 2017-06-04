from flask_wtf import Form
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class UrlForm(Form):
    url = StringField('URL:', validators=[validators.required()])
