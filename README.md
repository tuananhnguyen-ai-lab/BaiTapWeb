# Website Học Lập Trình Web Theo Lộ Trình Cho Người Mới Bắt Đầu

Bài tập lớn môn **Lập trình Web**. Website giúp người mới học lập trình web biết mình đang ở trình độ nào, học theo một lộ trình rõ ràng (dạng cây kỹ năng), làm bài tập có sẵn khung code và tìm bạn học cùng lộ trình.

## 🎯 Vấn đề muốn giải quyết

Người mới tự học lập trình web thường bị ngợp vì có quá nhiều tài liệu, không biết bắt đầu từ đâu, sợ "trang giấy trắng" khi phải tự viết code từ đầu và dễ bỏ giữa chừng vì học một mình.

Website này giải quyết các thách thức trên bằng các giải pháp:
* **Test đầu vào:** Đánh giá năng lực ban đầu để xếp người học vào lộ trình phù hợp.
* **Cây kỹ năng (Skill Tree):** Thiết kế dạng node (HTML → CSS → JavaScript → DOM → ...), học xong node trước mới mở khóa node sau.
* **Bài tập hướng dẫn từng bước:** Có sẵn khung code, chỉ cần điền phần còn thiếu; code mẫu giảm dần độ gợi ý ở các bài nâng cao.
* **Tính năng ghép cặp bạn học (Study Buddy):** Mô hình quẹt/match bạn học cùng lộ trình để nhắn tin, tương tác và nhắc nhở nhau học tập.
* **Trợ lý AI tích hợp:** Giải thích lỗi sai bằng tiếng Việt và gợi ý bài học tiếp theo phù hợp.

## 🧩 Các module chính

Đề tài chọn **4 module** trong danh sách hệ thống môn học:

| Module | Nội dung trong website |
| :--- | :--- |
| **M10 – LMS/LCMS và tài nguyên học tập** | Quản lý bài học, bài tập, cây kỹ năng, lộ trình học và hệ thống chấm bài tự động. |
| **M12 – Hỗ trợ người học** | Hệ thống ghép cặp/quẹt tìm bạn học chung (*Study Buddy*), phòng chat nhắn tin riêng giữa bạn học. |
| **M16 – Đào tạo năng lực số** | Test đầu vào, theo dõi tiến độ học tập, tính điểm XP, huy hiệu, chuỗi ngày học (*Streak*). |
| **M20 – Tài khoản, SSO và phân quyền** | Đăng ký/đăng nhập (Email, Google, GitHub), phân quyền người dùng (Khách / Người học / Mentor / Admin). |

## 👤 Người dùng và chức năng

| Vai trò | Chức năng thực hiện |
| :--- | :--- |
| **Khách** | Xem giới thiệu, xem cây kỹ năng mẫu, làm thử test đầu vào, đăng ký tài khoản. |
| **Người học** | Làm test đầu vào, học theo cây kỹ năng, làm và nộp bài tập, nhận XP và huy hiệu, **quẹt/ghép cặp bạn học cùng lộ trình để nhắn tin**, hỏi trợ lý AI. |
| **Mentor / Giảng viên** | Tạo bài học, bài tập, node và lộ trình; xem tiến độ và nhận xét bài làm của người học. |
| **Quản trị viên** | Quản lý tài khoản và phân quyền, ngân hàng câu hỏi, duyệt nội dung, xử lý báo cáo vi phạm. |

## 🛠 Công nghệ sử dụng

* **Frontend:** ReactJS (Next.js), TailwindCSS, React Flow (vẽ cây kỹ năng), Monaco Editor (soạn code trên trình duyệt).
* **Backend:** Node.js (Express/NestJS), REST API, Socket.IO (chat real-time).
* **Cơ sở dữ liệu:** PostgreSQL, Redis (cache, quản lý phiên đăng nhập).
* **Chấm bài:** Chạy code HTML/CSS/JS trong iframe sandbox, kiểm thử bằng Jest.
* **Xác thực:** JWT, OAuth (Google/GitHub).
* **AI:** OpenAI API hoặc Gemini API.
* **Triển khai:** Docker, Vercel (frontend), Render/Railway (backend).

## 📁 Cấu trúc thư mục (dự kiến)

```text
.
├── frontend/   # Giao diện Next.js
├── backend/    # API Node.js
├── docs/       # Tài liệu, báo cáo, thiết kế
└── README.md
```

## 🚀 Cài đặt và chạy (dự kiến)

```bash
# Lấy mã nguồn
git clone https://github.com/tuananhnguyen-ai-lab/B-i-t-p-Web.git
cd B-i-t-p-Web

# Chạy backend
cd backend
npm install
npm run dev

# Chạy frontend (mở terminal khác)
cd frontend
npm install
npm run dev
```

> **Lưu ý:** Tạo file `.env` trong thư mục `backend/` với các biến môi trường như `DATABASE_URL`, `JWT_SECRET`, `GOOGLE_CLIENT_ID`, `AI_API_KEY` trước khi vận hành dự án.

## 👥 Thành viên nhóm

| Họ tên | MSSV | Công việc |
| :--- | :--- | :--- |
| | | |

## 📚 Tài liệu tham khảo

* [roadmap.sh](https://roadmap.sh/)
* [freeCodeCamp](https://www.freecodecamp.org/)
* [The Odin Project](https://www.theodinproject.com/)
* [MDN Web Docs](https://developer.mozilla.org/)
* Duolingo (Mô hình cây kỹ năng, XP, chuỗi ngày học)
