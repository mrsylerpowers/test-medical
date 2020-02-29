from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, InputRequired


class LoginForm(FlaskForm):
    username = StringField(u'Username', validators=[InputRequired(message="You must enter a username"),validators.length(max=50)])
    password = PasswordField('Password', [InputRequired(message="You must enter a password"), validators.length(max=50)])