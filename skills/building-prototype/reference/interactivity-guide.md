# Mức độ tương tác: Workflow chính vs Màn hình phụ

Mỗi màn hình thuộc đúng 1 trong 2 nhóm dưới đây — xác định dựa trên danh sách 2-4 workflow chính đã xác nhận với người dùng trước khi generate. Nếu Loại dự án trong `ui-kit-brief.md` là Landing page/Website marketing thuần, "workflow chính" là danh sách conversion action (form Liên hệ/Đăng ký dùng thử/Đặt lịch...) đã xác nhận ở bước "Identify main workflows / conversion actions" trong `SKILL.md` — áp dụng y nguyên các mục Form/Trạng thái xử lý/Validate bên dưới, chỉ khác bước "Lưu dữ liệu": không có màn hình quản lý cha để quay về, submit hợp lệ điều hướng tới trang Trang cảm ơn (xem `reference/landing-page.md`) thay vì lưu vào `localStorage` để hiển thị lại trong 1 bảng.

**Ngôn ngữ nội dung hiển thị:** các ví dụ copy tiếng Việt dưới đây (vd "Tạo thành công", "Reset dữ liệu demo") chỉ là minh hoạ mặc định — dịch sang ngôn ngữ đã chọn ở câu 7 trong `ui-kit-qna.md` nếu khác Tiếng Việt.

## Màn hình thuộc workflow chính — tương tác đầy đủ

- **Form:** validate client-side thật (required field, định dạng email/số điện thoại/số nếu có trường tương ứng) bằng vanilla JS, hiển thị lỗi ngay dưới từng trường — kiểm tra cả khi rời khỏi trường (`blur`) chứ không chỉ lúc submit, để lỗi hiện sớm thay vì dồn hết tới cuối.
- **Trạng thái xử lý (loading):** khi bấm "Lưu"/"Gửi", disable nút hành động + đổi nhãn tạm thời (vd "Đang lưu...") trong ~400-800ms (dùng `setTimeout` giả lập độ trễ xử lý) trước khi hiện kết quả — tránh cảm giác "bấm phát ăn ngay" thiếu chân thực của 1 hệ thống có backend thật.
- **Lưu dữ liệu:** khi submit hợp lệ, ghi bản ghi mới vào `localStorage` (key đặt theo tên module, vd `localStorage['vandon_data']`), sau đó điều hướng về màn hình quản lý cha kèm thông báo "Tạo thành công" (banner tạm thời hoặc alert đơn giản).
- **Giá trị tính toán (nếu form có trường phụ thuộc lẫn nhau):** vd số lượng × đơn giá = thành tiền, tổng các dòng = tổng cộng — tính lại bằng JS ngay khi người dùng nhập, không để tĩnh chờ submit.
- **Màn hình quản lý:** khi tải trang, đọc mock data gốc từ biến `DATA_<ENTITY>` dùng chung trong `assets/data/<entity>.js` (xem `reference/data-layer.md` — KHÔNG hardcode lại mảng dữ liệu riêng trong `script.js`) + gộp thêm dữ liệu đã lưu trong `localStorage` (nếu có) để bảng hiển thị phản ánh đúng các thay đổi người dùng vừa thao tác trong phiên demo.
- **Filter/Search/Sort:** xử lý thật bằng JS trên tập dữ liệu đã gộp (lọc/sắp xếp mảng rồi render lại bảng), không cần gọi API vì không có backend.
- **Xóa (nếu có):** hiện modal/dialog xác nhận ("Xoá <tên bản ghi>? Không thể hoàn tác.") trước khi xoá thật — không xoá ngay khi bấm 1 lần. Sau khi xác nhận mới xóa khỏi `localStorage` (không xóa mock data gốc), cập nhật lại bảng ngay.

Vì mỗi màn hình là 1 file HTML riêng (theo cấu trúc dự án), dùng `localStorage` là cách đơn giản nhất để mô phỏng dữ liệu "sống" xuyên suốt giữa các trang mà không cần backend hay SPA.

## Màn hình phụ — chỉ cần UI + điều hướng

- Hiển thị mock data tĩnh đọc từ `DATA_<ENTITY>` trong `assets/data/<entity>.js` như trên (xem `reference/data-layer.md` — vẫn không được hardcode riêng dù là màn hình phụ), không đọc/ghi `localStorage`.
- Không cần validate — nếu có form, nút "Lưu" chỉ điều hướng về màn hình cha (không cần lưu dữ liệu thật).
- Vẫn cần đầy đủ link điều hướng đúng (breadcrumb, menu, nút hành động) để người xem click qua lại được toàn bộ sitemap — chỉ khác là không có logic xử lý dữ liệu phía sau.

## Reset dữ liệu demo

Thêm 1 nút nhỏ (góc dưới trái, không nổi bật) "Reset dữ liệu demo" ở các màn hình quản lý thuộc workflow chính — xóa key `localStorage` liên quan, quay về mock data gốc. Giúp demo lại từ đầu khi cần trình bày nhiều lần.
