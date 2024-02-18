from flask import Flask
from database import db
from routes import user_blueprint

# Flask App
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = ''
# Register the Flask app with SQLAlchemy
db.init_app(app)


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.register_blueprint(user_blueprint)
    app.run(host='0.0.0.0', port=3030)
