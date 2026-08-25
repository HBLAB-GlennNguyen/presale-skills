# Menu ngang + bảng dữ liệu dày đặc (kiểu Airtable)

Áp dụng khi "Kiểu điều hướng chính" trong `ui-kit-brief.md` (xem `ui-kit-qna.md`) đã chọn menu ngang, ẩn sidebar dọc — thay cho phần sidebar trong "Khung layout chuẩn" của `screen-generation-guide.md`. Áp dụng nhất quán cho TOÀN BỘ prototype, không trộn với sidebar dọc ở vài màn hình khác.

## Chrome ngang thay sidebar

- 1 thanh ngang duy nhất, cao 48-56px, nền màu đặc/gradient dựng từ Primary-dark (như sidebar trước đây) — chứa: brand-mark + TÊN SẢN PHẨM bên trái, các nhóm menu ở giữa (từ bảng "Thiết kế nhóm menu" trong `scope-and-sitemap.md`, mỗi nhóm là 1 mục ngang; nhóm có nhiều module con hiện dropdown khi click/hover, mục đang chọn được highlight bằng nền sáng hơn), avatar/icon thông báo + nút Đăng xuất bên phải.
- Breadcrumb giữ nguyên, đặt ngay dưới thanh ngang như `screen-generation-guide.md` đã mô tả.
- Không dựng thêm sidebar dọc song song ở bất kỳ màn hình nào — toàn bộ chiều ngang còn lại (trừ padding) dành cho bảng/lưới dữ liệu.
- Responsive: khi thu hẹp xuống mobile, thanh ngang này chuyển thành hamburger + drawer theo đúng cơ chế trong `reference/responsive-and-pwa.md` — dropdown nhóm menu ngang trở thành accordion dọc trong drawer.

## Bảng dữ liệu nâng cao (bổ sung cho phần "Màn hình quản lý (danh sách/CRUD)" trong `screen-generation-guide.md`, không thay thế — toolbar/phân trang/mock data vẫn theo đúng file đó)

Chỉ áp dụng đầy đủ 4 tính năng dưới đây cho màn hình thuộc workflow chính đã xác nhận (theo phân loại trong `interactivity-guide.md`); màn hình phụ vẫn chỉ cần UI tĩnh như bình thường.

- **Sort qua header:** click trực tiếp vào tiêu đề cột đổi chiều sắp xếp (asc/desc/về mặc định theo vòng lặp 3 bước), hiện mũi tên chỉ hướng cạnh tên cột đang sort — bổ sung cho chip "Sắp xếp" trong toolbar đã có (2 cách cùng dẫn tới 1 hàm sort JS, không tách rời logic).
- **Inline edit:** click/double-click 1 ô (trừ cột ID/mã không cho sửa) → ô chuyển thành input tại chỗ đúng kiểu dữ liệu cột đó (text/select/date); Enter hoặc blur ra ngoài → lưu giá trị mới vào `localStorage` (theo đúng cơ chế merge trong `interactivity-guide.md`) và render lại; Esc → huỷ, giữ giá trị cũ. Form nhập liệu theo `reference/form-containers.md` vẫn dùng khi tạo mới bản ghi hoặc cần sửa nhiều trường cùng lúc — inline edit chỉ dành cho sửa nhanh 1 trường.
- **Group theo cột:** chip "Nhóm theo" trong toolbar chạy thật — chọn 1 cột có giá trị phân loại rõ (trạng thái, loại, người phụ trách...), render lại bảng thành các nhóm có header thu gọn/mở rộng được (accordion), mỗi header hiện tên nhóm + số dòng trong nhóm. Bỏ chọn "Nhóm theo" quay về bảng phẳng.
- **Search theo từng cột:** icon kính lúp nhỏ trong header mỗi cột (ẩn, hiện khi hover/focus header đó) mở 1 popover input lọc riêng giá trị cột đó — kết hợp AND với ô tìm kiếm toàn bảng ở toolbar nếu cả 2 đang có giá trị, không thay thế nhau.

Giữ nguyên mọi quy tắc đã có ở `interactivity-guide.md` (merge localStorage, modal xác nhận trước khi xoá, loading state khi lưu, validate on-blur) — đây là lớp tính năng bổ sung trên cùng nền đó, không viết lại cơ chế lưu trữ.
