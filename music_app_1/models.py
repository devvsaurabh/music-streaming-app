from music_app_1 import db


class MusicStore(db.Model):

    __tablename__ = 'music_store'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.Text)
    artist = db.Column(db.Integer)
    album = db.Column(db.Text)

    def __init__(self,title,artist,album):
        self.title = title
        self.artist = artist
        self.album = album


    def __repr__(self):
        return f"{self.title}"