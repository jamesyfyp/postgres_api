from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users_s(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)  
    user_id = db.Column(db.Integer, db.ForeignKey('user_s.id'), nullable=False)

