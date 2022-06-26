from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField
from wtforms.validators import DataRequired

class AddProjectForm(FlaskForm):
    title = StringField('Titel', validators=[DataRequired()])
    desc = TextAreaField('Beschreibung', validators=[DataRequired()])
    submit = SubmitField('Hinzufügen')