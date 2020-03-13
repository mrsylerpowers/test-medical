from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SelectField
from wtforms.validators import DataRequired, InputRequired

class RegisterForm(FlaskForm):
    acessType = SelectField(u"Access Type", choices=[(2,"Doctor"),(1,"Nurse")], coerce=int)
    username = StringField(u'Username', validators=[InputRequired(message="You must enter a username"),validators.length(max=50)])
    password = PasswordField('Password', [InputRequired(message="You must enter a password"), validators.length(max=50)])

class LoginForm(FlaskForm):
    username = StringField(u'Username', validators=[InputRequired(message="You must enter a username"),validators.length(max=50)])
    password = PasswordField('Password', [InputRequired(message="You must enter a password"), validators.length(max=50)])