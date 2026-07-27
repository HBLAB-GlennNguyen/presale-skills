# Các giai đoạn dự án chuẩn & cách dựng Master Schedule

## Các giai đoạn & tỷ lệ thời gian

Điểm khởi đầu (starting point) để chia tổng thời lượng dự án thành các giai đoạn — hiệu chỉnh lại theo đặc thù từng dự án khi cần.

| Giai đoạn | % thời gian dự án | Vai trò chính tham gia |
|---|---|---|
| Khởi tạo & chốt yêu cầu | ~10% | PM, BA |
| Thiết kế (UI/UX + kỹ thuật) | ~15% | PM, BA, Designer, Dev (tech lead) |
| Phát triển | ~50% | Dev (toàn bộ); QA bắt đầu tham gia từ giữa giai đoạn |
| Kiểm thử & UAT | ~20% | QA (toàn bộ); Dev hỗ trợ fix bug |
| Triển khai & bàn giao | ~5% | PM, Dev, DevOps/hạ tầng |

Tổng = 100% thời lượng dự án.

## Xác định tổng thời lượng dự án

**Trường hợp 1 — khách hàng đã cho timeline:** dùng "Ngày mong muốn khởi động" và "Ngày mong muốn go-live / deadline" trong requirements-summary.md làm tổng thời lượng cố định. Team composition (xem `team-composition-guide.md`) được tính để khớp với thời lượng này.

**Trường hợp 2 — khách hàng chưa cung cấp timeline** (còn "*Chưa rõ*"/"*Giả định*"): tự đề xuất thời lượng theo các bước sau. Chỉ áp dụng được khi tổng effort đã ở dạng **man-day** (phương pháp bottom-up) — công thức cần chia effort cho số người × ngày làm việc. Nếu đang dùng phương pháp PERT (dự án >100 màn hình, tổng ở dạng story point), không tự đề xuất thời lượng được vì chưa có man-day để tính; trong trường hợp đó, dừng lại và yêu cầu người dùng cung cấp timeline mong muốn trực tiếp, hoặc hoàn tất quy đổi story point → man-day trước.

Mục tiêu khi tự đề xuất là một timeline vừa phải — không ép quá chặt (rủi ro trễ/chất lượng), cũng không kéo quá dài (mất lợi thế cạnh tranh, tăng chi phí quản lý):

1. Giả định team size ban đầu = 6 người (điểm giữa của khoảng 5-8 người được chấp nhận cho dự án dạng này).
2. Tính thời lượng đề xuất = Tổng effort sau buffer (man-day) ÷ (team size × ~22 ngày làm việc/tháng).
3. Nếu thời lượng > 12 tháng: tăng dần team size (tối đa 8 người) để rút ngắn xuống gần 12 tháng nhất có thể. Nếu vẫn > 12 tháng ngay cả với 8 người, giữ nguyên kết quả và ghi rõ đây là dự án cần thời gian dài, không cố ép ngắn lại thêm nữa (đánh đổi rủi ro chất lượng).
4. Nếu thời lượng < 12 tháng ngay từ team size 6, giữ nguyên team size 6 — không cần tăng thêm.
5. Ngày bắt đầu: dùng "Ngày mong muốn khởi động" nếu có, nếu không thì ghi "Ngày bắt đầu dự kiến: cần xác nhận khi ký hợp đồng" thay vì tự chọn một ngày cụ thể.
6. Luôn ghi rõ trong master-schedule.md rằng thời lượng này là **đề xuất của skill** (khách hàng chưa xác nhận), kèm giả định team size đã dùng — không trình bày như thể đây là con số khách hàng đã chốt.

## Dựng bảng giai đoạn

Với tổng thời lượng đã xác định (trường hợp 1 hoặc 2), nhân với % ở bảng đầu để ra thời lượng từng giai đoạn. Nếu có ngày bắt đầu, cộng dồn để ra ngày bắt đầu/kết thúc từng giai đoạn.
