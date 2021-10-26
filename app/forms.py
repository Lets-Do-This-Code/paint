from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired

# Place forms for taking data here

class RegisterForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    surname= StringField('Surname')
    phone = StringField('Phone')
    submit = SubmitField('Complete Registration')



class CalculateForm(FlaskForm):
	height = IntegerField('Height')
	width = IntegerField('Width')
	submit = SubmitField ('Submit')
