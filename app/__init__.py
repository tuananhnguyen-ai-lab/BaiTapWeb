from flask import Flask
from config import Config
from app.extensions import db, migrate, login_manager


def create_app(config_class=Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Khởi tạo các Extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Đăng ký các Modular Blueprints
    from app.blueprints.auth import auth_bp
    from app.blueprints.main import main_bp
    from app.blueprints.judge import judge_bp
    from app.blueprints.skills import skills_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(judge_bp)
    app.register_blueprint(skills_bp)

    return app
