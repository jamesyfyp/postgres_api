import os
from urllib.parse import quote

from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB_NAME')

encoded_password = quote(password, safe='')

SQLALCHEMY_DATABASE_URI = f"postgresql://{username}:{encoded_password}@{host}:{port}/{database}"

print(SQLALCHEMY_DATABASE_URI)