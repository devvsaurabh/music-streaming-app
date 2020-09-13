from flask import Blueprint,render_template,redirect,url_for,request,flash,send_file
from music_app_1 import db
from music_app_1.models import MusicStore
from music_app_1.forms import SongUploadForm
import eyed3
import os
from music_app_1 import app
from werkzeug.utils import secure_filename


songs_blueprint = Blueprint('songs',__name__,
                             template_folder="templates/")


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['UPLOAD_EXTENSIONS']


@songs_blueprint.route("upload/",methods=["GET","POST"])
def upload_song():

    form = SongUploadForm()

    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file uploaded')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_PATH'], filename))

            # extracting metadata from the .mp3 file
            audf = eyed3.load(os.path.join(app.config['UPLOAD_PATH'], filename))
            s_title = audf.tag.title
            s_artist = audf.tag.artist
            s_album = audf.tag.album
            store = MusicStore(s_title,s_artist,s_album,filename)
            db.session.add(store)
            db.session.commit()

            songs = MusicStore.query.all()
            return render_template('allSongs.html',songs = songs)
    return render_template('upload.html', form=form)


@songs_blueprint.route("all_songs/",methods=["GET"])
def fetch_all_songs():
    # Loading all the songs
    songs = MusicStore.query.all()
    return render_template('allSongs.html',songs = songs)


@songs_blueprint.route("delete/<id>",methods=["GET","POST"])
def delete_song(id):
    # delete the song using songid
    song = MusicStore.query.get(id)
    path = os.path.join(app.config['UPLOAD_PATH'], song.filename)
    os.remove(path)
    db.session.delete(song)
    db.session.commit()

    # Loading rest songs
    songs = MusicStore.query.all()
    return render_template('allSongs.html',songs = songs)


@songs_blueprint.route("play/<id>",methods = ["GET","POST"])
def play_song(id):
    music = MusicStore.query.get(id)
    filename = music.filename
    path = os.path.join(app.config['UPLOAD_PATH'], filename)
    return render_template("play.html",path=path,music = music)



@songs_blueprint.route("download/<filename>",methods=["GET","POST"])
def download_song(filename):
    path = os.path.join(app.config['UPLOAD_PATH'], filename)
    return send_file(path, as_attachment=True)
    












