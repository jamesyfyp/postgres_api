from flask_sqlalchemy import SQLAlchemy
from factory import db


class Users_s(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    posts = db.relationship('Post_s', backref='author', lazy=True)



