from flask import Blueprint,render_template,redirect,url_for
from music_app_1 import db



songs_blueprint = Blueprint('songs',__name__,
                             template_folder='./templates/music_app_1')