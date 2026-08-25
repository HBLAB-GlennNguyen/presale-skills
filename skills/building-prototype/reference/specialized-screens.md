# Màn hình đặc thù (thay cho mục CRUD/Màn hình chính mặc định khi khớp loại)

Nhận diện qua tên/mô tả màn hình trong sitemap (vd "Duyệt yêu cầu", "Lịch công tác", "Bảng Kanban", "Bản đồ theo dõi xe"...) — dùng đúng mục tương ứng bên dưới thay cho "Màn hình quản lý (danh sách/CRUD)" hay "Màn hình chính" mặc định trong `screen-generation-guide.md`. Layout khung chuẩn (header/sidebar/breadcrumb), bảng màu, spacing, icon vẫn lấy từ `ui-kit-brief.md`/`ui-kit-qna.md` như mọi màn hình khác — các mục dưới đây chỉ mô tả phần nội dung/component đặc thù.

Mức độ tương tác vẫn theo đúng phân loại workflow chính/phụ trong `interactivity-guide.md` — mặc định ưu tiên tương tác qua CLICK (nút, dropdown "Chuyển trạng thái") thay vì tự viết drag-and-drop bằng tay cho những màn hình dưới đây có nhắc tới kéo-thả: drag-and-drop JS viết tay dễ vỡ/thiếu mượt trong 1 file demo tĩnh, trong khi 1 nút "Chuyển sang cột kế" đạt cùng hiệu quả thuyết phục khi demo mà rủi ro thấp hơn nhiều. Chỉ làm drag-and-drop thật nếu đây là 1 trong các workflow chính đã xác nhận VÀ người dùng yêu cầu rõ ràng.

## Dashboard nâng cao

Bổ sung cho mục "Dashboard / Trang tổng quan" trong `screen-generation-guide.md` khi sản phẩm cần mức phân tích sâu hơn 1 dashboard tổng quan cơ bản:
- KPI card có thêm mũi tên xu hướng (▲/▼ màu success/error) + % so với kỳ trước, không chỉ số tĩnh.
- Đa dạng loại chart theo đúng dữ liệu (không dùng donut cho mọi thứ): line cho xu hướng theo thời gian, bar cho so sánh danh mục, donut/pie cho tỷ trọng (tối đa 5-6 lát, gộp phần nhỏ vào "Khác"), area chart nếu cần nhấn khối lượng tích lũy — áp dụng màu/spacing của skill `dataviz`.
- Sparkline mini (1 line chart nhỏ không trục, không nhãn) lồng trong dòng bảng hoặc card để gợi xu hướng mà không chiếm nhiều chỗ.
- Chart/card có thể click để drill-down: click 1 lát donut hoặc 1 cột bar → điều hướng sang màn hình danh sách đã lọc sẵn theo đúng danh mục đó (nếu màn hình danh sách tương ứng tồn tại trong sitemap).

## Approval/Workflow (duyệt yêu cầu, quản lý ticket)

- **Danh sách:** dùng mục CRUD chuẩn, cột trạng thái là badge màu theo đúng ngữ nghĩa (chờ duyệt = warning, đã duyệt = success, từ chối = error, nháp = neutral gray) — không tự chế thêm màu ngoài 4 trạng thái semantic đã định nghĩa trong `ui-kit-qna.md`.
- **Màn hình chi tiết 1 ticket/yêu cầu:** badge trạng thái to, nổi bật ngay đầu trang (không chỉ trong bảng); **pipeline trạng thái** dạng stepper ngang (Nháp → Đã gửi → Đang xem xét → Đã duyệt/Từ chối) hiện bước hiện tại được highlight, các bước đã qua có dấu check; **lịch sử/thread hoạt động** dạng timeline dọc bên dưới hoặc cột phải — mỗi mục có avatar người thực hiện, hành động (vd "Nguyễn Văn A đã duyệt"), timestamp, ghi chú nếu có (vd lý do từ chối) — giống UI comment/audit trail, không phải bảng dữ liệu thô.
- **Nút hành động (Duyệt/Từ chối/Yêu cầu chỉnh sửa):** chỉ hiện khi trạng thái hiện tại cho phép (vd không hiện nút Duyệt nếu đã Đã duyệt) — nếu workflow chính, bấm Duyệt/Từ chối cập nhật trạng thái + thêm 1 dòng vào lịch sử ngay (localStorage), có modal xác nhận nhỏ nếu là Từ chối (bắt buộc nhập lý do).
- **SLA/hạn xử lý (nếu ngữ cảnh nghiệp vụ có):** badge đếm ngược hoặc hiện số ngày còn lại, đổi màu theo mức khẩn (còn nhiều thời gian = neutral, gần hạn = warning, quá hạn = error) — dùng đúng semantic color đã có.

## Calendar (quản lý lịch)

- Toggle 3 chế độ xem (Tháng/Tuần/Ngày) dạng tab ngang phía trên lưới lịch, mặc định Tháng.
- Sự kiện/task hiện dạng block màu nhỏ trong ô ngày, màu theo loại/trạng thái (dùng đúng semantic color hoặc màu theo category nếu có nhiều loại sự kiện — tối đa 4-5 màu category để không rối). Ô ngày có nhiều sự kiện quá số hiện được → hiện "+N khác", click mở popover liệt kê đủ.
- Click 1 sự kiện → popover hoặc modal chi tiết (tên, thời gian, người liên quan, mô tả, trạng thái) — không điều hướng sang trang khác trừ khi cần xem đầy đủ dữ liệu liên kết (vd link sang chi tiết đơn hàng).
- Nút "+ Tạo mới" ở góc trên hoặc click trực tiếp vào 1 ô ngày trống để mở form tạo sự kiện (chọn kiểu container theo `reference/form-containers.md`).
- Ngày hôm nay có viền/nền nhấn nhẹ (Primary-50) để định vị nhanh khi demo.

## Kanban board

- Cột = giá trị của 1 trường trạng thái (vd Cần làm/Đang làm/Chờ duyệt/Hoàn thành) — số cột và tên cột suy ra từ chính trường trạng thái của thực thể đang quản lý, không bịa cột chung chung.
- Mỗi card hiện: tiêu đề, 2-3 field quan trọng nhất (không nhồi hết field), avatar người phụ trách (ảnh/chữ cái đầu trong hình tròn), badge ưu tiên nếu có (cao/trung bình/thấp — màu error/warning/neutral), badge hạn nếu có.
- Header mỗi cột hiện tên cột + số lượng card trong cột (badge tròn nhỏ) + nút "+" thêm nhanh 1 card vào đúng cột đó.
- Chuyển trạng thái: dùng dropdown/nút "Chuyển sang [cột kế]" trong card (xem ghi chú drag-and-drop ở đầu file) thay vì kéo-thả viết tay, trừ khi được yêu cầu rõ.
- Click card → form chi tiết đầy đủ (chọn kiểu container theo `reference/form-containers.md`, thường là Pop-up Modal hoặc Slide-over tuỳ số trường).

## Timeline/Gantt (lập lịch dự án có thời lượng)

- Trục ngang là thời gian (ngày/tuần, chia cột đều), trục dọc là danh sách task/resource (tên bên trái, cố định khi cuộn ngang).
- Mỗi task là 1 thanh ngang (bar) đặt đúng vị trí bắt đầu/kết thúc theo mock data, màu theo trạng thái/loại, có thể hiện % hoàn thành bằng cách tô đậm 1 phần thanh.
- Quan hệ phụ thuộc giữa task (đường nối mũi tên) — CHỈ làm nếu đây là workflow chính và dữ liệu mock có trường phụ thuộc rõ ràng; bỏ qua nếu không, không tự bịa quan hệ phụ thuộc không có trong ngữ cảnh.
- Zoom/scale: cố định 1 mức hiển thị hợp lý (vd theo tuần) cho bản demo tĩnh, không cần logic zoom thật.
- Click 1 thanh task → mở chi tiết task (chọn kiểu container theo `reference/form-containers.md`).

## Bản đồ/theo dõi vị trí (logistics, giao hàng, field service, bất động sản)

**Không tích hợp map provider thật** (Google Maps/Mapbox cần API key, sẽ vỡ khi demo offline hoặc không có key) — dựng bản đồ CÁCH ĐIỆU: 1 nền SVG/CSS pattern gợi hình bản đồ (lưới đường phố đơn giản hoặc nền màu neutral có texture nhẹ), pin marker là các phần tử `position: absolute` đặt theo toạ độ % trong mock data (không phải toạ độ GPS thật), route là 1 đường SVG path nối các điểm nếu cần minh hoạ tuyến đường.
- Marker màu theo trạng thái (đang giao/đã giao/trễ hẹn... dùng semantic color), click marker → popover thông tin ngắn (tên, trạng thái, thời gian cập nhật gần nhất).
- Panel danh sách bên cạnh bản đồ (split-view) đồng bộ với marker — click 1 dòng trong danh sách highlight marker tương ứng trên bản đồ và ngược lại, nếu đây là workflow chính.
- Ghi chú trong `ui-kit-brief.md` rằng bản đồ là minh hoạ cách điệu, không phải dữ liệu địa lý thật — tránh khách hàng hiểu nhầm đây đã tích hợp bản đồ thật.

## Activity feed / Inbox (dòng sự kiện hệ thống, thông báo)

- Danh sách dọc, mỗi mục có icon theo loại sự kiện (dùng đúng bộ icon đã định nghĩa), mô tả ngắn hành động, timestamp tương đối (vd "2 giờ trước", tính từ mock data).
- Phân biệt đã đọc/chưa đọc: mục chưa đọc có chấm nhỏ màu Primary + chữ đậm hơn; đã đọc chữ thường, nền nhạt hơn.
- Chip lọc theo loại sự kiện phía trên danh sách (tương tự toolbar CRUD nhưng đơn giản hơn, không cần sort/group).
- Nút "Đánh dấu đã đọc tất cả" — nếu workflow chính, cập nhật trạng thái đã đọc trong `localStorage` cho toàn bộ danh sách hiện tại.

## Wizard nhiều bước (onboarding, luồng tạo hồ sơ phức tạp)

Khác các kiểu container trong `reference/form-containers.md` (dù chọn kiểu nào, đó vẫn là 1 bước nhập liệu) ở chỗ Wizard là 1 luồng TUẦN TỰ nhiều bước, thường là trang riêng không phải overlay:
- Step indicator ngang trên cùng: các vòng tròn đánh số nối bằng đường kẻ, bước hiện tại highlight màu Primary, bước đã qua có dấu check, bước chưa tới màu neutral.
- Mỗi bước là 1 panel riêng (ẩn/hiện bằng JS, không load lại trang, giữ dữ liệu đã nhập khi lùi/tiến bước).
- Nút "Quay lại"/"Tiếp tục" ở cuối mỗi bước, nút cuối cùng đổi thành "Hoàn tất" — bước cuối là 1 trang tóm tắt toàn bộ dữ liệu đã nhập trước khi submit thật.
- Validate theo từng bước (không cho "Tiếp tục" nếu bước hiện tại có lỗi) nếu đây là workflow chính, theo đúng cơ chế validate on-blur trong `interactivity-guide.md`.

## Quản lý file/tài liệu

- Toggle 2 chế độ xem: dạng lưới (thumbnail/icon theo loại file + tên bên dưới) và dạng danh sách (bảng CRUD chuẩn với cột Loại/Kích thước/Ngày sửa) — nút toggle ở góc toolbar.
- Điều hướng thư mục: breadcrumb thư mục (Thư mục gốc / Tên thư mục con...) hoặc cây thư mục thu gọn được ở cột trái nếu cấu trúc phân cấp sâu.
- Icon theo loại file (PDF/Word/Excel/ảnh...) nếu không có thumbnail thật — dùng bộ icon nhất quán đã định nghĩa, không dùng icon mặc định hệ điều hành.
- Vùng upload: khung viền đứt nét "Kéo thả file vào đây hoặc click để chọn" — chỉ cần UI, không cần xử lý upload thật; nếu là workflow chính, click/thả giả lập thêm 1 dòng file mới vào danh sách (mock, không đọc file thật) kèm loading state ngắn theo `interactivity-guide.md`.
- Click 1 file → panel/modal xem trước (thumbnail lớn hơn hoặc icon lớn + đầy đủ metadata) kèm action Tải xuống/Đổi tên/Xoá/Di chuyển.
