from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField('Enter your email', validators=[DataRequired()])
    password = PasswordField('Enter your password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me here')
    submit = SubmitField('LOG IN')