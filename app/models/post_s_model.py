from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post_s(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    posts = db.relationship('Post_s', backref='author', lazy=True)
