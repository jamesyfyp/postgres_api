from flask_sqlalchemy import SQLAlchemy
from app.routes import user_s_routes, post_s_routes
from factory import create_app

app, db = create_app()

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)