# Hướng dẫn đề xuất cơ cấu team

Tỷ lệ vai trò dưới đây phản ánh cách phân bổ effort trong bối cảnh phát triển phần mềm có ứng dụng AI hỗ trợ code (AI coding assistant), khác với tỷ lệ truyền thống: effort dành cho code thuần túy giảm tương đối (AI tăng throughput viết code trên đầu người), trong khi effort dành cho đặc tả yêu cầu (BA) và kiểm thử/verify (QA) tăng lên — vì điểm nghẽn dịch chuyển từ "viết code" sang "đặc tả đúng" và "kiểm chứng đúng".

## Tỷ lệ vai trò (điểm khởi đầu — hiệu chỉnh theo dự án thực tế)

| Vai trò | Tỷ lệ effort |
|---|---|
| PM (Project Manager) | ~10% |
| BA (Business Analyst) | ~15% |
| Designer (UI/UX) | ~3% |
| Dev (Frontend + Backend) | ~40 – 45% |
| QA | ~20 – 25% |
| Khác (DevOps/Infra...) | ~5% |

Khi Dev và QA có range, chọn giá trị sao cho tổng tất cả vai trò = 100% (ví dụ Dev 42%, QA 25% nếu các vai trò còn lại lấy giá trị giữa).

## Cách tính headcount đề xuất

1. **Tổng effort sau buffer** (man-day, từ bước áp dụng `buffer-rubric.md`).
2. **Số ngày làm việc trong timeline:** lấy khoảng từ "Ngày mong muốn khởi động" đến "Ngày mong muốn go-live / deadline" trong requirements-summary.md, quy đổi ra ngày làm việc (giả định ~22 ngày làm việc/tháng nếu không có thông tin lịch cụ thể).
3. **Blended FTE** = Tổng effort sau buffer ÷ Số ngày làm việc trong timeline.
4. **Headcount từng vai trò** = làm tròn (Blended FTE × tỷ lệ vai trò đó). Áp dụng tối thiểu hợp lý: PM tối thiểu 1 nếu dự án có từ 2 vai trò khác trở lên; nếu Dev ≥ 1 thì QA tối thiểu 1 (không thể có code mà không kiểm thử).

## Khi thiếu thông tin timeline

Nếu requirements-summary.md không có ngày go-live/deadline cụ thể, dùng thời lượng do skill tự đề xuất theo `schedule-phases.md` (Trường hợp 2) để tính headcount — không để trống, vì đây chính là lý do skill phải đề xuất timeline trước. Ghi rõ trong team-composition.md rằng headcount này dựa trên timeline đề xuất, chưa phải timeline khách hàng xác nhận.

## Liên kết với Master Schedule

Sau khi có headcount tổng (peak team size), đối chiếu với các giai đoạn trong `schedule-phases.md` để ghi ra **cửa sổ tham gia** của từng vai trò — không cần dựng ma trận headcount chi tiết theo từng giai đoạn, chỉ cần nêu vai trò nào full-time/part-time ở giai đoạn nào, dựa trên cột "Vai trò chính tham gia" của từng giai đoạn trong `schedule-phases.md`. Ví dụ: PM tham gia full-time xuyên suốt mọi giai đoạn; QA chỉ tham gia part-time ở giai đoạn Phát triển rồi full-time ở giai đoạn Kiểm thử & UAT.
