# Chọn kiểu container cho form nhập liệu

Thay cho việc mặc định mọi form đều là modal — chọn 1 trong 5 kiểu dưới đây theo số trường dữ liệu + tính chất workflow, tự suy luận cho TỪNG màn hình form khi generate (không phải quyết định 1 lần cho cả dự án như "Kiểu điều hướng chính"). Đếm số trường bằng cách suy luận hợp lý từ tên thực thể/module trong `scope-and-sitemap.md` và ngữ cảnh nghiệp vụ trong `requirements-summary.md`.

| Kiểu | Số trường | Giữ ngữ cảnh | Tốc độ nhập |
|---|---|---|---|
| Inline Form | Rất ít (1-3) | Cực cao | Rất nhanh |
| Pop-up Modal | Ít (3-6) | Trung bình | Nhanh |
| Slide-over (Drawer) | Trung bình-nhiều (5-15) | Cao | Nhanh/linh hoạt |
| Split Screen | Trung bình | Tối đa | Cực nhanh (tạo liên tục) |
| Dedicated Page | Rất nhiều (>15 hoặc nhiều loại file) | Thấp (chuyển trang) | Chậm/kỹ lưỡng |

## Suy luận chọn kiểu (theo thứ tự ưu tiên)

1. **Workflow nhập liệu liên tục** (mô tả nghiệp vụ trong `scope-and-sitemap.md`/`requirements-summary.md` có ý "nhập hàng loạt", "tạo liên tục nhiều bản ghi", "import nhanh"...) → **Split Screen**, bất kể số trường rơi vào khoảng nào — tín hiệu workflow ưu tiên hơn đếm trường.
2. Nếu không, đếm số trường:
   - 1-3 trường, và đây là SỬA nhanh 1 field đã tồn tại (không phải tạo mới 1 bản ghi cần định danh) → **Inline Form**. Tạo mới 1 bản ghi dù chỉ 1-2 trường (cần ít nhất tên/định danh) vẫn có thể dùng Pop-up Modal nhỏ nếu ngữ cảnh cần xác nhận rõ ràng hơn — Inline Form ưu tiên cho SỬA tại chỗ.
   - 3-6 trường → **Pop-up Modal** (mặc định khi không có tín hiệu nào khác).
   - 5-6 trường (vùng chồng lấn giữa Modal và Drawer) → tie-break theo mức độ cần giữ ngữ cảnh: nếu người dùng cần vừa nhìn thấy danh sách/dữ liệu nền vừa điền (vd đối chiếu số liệu khác trong lúc nhập) → **Slide-over**; nếu không → **Pop-up Modal**.
   - 7-15 trường → **Slide-over (Drawer)**.
   - >15 trường, HOẶC nhiều loại file cần upload cùng lúc, HOẶC các nhóm trường có phụ thuộc tuần tự thật sự (nhóm sau cần lựa chọn ở nhóm trước) → **Dedicated Page**; nếu các nhóm trường có phụ thuộc tuần tự thật sự, cân nhắc dùng Wizard (`reference/specialized-screens.md`) thay vì 1 trang dài — Dedicated Page dùng khi các nhóm trường ĐỘC LẬP với nhau (không cần điền theo đúng thứ tự).

Ghi kiểu đã chọn cho từng loại form/entity chính vào `ui-kit-brief.md` nếu 1 entity xuất hiện ở nhiều màn hình (vd cả Tạo và Sửa) để dùng nhất quán 1 kiểu cho cùng 1 entity, không đổi kiểu giữa 2 màn hình của cùng 1 loại dữ liệu.

## Guideline thiết kế theo từng kiểu

### Inline Form
Đây chính là cơ chế inline-edit đã mô tả trong `reference/data-grid.md` (click/double-click ô → input tại chỗ, Enter/blur lưu, Esc huỷ) khi sửa 1 trường trong bảng — dùng lại nguyên cơ chế đó, không viết lại. Với 2-3 trường liên quan (vd thêm 1 dòng con trong bảng phụ), dùng 1 hàng input tạm ngay trong bảng kèm 2 icon nhỏ check/x để xác nhận/huỷ thay vì nút Lưu/Hủy to.

### Pop-up Modal
- Trình bày dạng modal che phủ 1 phần màn hình nền (overlay mờ phía sau).
- Các trường input suy ra từ tên màn hình/module (vd màn hình "Tạo vận đơn" → mã vận đơn, người gửi, người nhận, địa chỉ, trạng thái...).
- Nếu form có nhiều nhóm trường tách biệt rõ ràng (vd thông tin chung/thành phần con/hình ảnh), chia thành **tabs ngang bên trong modal** thay vì 1 form dài cuộn — mỗi tab chỉ hiện panel tương ứng (ẩn/hiện bằng JS), tab đang chọn gạch chân màu Primary. Dùng toggle switch thay checkbox thô cho trường bật/tắt.
- 2 nút hành động: "Lưu" và "Hủy" — "Hủy" quay lại màn hình quản lý cha.

### Slide-over (Drawer)
- Panel trượt từ cạnh phải màn hình (transition translateX, theo thời lượng/easing trong `reference/craft-and-qa.md`), rộng ~400-560px tuỳ số trường, cao full viewport.
- Overlay phía sau mờ NHẸ hơn modal (hoặc không overlay, chỉ che 1 phần content) — mục đích là vẫn hé lộ được danh sách/dữ liệu nền, giữ ngữ cảnh cho người dùng.
- Nội dung dài hơn modal nên cuộn dọc được bên trong panel; chia nhóm bằng heading phụ đơn giản (không cần tabs vì panel đã đủ cao để hiện tuần tự).
- Đóng bằng nút X ở góc trên panel hoặc click ra vùng overlay ngoài panel.
- Nút Lưu/Hủy sticky ở đáy panel khi nội dung dài hơn viewport (luôn thấy được, không phải cuộn xuống mới thấy).

### Split Screen
- Layout 2 cột cố định trong CÙNG 1 trang (không phải overlay che phủ): cột trái là danh sách/bảng hiện có (có thể thu hẹp lại để nhường chỗ), cột phải là form tạo/sửa luôn hiển thị song song, không cần mở/đóng.
- 2 lựa chọn lưu: **"Lưu & Tạo tiếp"** (lưu bản ghi vào `localStorage`, reset form về trống, focus lại trường đầu tiên, danh sách cột trái cập nhật ngay — phục vụ nhập liên tục) và **"Lưu & Đóng"** (lưu rồi thoát Split Screen, quay về danh sách full-width).
- Dòng vừa lưu trong danh sách cột trái nên có hiệu ứng highlight ngắn (background nhấp nháy nhẹ rồi tắt) để xác nhận đã lưu thành công mà không cần rời mắt khỏi form đang nhập tiếp.

### Dedicated Page
- Điều hướng sang 1 trang riêng (route/file HTML riêng theo đúng cấu trúc `screens/<module>/<tên màn hình>/`), không phải overlay.
- Chia nhóm trường bằng section có heading rõ ràng — nếu nhiều nhóm, thêm side-nav trong trang (anchor link cuộn tới từng section, giống mẫu màn hình Cấu hình/Cài đặt trong `screen-generation-guide.md`) để điều hướng nhanh giữa các nhóm thay vì cuộn dài.
- Nút Lưu/Hủy sticky ở cuối trang hoặc trong 1 thanh footer cố định — luôn tiếp cận được dù đang ở nhóm trường nào.
- Nếu cần upload nhiều loại file, mỗi loại 1 dropzone riêng theo mẫu "Quản lý file/tài liệu" trong `reference/specialized-screens.md`.
- Nếu các nhóm trường có phụ thuộc tuần tự thật sự, cân nhắc đổi sang Wizard (`reference/specialized-screens.md`) — Dedicated Page mặc định KHÔNG ép thứ tự điền giữa các nhóm.
