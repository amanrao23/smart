from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import InputRequired, Length, Email

'''new control centre form'''


class Newctrlcntrform(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(min=2, max=20)])
    username = StringField('Username', validators=[InputRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=2, max=20)])
    submit = SubmitField('signup')


class Loginctrlform(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=2, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class Newngoform(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(min=2, max=20)])
    disasterId = IntegerField('DisasterID', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=2, max=20)])
    submit = SubmitField('signup')


class Loginngoform(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=2, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('signup')
