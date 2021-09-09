from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired, Length

class Blog_info(FlaskForm):
    title = StringField('Blog title:', validators=[DataRequired(), Length(max=30)] )
    description = TextAreaField('Description:', validators=[Length(max=50)])
