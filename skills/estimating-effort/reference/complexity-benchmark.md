# Benchmark ước lượng effort theo độ phức tạp

Đây là điểm khởi đầu (starting point) để phân loại độ phức tạp — hiệu chỉnh lại theo dữ liệu thực tế của từng đội ngũ/dự án khi có.

Có 2 cách dùng bảng này, tùy phương pháp ước lượng được chọn (xem `SKILL.md`):
- **Bottom-up theo function** (dự án ≤ 100 màn hình): dùng cột "Man-day (function)" — ước trực tiếp bằng man-day.
- **3-point/PERT theo màn hình** (dự án > 100 màn hình): dùng cột "Story point O/M/P (màn hình)" — ước 3 giá trị Lạc quan/Khả dĩ nhất/Bi quan cho mỗi màn hình rồi tính theo công thức PERT: `(O + 4M + P) / 6`. Đơn vị story point, KHÔNG quy đổi ra giờ/man-day — việc quy đổi để người thực hiện ước lượng tự điền sau.

## Các mức độ phức tạp

### 1. Rất đơn giản
- **Tiêu chí:** Chỉ hiển thị thông tin tĩnh hoặc đọc dữ liệu đơn giản, không có business logic, không có input từ người dùng (vd: trang giới thiệu, màn hình xem thông tin read-only, dashboard tĩnh).
- **Man-day (function):** 0.5 – 1
- **Story point O / M / P (màn hình):** 0.5 / 1 / 1.5

### 2. Đơn giản
- **Tiêu chí:** CRUD cơ bản trên 1 bảng dữ liệu, ít trường (dưới ~10 trường), validate đơn giản, không có business rule phức tạp.
- **Man-day (function):** 1 – 2
- **Story point O / M / P (màn hình):** 1 / 2 / 3

### 3. Trung bình
- **Tiêu chí:** Có business logic vừa phải (tính toán, điều kiện rẽ nhánh), liên kết dữ liệu từ 2-3 bảng, có filter/search/sort, validate nhiều trường.
- **Man-day (function):** 2 – 4
- **Story point O / M / P (màn hình):** 2 / 3 / 5

### 4. Phức tạp
- **Tiêu chí:** Nhiều business rule lồng nhau, liên kết dữ liệu từ nhiều bảng/module, tích hợp với 1 hệ thống ngoài, workflow nhiều bước (multi-step form/approval).
- **Man-day (function):** 4 – 8
- **Story point O / M / P (màn hình):** 3 / 5 / 8

### 5. Rất phức tạp
- **Tiêu chí:** Workflow nhiều actor/nhiều trạng thái (state machine), tích hợp nhiều hệ thống ngoài đồng thời, xử lý real-time/bất đồng bộ, thuật toán/tính toán phức tạp, hoặc yêu cầu hiệu năng đặc biệt.
- **Man-day (function):** 8 – 15
- **Story point O / M / P (màn hình):** 5 / 8 / 13

## Dùng bảng Phân tích đối tượng nghiệp vụ để chọn tier

Nếu function/màn hình đang xét quản lý một đối tượng có mặt trong bảng "Phân tích đối tượng nghiệp vụ & vòng đời" của `scope-and-sitemap.md` (khớp theo cột "Thuộc chức năng/module"), dùng thông tin đó làm căn cứ chọn tier thay vì suy đoán từ tên chức năng:
- Số trường Ít, vòng đời ≤ 2 trạng thái, không có ràng buộc đặc thù → nghiêng về **Đơn giản**
- Số trường Vừa, vòng đời 3-4 trạng thái → nghiêng về **Trung bình**
- Số trường Nhiều, HOẶC vòng đời nhiều trạng thái dạng state machine (phê duyệt nhiều bước, nhiều actor), HOẶC có ràng buộc đặc thù (chứng chỉ, tiêu chuẩn, compliance) → nghiêng về **Phức tạp**/**Rất phức tạp**
- Nếu không khớp rõ với bullet nào ở trên, kết hợp thông tin từ bảng với tiêu chí 5 mức trong phần trên của tài liệu này để chọn tier phù hợp nhất.

Cột "Ghi chú độ phức tạp gợi ý" trong bảng chỉ mang tính tham khảo — tier vẫn phải được suy ra từ 3 cột Số trường / Vòng đời / Ràng buộc đặc thù ở trên, không copy trực tiếp từ cột ghi chú.

Ví dụ: "Quản lý sản phẩm" cho khách hàng ngành nội thất (đối tượng Sản phẩm: ít trường, vòng đời Nháp→Đang bán→Ngừng bán, không ràng buộc) → Đơn giản/Trung bình. Cùng chức năng "Quản lý sản phẩm" nhưng khách hàng ngành thiết bị hàng không (đối tượng Sản phẩm: nhiều trường, vòng đời Nháp→Chờ kiểm định→Đã cấp chứng chỉ→Đang lưu kho→Thu hồi/Hết hạn, ràng buộc chứng chỉ an toàn/kiểm định định kỳ) → Rất phức tạp — dù tên chức năng giống hệt nhau.

Nếu function/màn hình không khớp với đối tượng nào trong bảng (vd màn hình dashboard, báo cáo tổng hợp), tiếp tục dùng tiêu chí 5 mức như hiện tại.

## Cách chọn giá trị trong range

Khi một function/màn hình rơi vào 1 mức, chọn giá trị trong range dựa trên vị trí tương đối so với các function/màn hình khác đã phân loại cùng mức (ví dụ: 2 function cùng "Trung bình" nhưng 1 cái rõ ràng nặng hơn cái kia thì cái nặng hơn lấy giá trị cao hơn trong range 2-4). Nếu không đủ thông tin để phân biệt, dùng giá trị giữa range.
