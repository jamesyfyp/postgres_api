from flask_sqlalchemy import SQLAlchemy
from app.models import db
from app.routes import user_s_routes, post_s_routes
from factory import create_app

app, db = create_app()

app.register_blueprint(user_s_routes.user_bp)
app.register_blueprint(post_s_routes.post_bp)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)