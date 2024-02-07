from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from map.map import map


class Shipping_Form(FlaskForm):
    sender = StringField("Name of Sender", validators=[DataRequired()])
    recipent = StringField("Name of Recipient", validators=[DataRequired()])
    origin = SelectField("Origin options", choices=[map.keys()], validators=[DataRequired()])
    destination = SelectField("Destination options", choices=[map.keys()], validators=[DataRequired()])
    express_shipping = BooleanField("Express Shipping desired?", validators=[DataRequired()])
    submit_button = SubmitField("Submit")
    