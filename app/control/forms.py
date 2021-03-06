from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import InputRequired, Length, Email


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

class Parametersform(FlaskForm):
    searchQuery = StringField('Keyword') # this is what we're searching for
    maxTweets = IntegerField('maz tweets')  # Some arbitrary large number
    tweetsPerQry = IntegerField('Tweets Per Query')
    submit=SubmitField('Start Fetching')