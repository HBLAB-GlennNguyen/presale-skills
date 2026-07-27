# Rubric đánh giá rủi ro (Risk Matrix: Likelihood × Impact)

Mỗi rủi ro dưới đây được chấm theo **2 trục độc lập**: Khả năng xảy ra (Likelihood) và Mức độ ảnh hưởng (Impact), mỗi trục từ 1 đến 5. Điểm rủi ro = Likelihood × Impact (1-25). Nếu không đủ thông tin để chấm một trục, ghi "?" và giải thích lý do — không tự suy đoán.

## Thang điểm chung (áp dụng cho mọi rủi ro)

**Likelihood (khả năng xảy ra):**
- 1: Khó xảy ra — thông tin hiện có cho thấy đây khó là vấn đề thực sự
- 3: Có thể xảy ra — thông tin chưa đủ để loại trừ, cần theo dõi
- 5: Gần như chắc chắn xảy ra — thông tin hiện có cho thấy đây gần như chắc chắn là vấn đề

**Impact (mức độ ảnh hưởng nếu xảy ra):**
- 1: Ảnh hưởng nhỏ — không tác động đáng kể tới scope/timeline/chất lượng
- 3: Ảnh hưởng vừa — cần điều chỉnh kế hoạch nhưng dự án vẫn kiểm soát được
- 5: Ảnh hưởng nghiêm trọng — có thể khiến dự án trễ lớn/vượt ngân sách/thất bại

## Danh sách rủi ro

### 1. Phạm vi bị hiểu sai hoặc thay đổi giữa chừng
- Gợi ý Likelihood: cao nếu phạm vi trong scope-and-sitemap.md còn mơ hồ/nhiều mục "Chưa rõ"; thấp nếu phạm vi mô tả chi tiết, rõ ràng.
- Gợi ý Impact: cao hơn nếu mô hình hợp tác là Fixed Price (cam kết giá cố định trên phạm vi sai sẽ tốn kém); thấp hơn nếu là T&M/ODC (phạm vi điều chỉnh được).

### 2. Đội ngũ chậm tiến độ do công nghệ mới/thiếu kinh nghiệm
- Gợi ý Likelihood: cao nếu phần lớn công nghệ yêu cầu mới hoặc đội ngũ chưa từng triển khai; thấp nếu stack quen thuộc.
- Gợi ý Impact: cao nếu công nghệ mới nằm ở phần lõi hệ thống; thấp nếu chỉ ở phần phụ trợ.

### 3. Dự án trễ deadline do timeline quá gấp
- Gợi ý Likelihood: cao nếu timeline khách hàng mong muốn rõ ràng gấp so với khối lượng công việc ước tính sơ bộ; thấp nếu timeline thoải mái hoặc chưa xác định (chưa có áp lực cụ thể).
- Gợi ý Impact: cao nếu deadline gắn với sự kiện kinh doanh quan trọng của khách hàng (ra mắt sản phẩm, mùa cao điểm); thấp nếu deadline linh hoạt.

### 4. Tích hợp hệ thống ngoài phát sinh vấn đề kỹ thuật
- Gợi ý Likelihood: cao nếu cần tích hợp nhiều hệ thống, hệ thống legacy, hoặc thiếu tài liệu API; thấp nếu không cần tích hợp hoặc tích hợp đơn giản, tài liệu rõ ràng.
- Gợi ý Impact: cao nếu hệ thống tích hợp là lõi nghiệp vụ (vd hệ thống kế toán, thanh toán); thấp nếu chỉ là tích hợp phụ trợ.

### 5. Vi phạm yêu cầu tuân thủ/quy định
- Gợi ý Likelihood: cao nếu ngành có quy định nghiêm ngặt (tài chính, y tế) và đội ngũ chưa quen; thấp nếu không có yêu cầu tuân thủ đặc biệt.
- Gợi ý Impact: luôn ở mức cao-rất cao nếu có liên quan pháp lý/compliance, vì hậu quả (phạt, mất hợp đồng) thường nghiêm trọng.

### 6. Vượt ngân sách hoặc tranh chấp thanh toán
- Gợi ý Likelihood: cao nếu ngân sách chưa rõ ràng hoặc thấp bất thường so với phạm vi mô tả; thấp nếu ngân sách nêu rõ và hợp lý.
- Gợi ý Impact: cao hơn nếu mô hình hợp tác là Fixed Price (vendor gánh chênh lệch); thấp hơn với T&M/ODC.

### 7. Chất lượng giải pháp không đạt do thiếu kinh nghiệm domain
- Gợi ý Likelihood: cao nếu domain hoàn toàn mới với đội ngũ; thấp nếu đã có kinh nghiệm trực tiếp trong ngành/domain của khách hàng.
- Gợi ý Impact: cao nếu domain có nghiệp vụ đặc thù phức tạp (vd tài chính, bảo hiểm); thấp nếu nghiệp vụ đơn giản, dễ tiếp cận.

### 8. Chậm phối hợp do khách hàng thiếu năng lực IT nội bộ
- Gợi ý Likelihood: cao nếu khách hàng không có đội ngũ IT nội bộ (doanh nghiệp truyền thống/end-client không chuyên CNTT); thấp nếu khách hàng có đội ngũ IT đầy đủ, quen làm việc với vendor.
- Gợi ý Impact: cao nếu dự án cần khách hàng cung cấp quyết định/phản hồi kỹ thuật thường xuyên; thấp nếu ít phụ thuộc vào input kỹ thuật từ khách hàng.

## Ma trận rủi ro và mức tổng thể

Điểm rủi ro từng mục = Likelihood × Impact. Tra bảng để ra mức:

| Điểm (L × I) | Mức rủi ro |
|---|---|
| 1 – 4 | Thấp |
| 5 – 9 | Trung bình |
| 10 – 14 | Cao |
| 15 – 25 | Nghiêm trọng |

**Mức rủi ro tổng thể của dự án** = mức cao nhất xuất hiện trong danh sách 8 rủi ro (ví dụ: chỉ cần 1 rủi ro rơi vào "Nghiêm trọng" thì dự án được kết luận mức "Nghiêm trọng", bất kể các rủi ro khác thấp hơn). Nêu rõ rủi ro nào là nguyên nhân kéo mức tổng thể lên.

## Lưu ý về mô hình hợp tác

Nếu rủi ro #1 (Phạm vi bị hiểu sai) có Impact ≥ 4 **và** mô hình hợp tác là Fixed Price, nêu bật tổ hợp này riêng trong phần tổng kết — đây là tổ hợp rủi ro cao nhất đối với vendor (cam kết giá cố định trên phạm vi chưa rõ).
