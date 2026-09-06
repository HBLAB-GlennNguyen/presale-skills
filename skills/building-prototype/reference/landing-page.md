# Landing page

Áp dụng trong 2 trường hợp:
1. **Cả dự án là Landing page/Website marketing thuần** (Loại dự án đã chọn ở `ui-kit-qna.md`) — MỌI trang trong sitemap dùng file này (Trang chủ dùng đầy đủ cấu trúc bên dưới, các trang phụ dùng mục "Các loại trang phụ" ở cuối file), thay thế hoàn toàn `screen-generation-guide.md` (sidebar/CRUD/dashboard không áp dụng).
2. **1 màn hình marketing/giới thiệu thực sự nhúng trong 1 hệ thống quản lý lớn hơn** (nhiều section, mục tiêu chuyển đổi khách xem thành lead/đăng ký) — không phải mọi "Trang chủ public" đơn giản đều cần mức này. Nếu màn hình entry-flow chỉ cần giới thiệu ngắn + lối vào module (theo mục "Đăng nhập / Trang chủ public" trong `screen-generation-guide.md`), giữ nguyên cách đó — chỉ dùng file này khi archetype Public/Thương mại thực sự cần 1 trang bán hàng/giới thiệu sản phẩm đầy đủ.

Đây là loại màn hình có visual bar cao nhất trong prototype — nếu môi trường đã cài skill `frontend-design`, đây là nơi đáng gọi nhất (xem `SKILL.md` bước 3): hero là 1 thesis, không phải template "big number + gradient".

Toàn bộ copy hiển thị (Hero, Value props, About, Dịch vụ, Blog...) và hình ảnh minh họa dùng trong các section/trang dưới đây phải theo `reference/content-and-seo.md` (cách viết nội dung chuẩn SEO/AI-SEO, checklist thẻ `<head>`, và quy trình tìm/xác minh ảnh thật không watermark) — áp dụng cùng lúc với hướng dẫn bố cục ở file này, không phải bước tách biệt làm sau.

## Mục tiêu chính quyết định độ dày nội dung (chỉ áp dụng khi Loại dự án = Landing page thuần)

Dùng câu trả lời L1 trong `ui-kit-brief.md` để chọn bộ section — không áp dụng máy móc toàn bộ 9 section bên dưới cho mọi dự án:
- **Thu lead/đăng ký dùng thử · Bán hàng trực tiếp:** ưu tiên ít section, CTA dồn nén, đi thẳng vào giá trị — Header, Hero, Value props (3-4 khối), Social proof, Bảng giá (nếu có), CTA cuối, Footer là đủ; bỏ "Cách hoạt động"/FAQ nếu không thực sự cần thiết để chốt chuyển đổi.
- **Giới thiệu dịch vụ đầy đủ · Xây thương hiệu qua nội dung:** ưu tiên đầy đủ section hơn, có thể thêm các trang phụ (About, Blog, case study riêng) ngoài Trang chủ — xem "Các loại trang phụ" bên dưới. Trang chủ vẫn giữ cấu trúc chuẩn nhưng mỗi section có thể dài hơn, dẫn link sang trang phụ tương ứng để xem chi tiết thay vì nhồi hết vào 1 trang.

## Bố cục & khung nội dung Homepage — đề xuất rồi xác nhận, không tự chốt

Trước khi generate Hero, dùng L1 + L2 (trang tham khảo) trong `ui-kit-brief.md` để đề xuất 1 thứ tự section cụ thể cho Trang chủ (chọn/bớt/sắp xếp lại từ danh sách "Cấu trúc section" bên dưới). Sau khi thứ tự section được chốt, chạy tiếp quy trình brainstorm khung nội dung đầy đủ trong `reference/content-brainstorming.md` — chốt cả GÓC THÔNG ĐIỆP của từng section (không chỉ thứ tự), trình bày cho người dùng xác nhận/thêm/bớt/đổi trong 1 lần (giống cách `SKILL.md` đang làm với workflow/menu-grouping) — không tự chốt 1 mình rồi generate luôn. Ghi cả thứ tự section và khung nội dung đã xác nhận vào `ui-kit-brief.md` để dùng nhất quán nếu phải resume.

## Cấu trúc section (thứ tự chuẩn, có thể bớt section không phù hợp, không thêm section không phục vụ mục tiêu chuyển đổi)

1. **Header sticky:** logo bên trái, nav ở giữa theo cấu trúc đã xác nhận ở bước "Identify the menu grouping / site navigation" trong `SKILL.md` — anchor link (cuộn trong Trang chủ) cho các section chỉ tồn tại trên Trang chủ, page link thường (điều hướng sang trang khác) cho các trang độc lập trong sitemap (About/Bảng giá/Blog/Liên hệ...); nếu dự án có cả 2 loại, trộn chung 1 nav là bình thường. Header này PHẢI giống hệt nhau trên MỌI trang (không dựng lại khác nhau mỗi trang) — anchor link trỏ về `/#section-id` khi đứng ở trang khác Trang chủ. 1 nút CTA phụ (nếu Loại dự án là hệ thống có đăng nhập thì đây là "Đăng nhập"; nếu Landing page thuần thì đây có thể là 1 hành động phụ khác như "Xem bảng giá"/"Liên hệ", tùy L1) + 1 nút CTA chính (`btn-primary`, vd "Dùng thử miễn phí") bên phải. Đổi nền từ trong suốt sang surface đặc khi cuộn qua khỏi hero (dùng scroll listener đơn giản) — chỉ áp dụng hiệu ứng trong suốt này ở Trang chủ (nơi có hero full-bleed); các trang phụ có thể để header solid ngay từ đầu vì thường không có hero full-bleed.
2. **Hero:** headline 1 câu nêu đúng giá trị cốt lõi (không phải slogan chung chung "Giải pháp toàn diện cho doanh nghiệp") + 1 câu subheadline giải thích cách làm được điều đó, 1 CTA chính nổi bật + 1 CTA phụ dạng ghost/outline (vd "Xem demo"), 1 visual bên cạnh hoặc bên dưới (mockup sản phẩm dạng khung trình duyệt/điện thoại chứa ảnh chụp 1 màn hình THẬT đã generate trong prototype này — không dùng ảnh stock — hoặc 1 minh hoạ trừu tượng gắn với "Điểm nhấn riêng" đã chọn trong `ui-kit-brief.md`).
3. **Value props / Tính năng:** 3-4 khối tính năng chính — theo "Danh sách cấm" trong `reference/craft-and-qa.md`, KHÔNG lặp đúng 1 khuôn "icon tròn + heading + 1 dòng mô tả" cho cả 3-4 khối; đổi bố cục ít nhất 1 khối (vd 1 khối có ảnh minh hoạ lớn hơn, 1 khối dạng before/after, 1 khối có số liệu cụ thể thay vì icon).
4. **Cách hoạt động (How it works) — tùy chọn, chỉ dùng nếu quy trình sản phẩm thực sự có thứ tự các bước đáng nêu:** 3 bước đánh số — chỉ dùng số thứ tự khi các bước THẬT SỰ tuần tự (theo cảnh báo trong `craft-and-qa.md`), không dùng cho 3 tính năng độc lập không có thứ tự.
5. **Social proof — chỉ khi có nội dung thật hoặc mock hợp lý theo ngữ cảnh khách hàng:** logo khách hàng/đối tác (dùng tên công ty mock gắn với ngành trong `requirements-summary.md`, không dùng logo thật của bên thứ 3) hoặc 1-2 câu trích dẫn có tên người + chức danh + công ty mock cụ thể — KHÔNG viết câu kiểu "Được tin dùng bởi hàng trăm doanh nghiệp" không có gì cụ thể đi kèm (xem `craft-and-qa.md`).
6. **Bảng giá — chỉ nếu sản phẩm có mô hình gói/giá theo `requirements-summary.md`:** 2-3 cột gói, 1 gói được highlight (badge "Phổ biến nhất" + viền/nền Accent nổi bật hơn), mỗi gói liệt kê 4-6 tính năng có/không (icon check/x), 1 CTA riêng mỗi gói.
7. **FAQ — tùy chọn:** dạng accordion (click mở/đóng câu trả lời, chỉ 1 hoặc nhiều câu mở cùng lúc đều được), 4-6 câu hỏi thật liên quan tới sản phẩm/ngành, không phải câu hỏi chung chung mọi landing page nào cũng có.
8. **CTA cuối:** nhắc lại đúng CTA chính ở hero, nền màu đặc Primary-dark tương phản mạnh với section ngay trên để đánh dấu điểm kết bài.
9. **Footer:** logo + mô tả ngắn, cột link (Sản phẩm/Công ty/Pháp lý theo ngữ cảnh), social icon nếu phù hợp, copyright.

## Nhịp điệu thị giác giữa các section

Không để 2 section liên tiếp cùng nền trắng — xen kẽ nền trắng/surface với nền tint nhẹ (Primary-50 hoặc gray-50) hoặc nền đặc (chỉ hero và CTA cuối dùng Primary-dark) để mắt phân biệt được ranh giới section khi cuộn, không phải dựa vào khoảng trắng đơn thuần.

## Animation/tương tác (theo `reference/craft-and-qa.md` — motivated-motion, không phải hiệu ứng cho vui)

Mức độ áp dụng theo câu trả lời L3 trong `ui-kit-brief.md` (khi Loại dự án = Landing page thuần; nếu là 1 màn hình nhúng trong hệ thống quản lý, mặc định dùng mức "Vừa phải"). Mỗi mức bao gồm toàn bộ các mục của mức thấp hơn, cộng thêm phần liệt kê riêng.

**Tối giản:**
- Mỗi section (trừ hero, đã hiện sẵn khi tải trang) fade-in + translateY(16px→0) nhẹ khi cuộn vào viewport, dùng `IntersectionObserver` (không dùng thư viện ngoài) — mục đích: dẫn mắt người xem theo đúng thứ tự đọc, không phải trang trí.
- Thời lượng/easing theo bảng trong `craft-and-qa.md` (200-300ms, `ease-out`), tôn trọng `prefers-reduced-motion`.

**Vừa phải (mặc định nếu không nêu rõ):**
- Hover state rõ ràng trên mọi phần tử bấm được (nút đổi màu/nâng shadow nhẹ, card feature nâng lên `translateY(-4px)` + shadow đậm hơn khi hover, link đổi màu/gạch chân mượt bằng `transition`).
- Icon/hình minh hoạ trong mỗi khối value-prop có 1 micro-interaction nhỏ khi hover (xoay nhẹ, đổi màu nền tròn phía sau icon) — không lạm dụng, chỉ 1 hiệu ứng nhỏ mỗi phần tử.
- Nút CTA chính có hiệu ứng nhấn (scale nhẹ khi `:active`) để cảm giác phản hồi tức thời.

**Sống động:**
- Số liệu nổi bật (vd trong social proof/stat: "500+ khách hàng", "99.9% uptime") đếm chạy từ 0 lên giá trị thật khi vào viewport (dùng `IntersectionObserver` + `requestAnimationFrame`, không dùng thư viện ngoài), chạy đúng 1 lần.
- Section "Cách hoạt động" hoặc feature có thể dùng tab/accordion tương tác (click đổi nội dung/ảnh minh hoạ tương ứng) thay vì liệt kê tĩnh, nếu nội dung phù hợp có nhiều lựa chọn để so sánh.
- Hero visual có thể có 1 hiệu ứng chuyển động nhẹ liên tục (float lên xuống chậm của 1 hình khối trang trí, hoặc parallax NHẸ 1 lớp khi cuộn — tốc độ lớp nền chậm hơn foreground) — vẫn phải tôn trọng `prefers-reduced-motion` (tắt hẳn khi user bật) và không được che/làm khó đọc nội dung.
- Social proof có thể dùng carousel logo/testimonial tự trượt chậm (dừng khi hover) thay vì lưới tĩnh, nếu số lượng đủ nhiều (5+) để carousel có ý nghĩa.

**Ở mọi mức — KHÔNG dùng:** parallax phức tạp nhiều lớp, hiệu ứng chạy liên tục gây rối mắt (marquee logo cuộn vô hạn tốc độ nhanh, background động chiếm quá nhiều chú ý), hoặc bất kỳ animation nào không phục vụ nội dung/dẫn mắt đọc — xem danh sách cấm trong `craft-and-qa.md`.

## Responsive

Header chuyển sang hamburger dưới breakpoint tablet (xem `reference/responsive-and-pwa.md`), cột feature/pricing xếp dọc 1 cột trên mobile, hero visual xuống dưới text thay vì cạnh nhau.

## Các loại trang phụ (khi Loại dự án = Landing page thuần và sitemap có nhiều trang ngoài Trang chủ)

Mỗi trang dưới đây dùng chung header/footer đã xác định ở "Cấu trúc section" (mục 1 và 9) — không dựng lại chrome riêng. Nội dung chính (phần giữa header và footer) theo hướng dẫn riêng từng loại:

- **About/Giới thiệu:** hero ngắn (1 câu định vị công ty/sản phẩm, không cần CTA mạnh như Trang chủ), block câu chuyện/sứ mệnh, block đội ngũ (3-6 thẻ avatar + tên + chức danh mock phù hợp ngành), có thể thêm timeline mốc phát triển nếu ngữ cảnh phù hợp (công ty đã hoạt động nhiều năm) — không bịa timeline nếu `requirements-summary.md` không gợi ý gì về lịch sử công ty. Kết thúc bằng 1 CTA nhẹ (không cần nền đặc Primary-dark như CTA cuối Trang chủ).
- **Bảng giá (trang riêng, khác với section Bảng giá trong Trang chủ):** dùng lại đúng bố cục 2-3 cột gói ở mục 6 nhưng làm nội dung chính của cả trang — mở rộng thêm 1 bảng so sánh chi tiết đầy đủ tính năng theo từng cột gói (không chỉ 4-6 dòng rút gọn như trên Trang chủ), và 1 khối FAQ riêng về giá/thanh toán/nâng cấp-hạ cấp gói.
- **Blog — trang danh sách:** lưới card bài viết (ảnh đại diện + tiêu đề + đoạn trích + tên tác giả mock + ngày đăng), 6-9 bài mock liên quan tới ngành nghề khách hàng trong `requirements-summary.md` (không dùng tiêu đề chung chung kiểu "Bài viết 1"), có filter/tag theo chủ đề nếu hợp lý, phân trang cuối trang (UI tĩnh). Toàn bộ 6-9 bài này là entity "Bài viết" theo `reference/data-layer.md` — viết 1 lần vào `assets/data/bai-viet.js`, trang danh sách và trang chi tiết đều đọc từ đúng file đó (không mỗi trang tự bịa 1 bộ bài viết riêng).
- **Blog — trang chi tiết bài viết:** tiêu đề lớn + meta (tác giả/ngày/thời gian đọc), nội dung bài viết dạng rich-text mock (heading phụ, đoạn văn, có thể 1 ảnh minh hoạ, 1 blockquote) đủ dài để trông như bài thật (không phải 2 dòng placeholder), khối "Bài viết liên quan" (3 card) cuối bài — lấy đúng từ `DATA_BAI_VIET`, không bịa bài mới, CTA nhẹ quay lại danh sách blog hoặc CTA chuyển đổi chính của trang.
- **Liên hệ (trang riêng, khác với section CTA cuối):** 2 cột — cột form (Họ tên/Email/Điện thoại/Nội dung, đây thường là 1 trong các conversion action chính nên áp dụng interactivity đầy đủ theo `interactivity-guide.md`) và cột thông tin liên hệ (địa chỉ/email/điện thoại/giờ làm việc mock hợp lý theo ngành, có thể thêm khung bản đồ placeholder tĩnh — không cần tích hợp bản đồ thật).
- **Trang cảm ơn (Thank-you) — đích đến sau khi submit 1 conversion form:** không nằm sẵn trong sitemap nhưng vẫn phải tạo nếu có bất kỳ conversion form nào được xác nhận full-interactivity ở bước "Identify main workflows / conversion actions" trong `SKILL.md` — icon/minh hoạ xác nhận thành công (checkmark tròn màu Success), 1 câu cảm ơn cụ thể nhắc lại đúng hành động vừa thực hiện (vd "Cảm ơn bạn đã đăng ký dùng thử — đội ngũ sẽ liên hệ trong 24h" chứ không chung chung "Cảm ơn bạn"), 1 CTA quay về Trang chủ hoặc dẫn tới bước tiếp theo hợp lý (vd link tài liệu/case study).

## Interactivity

Trang phụ tĩnh (About, Bảng giá, Blog...) mặc định là màn hình phụ (static UI + điều hướng đúng theo `interactivity-guide.md`) trừ khi có form trên trang đó là 1 trong các conversion action đã xác nhận ở `SKILL.md` (vd form Liên hệ) — khi đó áp dụng validate/loading-state như mọi form thuộc workflow/conversion action chính, và submit thành công điều hướng tới Trang cảm ơn (xem "Các loại trang phụ" ở trên) thay vì quay về 1 màn hình quản lý.
