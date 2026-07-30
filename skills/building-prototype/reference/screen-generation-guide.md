# Hướng dẫn dựng từng màn hình

Áp dụng cho mỗi dòng trong bảng "Danh sách màn hình & Sitemap" của `scope-and-sitemap.md`, sau khi đã có UI kit (`ui-kit-brief.md`).

**Ngôn ngữ nội dung hiển thị:** mọi ví dụ label/nút/breadcrumb bằng tiếng Việt trong tài liệu này (vd "Lưu"/"Hủy", "Trang chủ", "Đăng nhập") chỉ là minh hoạ mặc định — dịch sang ngôn ngữ đã chọn ở câu 7 trong `ui-kit-qna.md` nếu khác Tiếng Việt, áp dụng nhất quán cho toàn bộ nội dung hiển thị trên màn hình (không áp dụng cho tên thư mục/file, vẫn giữ theo sitemap tiếng Việt).

## Chất lượng hoàn thiện — không được trông như wireframe

Mục tiêu là một phần mềm trông đã hoàn thiện, đủ để demo khách hàng tin đây gần với sản phẩm thật — không phải bản phác thảo layout. Trước khi coi 1 màn hình là xong, tự kiểm tra:

- Đã áp dụng đúng type scale, spacing scale (bội số 4px), elevation và bộ icon từ `ui-kit-brief.md` — không dùng font-size/margin/shadow tùy tiện khác với brief.
- Đã đối chiếu với "Sản phẩm tham khảo" trong `ui-kit-brief.md`: bố cục/khu vực chức năng của màn hình này có giống cách sản phẩm tham khảo tổ chức màn hình tương đương không?
- Card/table/form có shadow + border-radius theo elevation, không phải chỉ border 1px trơn.
- Mọi nút hành động chính, mục menu, action trên dòng bảng đều có icon kèm text (trừ khi rõ ràng chỉ cần icon, vd nút đóng modal).
- Trạng thái rỗng (bảng chưa có dữ liệu), trạng thái hover/active của nút và menu item, avatar user (ảnh placeholder hoặc chữ cái đầu tên trong hình tròn màu) đều được thiết kế, không để trống/mặc định trình duyệt.
- Không dùng dữ liệu mock kiểu "Item 1, Item 2", "Lorem ipsum" — xem mục Mock data bên dưới.
- **Kiểm tra độ phủ màu — lỗi phổ biến nhất:** nhìn tổng thể màn hình, nếu phần lớn diện tích là nền trắng/xám và màu chỉ xuất hiện lác đác ở icon/1 nút thì SAI. Khu vực điều hướng chính (sidebar/header) phải có nền màu đặc theo Primary-dark; heading/số liệu nổi bật phải dùng màu Primary-dark thay vì đen; badge/status phải có nền màu tint riêng theo trạng thái; nút bấm phải có ít nhất 2 kiểu (primary/outline hoặc primary/ghost) chứ không lặp 1 màu nút cho mọi hành động — xem chi tiết "Nguyên tắc dùng màu" trong `ui-kit-qna.md`.

## Khung layout chuẩn (dùng chung mọi màn hình)

- **Header:** cao 44-52px (thấp hơn ~20-25% so với header mặc định của các UI kit thông thường ~60-64px) để dành không gian cho content area — logo (theo `ui-kit-qna.md`) + tên hệ thống bên trái, khu vực user menu placeholder (avatar + tên "Người dùng") bên phải. Icon chuông thông báo + avatar tròn màu Primary luôn có mặt, thu nhỏ tương ứng theo chiều cao header.
- **Điều hướng chính — nền màu đặc, không dùng nền trắng, cấu trúc theo nhóm menu từ `scope-and-sitemap.md`:**
  - Đọc bảng "Thiết kế nhóm menu (Menu Grouping)" trong `scope-and-sitemap.md` (do `analyzing-rfp` tạo) — đây là cấu trúc menu THẬT phải dùng, không tự bịa cách nhóm khác. Mỗi nhóm menu = 1 mục cha dạng **accordion** trong sidebar (tên nhóm + icon), các màn hình/module thuộc nhóm đó là mục con thụt lề bên dưới. Nếu `scope-and-sitemap.md` chưa có bảng này (sitemap cũ trước khi mục này tồn tại), tự nhóm theo chức năng nghiệp vụ tương tự cách `analyzing-rfp` mô tả (Quản trị hệ thống / Dữ liệu chủ / Tài chính / Khách hàng...) rồi báo cho người dùng biết đã tự suy luận.
  - **Expand dần (accordion, không mở hết cùng lúc):** mặc định chỉ nhóm chứa màn hình đang xem được mở, các nhóm còn lại thu gọn (chỉ hiện tên nhóm + icon mũi tên chỉ hướng); click vào tên 1 nhóm khác thì mở thêm nhóm đó ra (không bắt buộc phải đóng nhóm đang mở) — giúp sidebar không bị dài quá mức khi có nhiều nhóm/nhiều màn hình.
  - Loại phần mềm Nội bộ → sidebar dọc bên trái, nền màu đặc/gradient dựng từ Primary-dark (chữ/icon màu sáng), module/mục đang chọn được highlight bằng nền Primary sáng hơn nền sidebar.
  - Loại phần mềm Public → thanh nav ngang trên cùng, nền trắng/surface nhưng logo + nút CTA chính vẫn phải nổi bật màu Primary, gọn hơn, ít mục hơn (nhóm menu áp dụng tương tự dưới dạng dropdown ngang nếu nav có nhiều mục).
  - Content area phía sau nav luôn dùng nền sáng (surface trắng hoặc gray nhạt) để tương phản với nav màu đặc — không để cả 2 khu vực cùng trắng.
- **Sidebar thu gọn/mở rộng (bắt buộc cho archetype Nội bộ/Vận hành — tham khảo Airtable/Notion):** trạng thái mở rộng hiển thị đủ icon + nhãn nhóm/module như bình thường; trạng thái thu gọn co lại còn một dải hẹp (~64-72px) chỉ hiện icon căn giữa, ẩn nhãn, module/mục đang chọn vẫn giữ highlight bằng nền sáng hơn. Đây là hành vi chrome dùng chung mọi màn hình (không phụ thuộc màn hình đó có thuộc workflow chính hay không, giống link điều hướng) — cài đặt bằng JS trong `assets/js/global.js`, toggle class trên sidebar và lưu trạng thái vào `localStorage` (key `sidebar_collapsed`) để giữ nguyên khi chuyển qua các màn hình khác trong phiên demo.
  - **Nút toggle:** đặt ở **góc trên-phải của sidebar** (không đặt cuối sidebar) — chỉ icon mũi tên trái/phải (xoay 180° theo trạng thái), KHÔNG kèm chữ. Mặc định mờ (opacity thấp, vd 0.4) để không gây chú ý; khi hover thì sáng hẳn lên (opacity 1, có nền nhấn nhẹ) và hiện tooltip riêng thiết kế theo bảng màu (không dùng tooltip mặc định của trình duyệt) cho biết hành động ("Thu gọn menu"/"Mở rộng menu" tùy trạng thái).
  - **Tooltip cho từng mục nav khi đã thu gọn:** vì nhãn bị ẩn, mỗi icon phải hiện tooltip tên mục khi hover (cùng kiểu tooltip thiết kế riêng như nút toggle), để người dùng không phải đoán icon.
  - **Sub-menu cho module có nhiều màn hình con:** nếu 1 module trong 1 nhóm menu có từ 2 màn hình quản lý con trở lên, gom thành 1 mục cha có sub-menu riêng (lớp thứ 3, lồng trong nhóm menu) thay vì liệt kê phẳng. Ở trạng thái mở rộng, click vào mục cha xổ/thu gọn danh sách con thụt lề ngay bên dưới (accordion inline). Ở trạng thái thu gọn, hover vào icon mục cha xổ ra 1 flyout panel bên cạnh (bên phải icon, nền sáng/surface tương phản với sidebar tối, có shadow cấp modal) chứa tên module + danh sách màn hình con để bấm vào — không cần click, chỉ cần hover là đủ.
- **Breadcrumb:** Trang chủ / Tên module / Tên màn hình — giúp hình dung vị trí trong sitemap khi demo.
- **Content area:** nội dung riêng theo loại màn hình (xem bên dưới).
- **Footer:** không bắt buộc, có thể bỏ qua để tập trung vào content.

## Theo loại màn hình

### Đăng nhập / Trang chủ public (màn hình vào app — không nằm sẵn trong sitemap thì vẫn phải tạo)
Đây là màn hình đầu tiên người xem gặp, quyết định ấn tượng ban đầu — không được sơ sài:
- Nếu `requirements-summary.md` có vai trò người dùng cần đăng nhập/phân quyền: dựng màn hình **Đăng nhập** riêng (`screens/auth/dang-nhap/`) theo bố cục 2 cột (split-panel), KHÔNG dựng dạng form trắng trơn giữa màn hình: cột bên trái/phải nền màu đặc/gradient Primary-dark chứa logo, tên hệ thống, 1 câu tagline, 2-3 điểm nổi bật (bullet có icon) và có thể thêm 1-2 hình khối trang trí (circle/blob mờ) cho sinh động; cột còn lại nền trắng chứa form email/username + password, nút "Đăng nhập" (`btn-primary`) full-width. Submit điều hướng thẳng tới Dashboard (không cần validate thật trừ khi Đăng nhập là 1 trong các workflow chính đã xác nhận).
- Nếu phần mềm không có đăng nhập (public, ai cũng dùng được): dựng **Trang chủ** giới thiệu ngắn gọn hệ thống + lối vào các module/chức năng chính, thay cho vai trò "màn hình vào app".

### Dashboard / Trang tổng quan (màn hình đầu tiên sau đăng nhập — không nằm sẵn trong sitemap thì vẫn phải tạo)
Đây là màn hình khách hàng nhìn lâu nhất khi demo, phải hiện đại và có sức thuyết phục:
- 3-5 **thẻ KPI/stat card** (icon + số liệu + nhãn + % thay đổi so với kỳ trước nếu hợp lý), mỗi thẻ có dải màu accent riêng theo "Nguyên tắc dùng màu" trong `ui-kit-qna.md` (không để cả dãy thẻ trắng giống hệt nhau) — cho các chỉ số quan trọng nhất mà hệ thống đang quản lý (suy ra từ các module/entity chính trong `scope-and-sitemap.md`, vd hệ quản lý đơn hàng → tổng đơn hôm nay, doanh thu, đơn chờ xử lý, tỷ lệ hoàn thành).
- Ít nhất 1-2 **biểu đồ** visualize dữ liệu theo thời gian hoặc theo danh mục (line/bar/donut) dựng bằng SVG/canvas thuần hoặc CSS — áp dụng nguyên tắc màu sắc/spacing của skill `dataviz` cho phần biểu đồ này.
- 1 khu vực **hoạt động gần đây** hoặc **danh sách cần xử lý** (bảng rút gọn 5 dòng, dẫn link sang màn hình quản lý đầy đủ tương ứng).
- Shortcut/nút truy cập nhanh tới 2-3 tác vụ hay dùng nhất (vd "+ Tạo mới ...") dẫn thẳng tới Pop-up dạng form tương ứng.

### Màn hình chính (của từng module, không phải Dashboard tổng)
Nội dung tổng quan của module đó — vài chỉ số/thẻ tổng hợp liên quan đến module (có icon, theo đúng elevation trong `ui-kit-brief.md`) hoặc trang landing của module dẫn vào các màn hình quản lý con. Có link/nút dẫn tới các màn hình quản lý cùng module.

### Màn hình quản lý (danh sách/CRUD)
- Bảng dữ liệu với 5-10 dòng mock data (xem "Mock data" bên dưới), cột phù hợp với thực thể đang quản lý. Header bảng dính (sticky) khi cuộn để vẫn thấy tên cột với bảng dài.
- **Thanh công cụ (toolbar) ngang, gọn, tối ưu không gian — tham khảo Airtable:** một dòng ngang mỏng ngay trên bảng, gồm các chip/icon-button nhỏ thay vì dropdown/select to chiếm nhiều chỗ dọc: ô tìm kiếm (icon kính lúp, mở rộng thành input khi click), chip "Lọc" (filter), chip "Sắp xếp" (sort), chip "Nhóm theo" (group — nếu dữ liệu có trường phân loại rõ, vd trạng thái/loại), rồi nút "+ Tạo mới" (`btn-primary`) ở cuối bên phải. Với archetype Nội bộ/Vận hành, đây là mặc định bắt buộc thay vì thanh filter kiểu form to; các archetype khác có thể dùng filter bar đơn giản hơn (select/input) như trước nếu phù hợp hơn.
- Mỗi dòng có action (Xem/Sửa/Xóa) — nút Sửa dẫn tới Pop-up dạng form tương ứng (chế độ edit).
- Phân trang ở cuối bảng (chỉ cần UI tĩnh, không cần logic phân trang thật).
- Archetype Nội bộ/Vận hành ưu tiên mật độ cao: padding dòng bảng ở cận dưới của spacing scale (vd `--sp-2`/`--sp-3` thay vì `--sp-4`) để hiện được nhiều dòng hơn trong màn hình, không đồng nghĩa với bỏ shadow/elevation của card bảng.

### Pop-up dạng form
- Trình bày dạng modal (che phủ 1 phần màn hình nền) hoặc trang riêng nếu modal không phù hợp với luồng.
- Các trường input suy ra từ tên màn hình/module (vd màn hình "Tạo vận đơn" → các trường: mã vận đơn, người gửi, người nhận, địa chỉ, trạng thái...).
- Nếu form có nhiều nhóm trường tách biệt rõ ràng, độc lập với nhau (vd chi tiết 1 đối tượng: thông tin chung / thành phần con / nội dung đồng bộ kênh / hình ảnh), chia thành **tabs ngang bên trong modal** thay vì 1 form dài cuộn — mỗi tab chỉ hiện panel tương ứng (ẩn/hiện bằng JS, không load lại trang), tab đang chọn có gạch chân màu Primary. Dùng toggle switch (on/off) thay cho checkbox thô cho các trường dạng bật/tắt.
- 2 nút hành động: "Lưu" và "Hủy". "Hủy" quay lại màn hình quản lý cha.

### Màn hình Cấu hình/Cài đặt (nhận diện qua tên: "Cấu hình", "Cài đặt", "Settings")
Không dựng dạng 1 form dài liệt kê hết mọi tuỳ chọn — chia bố cục 2 cột: **side-nav dọc bên trái** (không phải sidebar điều hướng chính) liệt kê các nhóm cấu hình liên quan (vd Thông tin tài khoản / Người dùng & phân quyền / Thông báo / Ngôn ngữ & khu vực..., suy ra từ các mục con thuộc module này trong `scope-and-sitemap.md`), **panel nội dung bên phải** hiển thị đúng 1 nhóm đang chọn (ẩn/hiện qua JS khi click, không load lại trang). Dùng toggle switch cho các tuỳ chọn bật/tắt, bảng cho danh sách (vd danh sách người dùng), form-grid cho các trường cấu hình đơn giản.

## Mock data

Sinh 5-10 dòng dữ liệu mẫu hợp lý theo ngôn ngữ đã chọn ở câu 7 trong `ui-kit-qna.md` (tên người/công ty/địa chỉ dùng ngôn ngữ/văn hoá tương ứng — vd tên Việt cho Tiếng Việt, tên quốc tế cho Tiếng Anh), gắn với ngữ cảnh khách hàng (ngành nghề, tên module) đã có trong `requirements-summary.md`/`scope-and-sitemap.md` — không dùng dữ liệu chung chung kiểu "Item 1, Item 2". Đặt trực tiếp trong `script.js` của màn hình dưới dạng mảng JS.

## Điều hướng giữa các màn hình

Sidebar/nav dựng theo bảng "Thiết kế nhóm menu" (xem "Khung layout chuẩn" ở trên) — đây là cấp nhóm cao nhất. Trong mỗi nhóm, dùng cột "Thuộc module/chức năng" của sitemap để gom các màn hình cùng module lại với nhau và tạo liên kết qua lại hợp lý (breadcrumb, nút hành động) — không tạo liên kết tùy tiện giữa các màn hình không liên quan. Dashboard không thuộc nhóm menu nào — luôn đặt là mục đầu tiên trong sidebar/nav ("Trang chủ"/"Tổng quan"), nằm ngoài mọi accordion group, và là đích điều hướng của logo/tên hệ thống ở header trên mọi màn hình.

## Mức độ JS logic — xem `interactivity-guide.md`

Chỉ màn hình thuộc workflow chính (đã xác nhận với người dùng ở bước trước) mới cần validate form đầy đủ, xử lý filter/sort thật trên mock data, và phản hồi tương tác (vd hiện thông báo khi Lưu thành công). Màn hình khác chỉ cần UI tĩnh + link điều hướng đúng. Ngoại lệ: hành vi chrome dùng chung (điều hướng, toggle thu gọn/mở rộng sidebar) luôn cần hoạt động thật bằng JS trên MỌI màn hình, không phụ thuộc phân loại workflow — xem "Khung layout chuẩn" ở trên.
