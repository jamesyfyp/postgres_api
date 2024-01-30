from flask import Flask
from sqlalchemy import create_engine
from urllib.parse import quote
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB_NAME')

encoded_password = quote(password, safe='')

database_uri = f"postgresql://{username}:{encoded_password}@{host}:{port}/{database}"
engine = create_engine(database_uri)

# Test the connection
try:
    connection = engine.connect()
    print("Connected successfully!")
    connection.close()
except Exception as e:
    print(f"Error: {e}")

# Test the connection
try:
    connection = engine.connect()
    print("Connected successfully!")
    connection.close()
except Exception as e:
    print(f"Error: {e}")

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)