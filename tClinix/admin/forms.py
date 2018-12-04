from flask_wtf import FlaskForm
from wtforms import (
    FloatField,
    IntegerField,
    TextField,
    PasswordField,
    SelectField,
    SelectMultipleField
)



class LoginForm(FlaskForm):
    name = TextField('Username')
    password = PasswordField('Password')


class CreateAccountForm(FlaskForm):
    name = TextField('Username')
    email = TextField('Email')
    password = PasswordField('Password')
 

class AddUser(FlaskForm):
    name = TextField('Username')
    email = TextField('Email')
    access_right_choices = (('Read-only',) * 2, ('Read-write',) * 2)
    access_rights = SelectField('Access rights', choices=access_right_choices)
    password = PasswordField('Password')


class DeleteUser(FlaskForm):
    users = SelectMultipleField('Users', choices=())
