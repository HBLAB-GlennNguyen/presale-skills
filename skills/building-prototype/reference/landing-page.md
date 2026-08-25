# Landing page

Áp dụng khi sitemap có 1 màn hình marketing/giới thiệu thực sự (nhiều section, mục tiêu chuyển đổi khách xem thành lead/đăng ký) — không phải mọi "Trang chủ public" đơn giản đều cần mức này. Nếu màn hình entry-flow chỉ cần giới thiệu ngắn + lối vào module (theo mục "Đăng nhập / Trang chủ public" trong `screen-generation-guide.md`), giữ nguyên cách đó — chỉ dùng file này khi archetype Public/Thương mại thực sự cần 1 trang bán hàng/giới thiệu sản phẩm đầy đủ (thường là màn hình "Trang chủ"/"Giới thiệu" trong sitemap của archetype Public, hoặc khi `requirements-summary.md` nêu rõ cần trang marketing riêng).

Đây là loại màn hình có visual bar cao nhất trong prototype — nếu môi trường đã cài skill `frontend-design`, đây là nơi đáng gọi nhất (xem `SKILL.md` bước 3): hero là 1 thesis, không phải template "big number + gradient".

## Cấu trúc section (thứ tự chuẩn, có thể bớt section không phù hợp, không thêm section không phục vụ mục tiêu chuyển đổi)

1. **Header sticky:** logo bên trái, anchor link tới các section chính ở giữa (Tính năng/Bảng giá/Liên hệ...), 1 nút CTA phụ (vd "Đăng nhập") + 1 nút CTA chính (`btn-primary`, vd "Dùng thử miễn phí") bên phải. Đổi nền từ trong suốt sang surface đặc khi cuộn qua khỏi hero (dùng scroll listener đơn giản).
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

## Animation khi cuộn (theo `reference/craft-and-qa.md` — motivated-motion, không phải hiệu ứng cho vui)

- Mỗi section (trừ hero, đã hiện sẵn khi tải trang) fade-in + translateY(16px→0) nhẹ khi cuộn vào viewport, dùng `IntersectionObserver` (không dùng thư viện ngoài) — mục đích: dẫn mắt người xem theo đúng thứ tự đọc, không phải trang trí.
- Thời lượng/easing theo bảng trong `craft-and-qa.md` (200-300ms, `ease-out`), tôn trọng `prefers-reduced-motion`.
- KHÔNG dùng parallax phức tạp hoặc hiệu ứng chạy liên tục (marquee logo cuộn vô hạn...) trừ khi thực sự phù hợp ngữ cảnh — dễ trông rối và không phục vụ nội dung.

## Responsive

Header chuyển sang hamburger dưới breakpoint tablet (xem `reference/responsive-and-pwa.md`), cột feature/pricing xếp dọc 1 cột trên mobile, hero visual xuống dưới text thay vì cạnh nhau.

## Interactivity

Landing page mặc định là màn hình phụ (static UI + điều hướng đúng theo `interactivity-guide.md`) trừ khi form đăng ký/liên hệ trên đó là 1 phần của workflow chính đã xác nhận — khi đó áp dụng validate/loading-state như mọi form thuộc workflow chính.
