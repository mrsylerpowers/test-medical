from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, PasswordField, IntegerField, FormField
from wtforms.validators import InputRequired




class RegisterFormPatent(FlaskForm):
    username = StringField(u'Username',
                           validators=[InputRequired(message="You must enter a username"), validators.length(max=50)])
    password = PasswordField('Password',
                             [InputRequired(message="You must enter a password"), validators.length(max=50)])
    name = StringField(u'Full name',
                       validators=[InputRequired(message="You must enter the patents name"), validators.length(max=50)])
    address = TextAreaField(u'Address',
                            [InputRequired(message="You must enter the patents address"), validators.length(max=200)])
    mobile_phone = StringField('Number',[validators.required()])
    accountBalance = IntegerField(u'Account Balance', [validators.required()])
