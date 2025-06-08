from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
  password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
  confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Register')

class LoginForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Login')

class StudentProfileForm(FlaskForm):
  full_name = StringField('Full Name', validators=[DataRequired()])
  age = IntegerField('Age', validators=[DataRequired()])
  submit = SubmitField('Update Profile')