from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User_s(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)  
    posts = db.relationship('Post', backref='author', lazy=True)

