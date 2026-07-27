# Warranty & Maintenance model / Communication plan — điểm khởi đầu

Đề xuất khởi điểm, hiệu chỉnh lại theo từng deal/chính sách công ty khi cần.

## Warranty & Maintenance model

- **Thời gian bảo hành:** 3 tháng miễn phí sau ngày go-live, tính từ ngày nghiệm thu (UAT sign-off).
- **Phạm vi bảo hành:** sửa lỗi phát sinh từ code do đội ngũ phát triển (bug), không bao gồm thay đổi/bổ sung yêu cầu mới (change request tính riêng).
- **SLA xử lý lỗi trong thời gian bảo hành:**

| Mức độ nghiêm trọng | Thời gian phản hồi | Thời gian xử lý mục tiêu |
|---|---|---|
| Critical (hệ thống ngừng hoạt động) | ≤ 2 giờ | ≤ 24 giờ |
| High (chức năng chính lỗi, có workaround) | ≤ 4 giờ | ≤ 3 ngày làm việc |
| Medium (chức năng phụ lỗi) | ≤ 1 ngày làm việc | ≤ 5 ngày làm việc |
| Low (lỗi nhỏ, giao diện...) | ≤ 2 ngày làm việc | Theo kế hoạch release tiếp theo |

- **Sau bảo hành:** đề xuất gói bảo trì trả phí (theo tháng hoặc theo support ticket) — chi tiết đàm phán riêng, không thuộc phạm vi báo giá ban đầu.

## Communication plan

- **Daily standup:** 15 phút/ngày giữa PM và các lead (Dev Lead, QA Lead), đồng bộ tiến độ, blocker.
- **Weekly status report:** gửi khách hàng vào cuối mỗi tuần — tiến độ so với master schedule, rủi ro phát sinh, việc cần khách hàng quyết định/phản hồi.
- **Sprint review / demo:** cuối mỗi giai đoạn phát triển (theo master schedule), demo tính năng đã hoàn thành cho khách hàng.
- **Kênh liên lạc:** đề xuất 1 kênh chat trực tiếp (Slack/Teams) cho trao đổi hàng ngày + email cho các quyết định/xác nhận chính thức cần lưu vết.
- **Escalation path:** nếu vấn đề không giải quyết được ở cấp PM trong X ngày làm việc, escalate lên cấp quản lý cao hơn của cả 2 bên (ghi rõ đầu mối trong "Vai trò & trách nhiệm hai bên" của requirements-summary.md).
