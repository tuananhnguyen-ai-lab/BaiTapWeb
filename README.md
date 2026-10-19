# Website học lập trình web theo lộ trình cho người mới bắt đầu

Bài tập lớn môn Lập trình Web. Website giúp người mới học lập trình web biết mình đang ở trình độ nào, học theo một lộ trình rõ ràng (dạng cây kỹ năng), làm bài tập có sẵn khung code và tìm bạn học cùng lộ trình.

## Vấn đề muốn giải quyết

Người mới tự học web thường bị ngợp vì quá nhiều tài liệu, không biết bắt đầu từ đâu, sợ "trang giấy trắng" khi phải tự viết code và dễ bỏ giữa chừng vì học một mình. Website này giải quyết bằng:

- **Test đầu vào** để xếp người học vào lộ trình phù hợp.
- **Cây kỹ năng** (HTML → CSS → JavaScript → DOM → ...), học xong node trước mới mở khóa node sau.
- **Bài tập có hướng dẫn từng bước**: có sẵn khung code, chỉ cần điền phần còn thiếu, code mẫu giảm dần ở các bài sau.
- **Ghép cặp bạn học** cùng lộ trình để nhắn tin, nhắc nhau học.
- **Trợ lý AI** giải thích lỗi bằng tiếng Việt và gợi ý bài học tiếp theo.

## Các module chính

Đề tài chọn 3 module trong danh sách của môn học:

| Module | Nội dung trong website |
|---|---|
| **M10 – LMS/LCMS và tài nguyên học tập** | Bài học, bài tập, cây kỹ năng, lộ trình học, chấm bài tự động |
| **M16 – Đào tạo năng lực số** | Test đầu vào, theo dõi tiến độ, XP, huy hiệu, chuỗi ngày học, kết nối bạn học |
| **M20 – Tài khoản, SSO và phân quyền** | Đăng ký/đăng nhập (email, Google, GitHub), phân quyền Khách / Người học / Mentor / Admin |

## Người dùng và chức năng

| Vai trò | Làm được gì |
|---|---|
| Khách | Xem giới thiệu, xem cây kỹ năng mẫu, làm thử test đầu vào, đăng ký |
| Người học | Làm test đầu vào, học theo cây kỹ năng, làm và nộp bài tập, nhận XP và huy hiệu, ghép cặp bạn học, hỏi trợ lý AI |
| Mentor / Giảng viên | Tạo bài học, bài tập, node và lộ trình; xem tiến độ và nhận xét bài làm của người học |
| Quản trị viên | Quản lý tài khoản và phân quyền, ngân hàng câu hỏi, duyệt nội dung, xử lý báo cáo vi phạm |

## Công nghệ sử dụng

- **Frontend:** ReactJS (Next.js), TailwindCSS, React Flow (vẽ cây kỹ năng), Monaco Editor (soạn code trên trình duyệt)
- **Backend:** Node.js (Express/NestJS), REST API, Socket.IO (chat)
- **Cơ sở dữ liệu:** PostgreSQL, Redis (cache, phiên đăng nhập)
- **Chấm bài:** chạy code HTML/CSS/JS trong iframe sandbox, kiểm thử bằng Jest
- **Xác thực:** JWT, OAuth (Google/GitHub)
- **AI:** OpenAI API hoặc Gemini API
- **Triển khai:** Docker, Vercel (frontend), Render/Railway (backend)

## Cấu trúc thư mục (dự kiến)

```
.
├── frontend/   # Giao diện Next.js
├── backend/    # API Node.js
├── docs/       # Tài liệu, báo cáo, thiết kế
└── README.md
```

## Cài đặt và chạy (dự kiến)

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

Tạo file `.env` trong `backend/` với các biến như `DATABASE_URL`, `JWT_SECRET`, `GOOGLE_CLIENT_ID`, `AI_API_KEY` trước khi chạy.

## Thành viên nhóm

| Họ tên | MSSV | Công việc |
|---|---|---|
|  |  |  |
|  |  |  |

## Tài liệu tham khảo

- [roadmap.sh](https://roadmap.sh)
- [freeCodeCamp](https://www.freecodecamp.org)
- [The Odin Project](https://www.theodinproject.com)
- [MDN Web Docs](https://developer.mozilla.org)
- [Duolingo](https://www.duolingo.com) (mô hình cây kỹ năng, XP, chuỗi ngày học)
