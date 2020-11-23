from wtforms_alchemy import ModelForm
from .model import User
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.validators import DataRequired, Email,ValidationError





class Unique(object):
    def __init__(self, model, field, message=None):
        self.model = model
        self.field = field
        if not message:
            message = 'this email already exists'
        self.message = message

    def __call__(self, form, field):         
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)

class UserForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(),Email(),Unique(User, User.email)])
    password = StringField('password', validators=[DataRequired()])


        