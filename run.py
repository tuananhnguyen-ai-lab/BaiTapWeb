from app import create_app
from app.extensions import db
from app.seed import seed_initial_data

app = create_app()


def init_db_and_seed():
    with app.app_context():
        db.create_all()
        seed_initial_data()


if __name__ == "__main__":
    init_db_and_seed()
    print("\n" + "=" * 75)
    print("🚀 WEBSITE HỌC LẬP TRÌNH WEB THEO LỘ TRÌNH CHO NGƯỜI MỚI BẮT ĐẦU (M10)")
    print("👉 Truy cập ngay tại: http://127.0.0.1:5000")
    print("👤 Vai trò 1 - Khách (Guest): Xem giới thiệu, Cây kỹ năng mẫu, Test đầu vào")
    print("🎓 Vai trò 2 - Người học:     hocvien / 123456")
    print("👨‍🏫 Vai trò 3 - Mentor / GV:   mentor  / 123456")
    print("🛡️  Vai trò 4 - Quản trị viên: admin   / 123456")
    print("=" * 75 + "\n")
    app.run(host="127.0.0.1", port=5000, debug=True)
