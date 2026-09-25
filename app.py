import os
from flask import Flask
from config import Config
from extensions import db, login_manager
from models import User
from blueprints.auth import auth_bp
from blueprints.classes import classes_bp
from blueprints.attendance import attendance_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Ensure the instance directory exists before database initialization
    os.makedirs(app.instance_path, exist_ok=True)

    db.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(auth_bp)
    app.register_blueprint(classes_bp)
    app.register_blueprint(attendance_bp)

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)