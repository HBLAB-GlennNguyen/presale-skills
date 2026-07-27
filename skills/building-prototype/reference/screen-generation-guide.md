# Hướng dẫn dựng từng màn hình

Áp dụng cho mỗi dòng trong bảng "Danh sách màn hình & Sitemap" của `scope-and-sitemap.md`, sau khi đã có UI kit (`ui-kit-brief.md`).

## Khung layout chuẩn (dùng chung mọi màn hình)

- **Header:** logo (theo `ui-kit-qna.md`) + tên hệ thống bên trái, khu vực user menu placeholder (avatar + tên "Người dùng") bên phải.
- **Điều hướng chính:**
  - Loại phần mềm Nội bộ → sidebar dọc bên trái, liệt kê các module chính (từ "Danh sách chức năng/module chính"), module hiện tại được highlight.
  - Loại phần mềm Public → thanh nav ngang trên cùng, gọn hơn, ít mục hơn.
- **Breadcrumb:** Trang chủ / Tên module / Tên màn hình — giúp hình dung vị trí trong sitemap khi demo.
- **Content area:** nội dung riêng theo loại màn hình (xem bên dưới).
- **Footer:** không bắt buộc, có thể bỏ qua để tập trung vào content.

## Theo loại màn hình

### Màn hình chính
Nội dung tổng quan của module đó — có thể là dashboard nhỏ (vài chỉ số/thẻ tổng hợp liên quan đến module) hoặc trang landing của module dẫn vào các màn hình quản lý con. Có link/nút dẫn tới các màn hình quản lý cùng module.

### Màn hình quản lý (danh sách/CRUD)
- Bảng dữ liệu với 5-10 dòng mock data (xem "Mock data" bên dưới), cột phù hợp với thực thể đang quản lý.
- Thanh công cụ phía trên bảng: ô tìm kiếm, filter cơ bản, nút "+ Tạo mới" (dẫn tới màn hình Pop-up dạng form tương ứng nếu có).
- Mỗi dòng có action (Xem/Sửa/Xóa) — nút Sửa dẫn tới Pop-up dạng form tương ứng (chế độ edit).
- Phân trang ở cuối bảng (chỉ cần UI tĩnh, không cần logic phân trang thật).

### Pop-up dạng form
- Trình bày dạng modal (che phủ 1 phần màn hình nền) hoặc trang riêng nếu modal không phù hợp với luồng.
- Các trường input suy ra từ tên màn hình/module (vd màn hình "Tạo vận đơn" → các trường: mã vận đơn, người gửi, người nhận, địa chỉ, trạng thái...).
- 2 nút hành động: "Lưu" và "Hủy". "Hủy" quay lại màn hình quản lý cha.

## Mock data

Sinh 5-10 dòng dữ liệu mẫu hợp lý bằng tiếng Việt, gắn với ngữ cảnh khách hàng (ngành nghề, tên module) đã có trong `requirements-summary.md`/`scope-and-sitemap.md` — không dùng dữ liệu chung chung kiểu "Item 1, Item 2". Đặt trực tiếp trong `script.js` của màn hình dưới dạng mảng JS.

## Điều hướng giữa các màn hình

Dựa vào cột "Thuộc module/chức năng" trong sitemap để nhóm các màn hình cùng module và tạo liên kết qua lại hợp lý (menu, breadcrumb, nút hành động) — không tạo liên kết tùy tiện giữa các màn hình không liên quan.

## Mức độ JS logic — xem `interactivity-guide.md`

Chỉ màn hình thuộc workflow chính (đã xác nhận với người dùng ở bước trước) mới cần validate form đầy đủ, xử lý filter/sort thật trên mock data, và phản hồi tương tác (vd hiện thông báo khi Lưu thành công). Màn hình khác chỉ cần UI tĩnh + link điều hướng đúng.
