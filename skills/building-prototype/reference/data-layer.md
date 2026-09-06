# Data layer — tách dữ liệu nghiệp vụ khỏi từng màn hình

Bắt buộc cho MỌI dự án (Hệ thống quản lý lẫn Landing page) — không phải tùy chọn. Không hardcode dữ liệu đối tượng nghiệp vụ trực tiếp bên trong `script.js` của từng màn hình nữa; mỗi entity có đúng 1 file dữ liệu dùng chung, mọi màn hình liên quan đọc từ đúng file đó.

## Vì sao dùng file `.js` chứa object literal thay vì file `.json` thật + `fetch()`

Prototype phải mở được trực tiếp bằng double-click file HTML (`file://`), không chạy qua HTTP server — đây là giá trị cốt lõi của 1 bản demo "clickable". `fetch()` một file `.json` cục bộ qua `file://` bị trình duyệt (đặc biệt Chrome/Edge) chặn bằng lỗi CORS, làm hỏng cả bản demo ngay khi khách double-click mở lên. Do đó dùng file `.js` chứa đúng cấu trúc dữ liệu dạng JSON (object/array literal hợp lệ, gán vào 1 hằng số), nạp bằng thẻ `<script>` — chạy được ngay qua `file://`, không cần server, không đổi bản chất "dữ liệu tách riêng, có cấu trúc, định nghĩa theo object" mà chỉ đổi cách nạp cho phù hợp môi trường chạy thật của prototype.

## Xác định danh sách entity

- **Hệ thống quản lý:** lấy đúng danh sách trong bảng "Phân tích đối tượng nghiệp vụ & vòng đời" của `scope-and-sitemap.md` (do `analyzing-rfp` tạo) — mỗi dòng trong bảng đó = 1 entity cần 1 file data riêng. Nếu bảng ghi "*Không có đối tượng nghiệp vụ riêng*", dự án đó không cần entity data riêng (hiếm, chỉ đúng khi toàn bộ chức năng là xem/báo cáo).
- **Landing page:** entity là các loại nội dung lặp lại nhiều bản ghi trong sitemap — thường gặp: bài viết blog, dịch vụ/gói sản phẩm, testimonial/đánh giá khách hàng, gói giá. Không phải landing page nào cũng có entity — 1 trang chủ đơn thuần không bảng giá/blog thì không cần file data nào; chỉ tạo cho nội dung thực sự lặp lại nhiều bản ghi.

## Quy ước file & schema

- Đường dẫn: `./output/prototype/assets/data/<slug-entity>.js` — slug là tên tiếng Việt không dấu, kebab-case (vd "Đơn hàng" → `don-hang.js`, "Bài viết" → `bai-viet.js`).
- Tên biến JS: `DATA_<TÊN_ENTITY_KHÔNG_DẤU_IN_HOA>` (vd `DATA_DON_HANG`, `DATA_BAI_VIET`).
- Đầu mỗi file, viết 1 comment block định nghĩa schema (tên trường + kiểu dữ liệu) TRƯỚC mảng dữ liệu — lấy cột "Số trường ước tính" trong bảng entity của `scope-and-sitemap.md` làm căn cứ độ lớn, không tự bịa quá nhiều/quá ít trường so với ước tính đó; với entity của Landing page (không có trong bảng đó), tự định nghĩa schema hợp lý theo ngữ cảnh nội dung.
- Nội dung: `const DATA_<ENTITY> = [ { ... }, { ... }, ... ];` — 5-10 bản ghi mock hợp lý theo `reference/screen-generation-guide.md` mục Mock data (đa dạng trạng thái, có trường hợp biên), viết bằng ngôn ngữ đã chọn ở câu 7 trong `ui-kit-qna.md`.
- File này KHÔNG dùng `export`/`import` (tránh ES module cần server) — chỉ khai báo `const` ở global scope; các file khác dùng trực tiếp qua thẻ `<script>` đã load trước đó.

## Cách mỗi màn hình dùng data layer

- Trong `index.html` của màn hình, thêm 1 thẻ `<script src="...">` trỏ tới đúng file `assets/data/<entity>.js` cho MỌI entity màn hình đó cần, đặt TRƯỚC thẻ `<script src="script.js">` của chính màn hình (để `DATA_<ENTITY>` đã tồn tại khi `script.js` chạy).
- `script.js` đọc `DATA_<ENTITY>` làm dữ liệu gốc, gộp thêm phần đã lưu trong `localStorage` (nếu có) theo đúng cơ chế trong `reference/interactivity-guide.md` — không sao chép lại dữ liệu gốc vào 1 mảng cục bộ khác trong `script.js`.
- Nếu `assets/data/<entity>.js` đã tồn tại từ 1 màn hình sinh trước đó (kể cả khi resume 1 phiên trước, xem `progress.md`), TÁI SỬ DỤNG nguyên file đó — không tạo file trùng/ghi đè, không viết lại 1 bộ dữ liệu khác cho cùng entity ở màn hình khác. Đây là cơ chế đảm bảo "Dữ liệu xuyên màn hình phải khớp nhau" ở `reference/screen-generation-guide.md` bằng cấu trúc, thay vì chỉ bằng kỷ luật thủ công như trước.

## Ngoại lệ — dữ liệu KHÔNG thuộc data layer

Trạng thái UI thuần túy cục bộ của 1 màn hình (giá trị tạm của filter/sort đang chọn, tab đang mở, trạng thái modal đang hiện/ẩn...) vẫn khai báo trong `script.js` của màn hình đó như bình thường — data layer chỉ áp dụng cho dữ liệu ĐỐI TƯỢNG NGHIỆP VỤ (bản ghi có thể xem/tạo/sửa/xóa), không áp dụng cho state UI tạm thời.
