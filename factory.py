from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import SQLALCHEMY_DATABASE_URI

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # Initialize the db object with the app

    # Register your blueprints or import your routes here
    from app.routes import user_s_routes, post_s_routes
    app.register_blueprint(user_s_routes.user_bp)
    app.register_blueprint(post_s_routes.post_bp)

    return app, db