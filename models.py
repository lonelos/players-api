import datetime
import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    nationality_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    current_club_id = db.Column(db.Integer, db.ForeignKey('clubs.id'))
    preferred_position = db.Column(db.String(64))
    date_of_birth = db.Column(db.Date)
    last_modified = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    players = db.relationship('Player', backref='nationality')


class Club(db.Model):
    __tablename__ = 'clubs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    players = db.relationship('Player', backref='current_club')
