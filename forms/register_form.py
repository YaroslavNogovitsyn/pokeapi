from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email


class RegisterForm(FlaskForm):
    email = StringField("Email: ", validators=[DataRequired(), Email("Некорректный email")],
                        render_kw={"placeholder": "Enter your email"})
    patronymic = StringField(render_kw={"placeholder": "Your patronymic (if exists)"})
    password = PasswordField(validators=[DataRequired()],
                             render_kw={"placeholder": "Enter your password"})
    password_again = PasswordField(validators=[DataRequired()],
                                   render_kw={"placeholder": "Repeat your password"})
    submit = SubmitField('REGISTER')
