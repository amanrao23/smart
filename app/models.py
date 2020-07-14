from app import db,login_manager
from flask_login import UserMixin
from sqlalchemy import PrimaryKeyConstraint, ForeignKeyConstraint

@login_manager.user_loader
def load_user(user_id):
    return Allusers.query.get(int(user_id))

class Allusers(UserMixin, db.Model):  # all users login id and password are stored here
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(80), default='guest')


class Control(db.Model):  # control centre class
    id = db.Column(db.Integer, primary_key=True)  # disaster id
    c_name = db.Column(db.String(20))
    c_username = db.Column(db.String(20), db.ForeignKey('allusers.username'), nullable=False)
    c_password = db.Column(db.String(60), nullable=False)
    ngo_manage = db.relationship('Ngo', backref='Control')


class Ngo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ngo_name = db.Column(db.String(20))
    control_id = db.Column(db.Integer, db.ForeignKey('control.id'), nullable=False)  # disaster id
    ngo_username = db.Column(db.String(20), db.ForeignKey('allusers.username'), nullable=False)
    ngo_password = db.Column(db.String(60), nullable=False)


class Offsitehelper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20), db.ForeignKey('allusers.username'), nullable=False)
    password = db.Column(db.String(60), nullable=False)


class Alltweets(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    content = db.Column(db.String(200))
    location = db.Column(db.String(200), nullable=True)
    control_id = db.Column(db.Integer, db.ForeignKey('control.id'), nullable=False)#disaster id


class Segregatedtweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    control_id = db.Column(db.Integer, db.ForeignKey('control.id'), nullable=False)  # disaster id
    content = db.Column(db.String(200))
    location = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(20), nullable=True)  # assigned/verified/matched etc
    type = db.Column(db.String(20), nullable=False)  # need or availability
    ngo_id = db.Column(db.Integer, db.ForeignKey('ngo.id'))


class matchedtweet(db.Model):
    __tablename__ = 'matchedtweet'
    ntweet = db.Column(db.Integer)
    atweet = db.Column(db.Integer)
    status = db.Column(db.String(20), nullable=True)  # assigned/verified/matched etc
    ngo_id = db.Column(db.Integer, db.ForeignKey('ngo.id'))

    __table_args__ = (
        PrimaryKeyConstraint('ntweet', 'atweet'), ForeignKeyConstraint([ntweet, atweet],
                                                                       [Segregatedtweet.id, Segregatedtweet.id]),
        {},)


class Comments(db.Model):
    username = db.Column(db.String(20), db.ForeignKey('allusers.username'), primary_key=True, nullable=False)
    comment = db.Column(db.String(200))
    tweetid = db.Column(db.Integer, db.ForeignKey('segregatedtweet.id'), nullable=False)

