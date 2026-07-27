# Mức độ tương tác: Workflow chính vs Màn hình phụ

Mỗi màn hình thuộc đúng 1 trong 2 nhóm dưới đây — xác định dựa trên danh sách 2-4 workflow chính đã xác nhận với người dùng trước khi generate.

## Màn hình thuộc workflow chính — tương tác đầy đủ

- **Form:** validate client-side thật (required field, định dạng email/số điện thoại/số nếu có trường tương ứng) bằng vanilla JS, hiển thị lỗi ngay dưới từng trường khi không hợp lệ.
- **Lưu dữ liệu:** khi submit hợp lệ, ghi bản ghi mới vào `localStorage` (key đặt theo tên module, vd `localStorage['vandon_data']`), sau đó điều hướng về màn hình quản lý cha kèm thông báo "Tạo thành công" (banner tạm thời hoặc alert đơn giản).
- **Màn hình quản lý:** khi tải trang, đọc mock data gốc (hardcode trong script.js) + gộp thêm dữ liệu đã lưu trong `localStorage` (nếu có) để bảng hiển thị phản ánh đúng các thay đổi người dùng vừa thao tác trong phiên demo.
- **Filter/Search/Sort:** xử lý thật bằng JS trên tập dữ liệu đã gộp (lọc/sắp xếp mảng rồi render lại bảng), không cần gọi API vì không có backend.
- **Xóa (nếu có):** xóa khỏi `localStorage` (không xóa mock data gốc), cập nhật lại bảng ngay.

Vì mỗi màn hình là 1 file HTML riêng (theo cấu trúc dự án), dùng `localStorage` là cách đơn giản nhất để mô phỏng dữ liệu "sống" xuyên suốt giữa các trang mà không cần backend hay SPA.

## Màn hình phụ — chỉ cần UI + điều hướng

- Hiển thị mock data tĩnh (hardcode trong script.js), không đọc/ghi `localStorage`.
- Không cần validate — nếu có form, nút "Lưu" chỉ điều hướng về màn hình cha (không cần lưu dữ liệu thật).
- Vẫn cần đầy đủ link điều hướng đúng (breadcrumb, menu, nút hành động) để người xem click qua lại được toàn bộ sitemap — chỉ khác là không có logic xử lý dữ liệu phía sau.

## Reset dữ liệu demo

Thêm 1 nút nhỏ (góc dưới trái, không nổi bật) "Reset dữ liệu demo" ở các màn hình quản lý thuộc workflow chính — xóa key `localStorage` liên quan, quay về mock data gốc. Giúp demo lại từ đầu khi cần trình bày nhiều lần.
