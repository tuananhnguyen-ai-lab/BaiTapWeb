# Phân công công việc nhóm 4 người

**Đề tài:** Website học lập trình web theo lộ trình cho người mới bắt đầu
**Module:** M10, M12, M16, M20 (theo README)

Nguyên tắc: mỗi người phụ trách đúng **1 module** và tự làm cả giao diện (frontend), API (backend) và bảng dữ liệu của module đó. Ai cũng code ngang nhau.

## Mỗi người một module

### Thành viên 1 – M20: Tài khoản, SSO và phân quyền
- Đăng ký, đăng nhập bằng Email, Google, GitHub (JWT, OAuth), quên/đổi mật khẩu
- Phân quyền Khách / Người học / Mentor / Admin, chặn trang và API theo quyền
- Hồ sơ cá nhân (ảnh, mục tiêu học, thời gian rảnh)
- Trang Admin: quản lý tài khoản, khóa/mở, đổi quyền, thống kê người dùng

### Thành viên 2: Tuấn Anh – M10: LMS/LCMS và tài nguyên học tập
- Cây kỹ năng dạng sơ đồ node (React Flow), khóa/mở khóa node
- Trang bài học, lộ trình học
- Bài tập điền code (Monaco Editor), xem trước kết quả, chấm tự động (iframe sandbox + Jest)
- Trang Mentor tạo/sửa bài học, bài tập, node, lộ trình; Admin duyệt nội dung

### Thành viên 3: Nhữ Hằng – M12: Hỗ trợ người học
- Quẹt/ghép cặp bạn học cùng lộ trình (Study Buddy)
- Phòng chat riêng giữa bạn học (Socket.IO), tạo nhóm học
- Báo cáo/chặn người dùng; Admin xử lý báo cáo vi phạm
- Trợ lý AI giải thích lỗi bằng tiếng Việt, gợi ý theo mức 1-2-3; Mentor nhận xét bài làm

### Thành viên 4 – Nhi: Đào tạo năng lực số
- Test đầu vào, xếp người học vào lộ trình; Admin quản lý ngân hàng câu hỏi
- Theo dõi tiến độ học tập, XP, huy hiệu, chuỗi ngày học (Streak), bảng xếp hạng
- Trang thống kê tiến độ người học cho Mentor
- AI gợi ý bài học tiếp theo dựa trên kết quả test và lịch sử làm bài

## Chỗ các module nối với nhau

- **M20** làm xong đăng nhập trước (tuần 2) để 3 module còn lại dùng chung.
- **M10** báo "đã làm xong bài" cho **M16** (cộng XP, cập nhật tiến độ) và gửi bài sai cho **M12** (AI giải thích lỗi).
- **M16** xếp lộ trình sau test đầu vào, **M12** dùng lộ trình và trình độ đó để ghép cặp.
- Cả nhóm thống nhất bảng dữ liệu chung (người dùng, node, bài nộp) và quy ước API ngay tuần đầu.

## Việc chung, chia đều

| Việc | Người làm |
|---|---|
| Tạo repo GitHub, khung dự án, triển khai (Docker, Vercel, Render) | Thành viên 1 |
| Thiết kế giao diện Figma, giao diện chung (header, menu, trang chủ) | Thành viên 2 |
| Viết test case, kiểm thử tổng thể | Thành viên 3 |
| Khảo sát người dùng, bảng so sánh, ghép báo cáo | Thành viên 4 |
| Báo cáo và demo module của mình, slide, cho người dùng thử | Cả nhóm |

## Gợi ý tiến độ

| Giai đoạn | Việc cần xong |
|---|---|
| Tuần 1–2 | Khảo sát, Figma, thống nhất CSDL và API, dựng khung dự án, xong đăng nhập |
| Tuần 3–5 | Mỗi người làm chức năng chính của module mình |
| Tuần 6 | Nối các module, phần Mentor/Admin |
| Tuần 7 | Tích hợp AI, kiểm thử |
| Tuần 8 | Triển khai, cho dùng thử, hoàn thiện báo cáo và slide |

## Bảng điền vào README

| Họ tên | MSSV | Công việc |
| :--- | :--- | :--- |
| Thành viên 1 | | M20 – Tài khoản, SSO, phân quyền; trang Admin; triển khai |
| Tuấn Anh | | M10 – Cây kỹ năng, bài học, bài tập, chấm bài; trang Mentor; Figma |
| Nhữ Hằng| | M12 – Ghép cặp bạn học, chat, trợ lý AI; kiểm thử |
| Thành viên 4 | | M16 – Test đầu vào, tiến độ, XP, huy hiệu, streak; khảo sát, báo cáo |
