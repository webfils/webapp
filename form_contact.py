from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

csrf = CSRFProtect()

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired('Error en el Nombre!')])
    email = StringField('Email', validators=[DataRequired('Error en el Correo!'),Email('No hemos logrado procesar su correo!')])
    subject = StringField('Subject', validators=[DataRequired('Error en el Asunto!')])
    message = TextAreaField('Message', validators=[DataRequired('No hemos logrado procesar su mensaje!')])
    submit = SubmitField("Send")