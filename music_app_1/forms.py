from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField

class SongUploadForm(FlaskForm):
    file = FileField('Upload Song')
    submit = SubmitField('Add Song')