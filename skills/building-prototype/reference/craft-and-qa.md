# Chất lượng thị giác nâng cao & QA cuối

Áp dụng cùng lúc với `ui-kit-qna.md` khi khoá `ui-kit-brief.md`/generate `global.css` (phần Bans/Browser-chrome/Motion), và ở bước 7-8 của `SKILL.md` (phần QA 2 track).

## Danh sách cấm — "dấu hiệu AI tạo ra" (tránh, không phải vì đẹp/xấu mà vì làm lộ prototype là generate hàng loạt)

Đây là các CATEGORY cần tránh, không phải giá trị cụ thể (hex/font cụ thể dễ lỗi thời khi model đổi) — tự nhận diện khi đang viết ra những thứ này:
- Copy giả khiêm tốn/marketing sáo rỗng kiểu "Được tin dùng bởi hàng trăm doanh nghiệp" không có tên thật đi kèm — nếu không có khách hàng/số liệu thật, đừng viết câu này.
- Chấm trạng thái (status dot) trang trí không gắn với dữ liệu thật — mọi chấm màu phải map với 1 trạng thái cụ thể trong mock data, không đặt cho vui.
- Footer version giả ("v1.4.2") hoặc timestamp/ngày giờ không phục vụ nội dung màn hình.
- Nhãn "eyebrow" đánh số (01/02/03, STEP 1/2/3) khi nội dung không thực sự là 1 chuỗi tuần tự có thứ tự quan trọng — chỉ dùng khi thứ tự có ý nghĩa thật (vd luồng duyệt 3 bước thật).
- Icon bằng emoji unicode (📊, ✅) thay cho SVG nhất quán — luôn dùng bộ icon outline đã định nghĩa trong `ui-kit-brief.md`.
- Chữ gradient trang trí không phục vụ đọc nội dung (khác với gradient nền sidebar/hero đã được yêu cầu ở "Nguyên tắc dùng màu" — đó là nền, không phải text).
- Card/section scaffold lặp lại y hệt "icon tròn + heading + 1 dòng mô tả" cho mọi khối nội dung khác nhau — nếu 3+ khối liên tiếp dùng đúng 1 khuôn này, đổi bố cục cho ít nhất 1 khối để tạo phân cấp.
- Ảnh minh họa (Landing page) không khớp nội dung, có watermark/logo hãng ảnh đè lên, hoặc là 1 URL ảnh tự đoán chưa được xác minh tồn tại — xem quy trình bắt buộc trong `reference/content-and-seo.md`.

## Browser-chrome theming (rẻ nhưng hiệu quả — dấu hiệu rẻ nhất phân biệt "được thiết kế" với "được lắp ráp vội")

Định nghĩa trong `global.css`, áp dụng toàn cục:
```css
::selection { background: var(--primary-100); color: var(--primary-dark); }
::-webkit-scrollbar { width: 10px; height: 10px; }
::-webkit-scrollbar-thumb { background: var(--gray-300); border-radius: 999px; }
::-webkit-scrollbar-thumb:hover { background: var(--gray-400); }
:focus-visible { outline: 2px solid var(--primary); outline-offset: 2px; }
```
Không dùng `outline: none` mà không có thay thế — mọi phần tử tương tác (nút, link, input, dòng bảng có thể chọn) phải có `:focus-visible` rõ ràng theo bảng màu, không phải viền xanh mặc định trình duyệt hoặc mất hẳn viền.

## Motion/animation (tối thiểu — hiện skill trước đây chưa có mục nào về animation)

- **Motivated-motion gate:** trước khi thêm bất kỳ transition/animation nào, phải nêu được 1 câu nó phục vụ mục đích gì (feedback xác nhận hành động / thể hiện phân cấp / báo hiệu chuyển trạng thái) — "trông đẹp/sinh động" không phải lý do hợp lệ. Nếu không nêu được, bỏ animation đó.
- **Thời lượng:** 100-150ms cho feedback tức thời (hover, click, toggle), 200-300ms cho chuyển đổi trạng thái trong màn hình (mở accordion, chuyển tab), 400-600ms cho các sequence lớn hơn (mở modal, entrance của Dashboard khi load) — không dùng thời lượng tùy tiện.
- **Easing:** `ease-out` cho phần tử xuất hiện/mở rộng, `ease-in` cho phần tử biến mất/thu gọn — KHÔNG dùng bounce/elastic easing mặc định (dấu hiệu AI-generated rõ rệt, không phù hợp phần mềm nội bộ/B2B).
- **Tôn trọng `prefers-reduced-motion`:** mọi animation khác flat opacity/color transition đơn giản phải wrap trong `@media (prefers-reduced-motion: no-preference)`; dưới điều kiện `reduce`, giữ transition tối thiểu (không tắt hoàn toàn phản hồi, chỉ bỏ chuyển động lớn).
- **Pattern động phù hợp phần mềm nội bộ/CRUD (không lấy pattern hướng marketing-site như scroll-parallax):** hover elevation nhẹ trên card (translateY -2px + shadow tăng cấp), skeleton loading khi tải dữ liệu bảng (thay vì spinner trống), toast slide-in từ góc màn hình, sticky header đổi shadow khi cuộn (báo hiệu đang cuộn qua nội dung), accordion/dropdown expand theo `max-height`/`grid-template-rows` với easing ở trên. Dòng này áp dụng cho Loại dự án = Hệ thống quản lý; khi Loại dự án = Landing page, dùng bộ pattern riêng theo mức L1/L2/L3 trong `reference/landing-page.md` (bao gồm cả scroll-reveal, micro-interaction hover và — ở mức "Sống động" — parallax nhẹ/carousel), không bị giới hạn bởi dòng này.

## QA cuối — 2 track tách biệt, không để track này neo/lây nhiễm track kia

Áp dụng ở bước 7 (critique 2 màn hình neo) và bước 8 (spot-check) trong `SKILL.md`. Làm ĐÚNG THỨ TỰ này: xong track thẩm mỹ rồi mới sang track đếm-được — nếu làm ngược, checklist đếm-được sẽ neo phán đoán thẩm mỹ vào các mục cụ thể của nó thay vì đánh giá tổng thể trước.

**Track 1 — Phán đoán thẩm mỹ, không neo theo checklist (bước 7):** nhìn tổng thể màn hình như 1 khách hàng lần đầu thấy demo — có trông như phần mềm thật không, hay vẫn có cảm giác "được tạo ra"? Điểm nhấn riêng (`ui-kit-qna.md`) có thực sự nổi bật hay bị pha loãng? Đây là phán đoán chủ quan có chủ đích, không dùng danh sách đếm ở dưới để tự thuyết phục bản thân là "ổn" khi cảm giác tổng thể vẫn sai.

**Track 2 — Đếm được cụ thể, cơ học (bước 8, áp dụng khi spot-check 3 màn hình):**
- Đếm số card/stat dùng đúng 1 kiểu không có dải màu/phân cấp riêng — phải bằng 0 (xem "Nguyên tắc dùng màu" trong `ui-kit-qna.md`).
- Đếm số nút hành động trên màn hình dùng cùng 1 class (`btn-primary` cho mọi nút) — nếu màn hình có ≥3 nút hành động mà chỉ dùng 1 kiểu, sai.
- Đếm số vị trí đang dùng `:hover` làm cách DUY NHẤT để lộ thông tin/action quan trọng (không có fallback) — phải bằng 0 nếu nền tảng mục tiêu khác Desktop/nội bộ (xem `reference/responsive-and-pwa.md`).
- Đếm số chỗ vi phạm danh sách cấm ở trên — phải bằng 0.
Mỗi mục không đạt = sửa ngay tại chỗ, không ghi chú "để sau".

**QA trực quan tùy chọn (best-effort, không bắt buộc):** nếu môi trường đang chạy skill này có sẵn cách render/chụp màn hình HTML (vd qua skill `run` hoặc công cụ trình duyệt khác), mở màn hình neo (Đăng nhập/Trang chủ + Dashboard cho Hệ thống quản lý; Trang chủ cho Landing page) ở khổ ~375px và ~1440px trước khi báo hoàn tất, kiểm tra layout không vỡ. Bỏ qua bước này nếu không có công cụ phù hợp — không dừng tiến trình để cài đặt công cụ mới chỉ cho việc này.
