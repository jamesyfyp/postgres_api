from flask_sqlalchemy import SQLAlchemy
from pgvector.sqlalchemy import Vector
from factory import db

class Chunk_s(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users_s.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post_s.id'), nullable=False)
    chunk_number = db.Column(db.Integer, nullable=False)
    text_chunk = db.Column(db.Text, nullable=False)
    vector = db.Column(Vector(384), nullable=False)