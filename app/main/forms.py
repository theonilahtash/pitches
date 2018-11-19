from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from ..models import Pitch, Comment
from wtforms.validators import DataRequired


class PitchForm(FlaskForm):
    title = StringField('Category Pitch', validators=[DataRequired()])
    body = TextAreaField('Add your Pitch', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Add a comment', validators=[DataRequired()])
    submit = SubmitField('Submit')
