import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__,template_folder='templates',static_folder='static/uploads')

app.config['SECRET_KEY'] = 'asdfgghj'

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_EXTENSIONS'] = ['mp3']
app.config['UPLOAD_PATH'] = os.path.join(basedir,'static/uploads')

db = SQLAlchemy(app)

Migrate(app,db)

from music_app_1.views import songs_blueprint

app.register_blueprint(songs_blueprint,url_prefix='/song/')

