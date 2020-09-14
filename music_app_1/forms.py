from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField, StringField, SelectField

class SongUploadForm(FlaskForm):
    file = FileField('Upload Song')
    submit = SubmitField('Add Song')

class SearchForm(FlaskForm):
    choices = [('Artist', 'Artist'),
               ('Album', 'Album'),
               ('Title', 'Title')]
    select = SelectField('Search for music:', choices=choices)
    search = StringField('')
