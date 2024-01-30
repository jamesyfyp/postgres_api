from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import db
from app.routes import user_s_routes, post_s_routes
from urllib.parse import quote
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB_NAME')

encoded_password = quote(password, safe='')

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{username}:{encoded_password}@{host}:{port}/{database}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)