import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")
    # Mặc định dùng SQLite cho Local/MVP, tự động chuyển sang MySQL nếu có biến môi trường DATABASE_URL
    # Ví dụ MySQL: mysql+pymysql://root:password@localhost:3306/lms_db?charset=utf8mb4
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", f"sqlite:///{BASE_DIR / 'lms_judge.db'}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
    }
    # Cấu hình Auto-Judge Thread Pool
    JUDGE_MAX_WORKERS = int(os.environ.get("JUDGE_MAX_WORKERS", 2))


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False
