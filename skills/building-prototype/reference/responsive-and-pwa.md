# Responsive, Tablet & PWA

Áp dụng cho TOÀN BỘ prototype khi câu 8 trong `ui-kit-qna.md` khác "Desktop/nội bộ" — đọc file này trước khi generate `global.css`/`global.js`, không phải tùy chọn thêm cho vài màn hình riêng lẻ. Nếu câu 8 = Desktop/nội bộ, bỏ qua toàn bộ file này, hành vi hiện tại của `screen-generation-guide.md` không đổi.

## Breakpoint & chiến lược layout

- Mobile-first: viết CSS base cho mobile trước, dùng `min-width` để thêm phức tạp dần — không viết desktop trước rồi thu nhỏ bằng `max-width`.
- 3 breakpoint theo nội dung, không chạy theo kích thước thiết bị cụ thể: ~640px (mobile→tablet), ~768px, ~1024px (tablet→desktop) — nếu 1 màn hình cụ thể vỡ layout ở kích thước khác, thêm breakpoint tại đúng điểm đó thay vì ép vào 3 mốc trên.
- Dùng `clamp()` cho các giá trị cần mượt giữa 2 mốc (font-size hero, padding lớn) thay vì nhảy bậc cứng ở mỗi breakpoint.
- **Dùng input-method query, không chỉ dựa kích thước màn hình** — tablet có thể gắn bàn phím/chuột rời (iPad + Magic Keyboard), laptop có thể có cảm ứng:
```css
@media (hover: none) and (pointer: coarse) { /* đang chạm, tối ưu touch target */ }
@media (hover: hover) and (pointer: fine)  { /* có chuột/trackpad, có thể dùng hover */ }
```

## Điều hướng theo thiết bị

Cấu trúc nhóm menu/module vẫn lấy từ bảng "Thiết kế nhóm menu" như `screen-generation-guide.md` đã mô tả — chỉ đổi VỎ hiển thị theo breakpoint, không đổi dữ liệu nav:
- **Desktop (≥1024px):** giữ nguyên sidebar dọc/nav ngang theo archetype (hoặc `data-grid.md` nếu kiểu điều hướng = ngang).
- **Tablet (768-1023px):** nếu đang dùng sidebar dọc, giữ nhưng mặc định ở trạng thái thu gọn (icon-rail) để nhường chỗ content; nếu đang dùng nav ngang (Public hoặc data-grid), giữ nguyên nav ngang.
- **Mobile (<768px):** MỌI kiểu điều hướng (sidebar dọc lẫn nav ngang) chuyển thành hamburger + drawer trượt từ trái, che overlay mờ phần content khi mở — tái dùng đúng cấu trúc accordion nhóm menu đã có bên trong drawer, không thiết kế lại. Cân nhắc thêm bottom tab bar (tối đa 5 icon) thay hamburger nếu số nhóm menu ≤5 và các nhóm đó là điểm vào chính được dùng thường xuyên.

## Không được phụ thuộc `:hover` làm cách DUY NHẤT để lộ thông tin/action

Đây là lỗi thật trong `screen-generation-guide.md` hiện có nếu không patch — rà theo đúng các mục sau khi platform mục tiêu khác Desktop/nội bộ:
- **Tooltip tên mục nav khi sidebar thu gọn:** giữ hiện khi hover (desktop có chuột), nhưng khi platform ≠ Desktop/nội bộ, sidebar không được mặc định ở trạng thái "chỉ icon" trên mobile (đã chuyển sang drawer có nhãn đầy đủ ở trên) nên vấn đề tự triệt tiêu ở mobile; ở tablet nếu vẫn giữ icon-rail, đổi tooltip-on-hover thành tooltip-on-tap-and-hold hoặc bỏ hẳn chế độ chỉ-icon cho tablet (ưu tiên phương án sau, đơn giản hơn).
- **Flyout khi hover vào nhóm menu đã thu gọn:** trên touch, đổi "chỉ cần hover là đủ" thành tap-to-open (tap lần nữa hoặc tap ra ngoài để đóng) — không được là cách DUY NHẤT không có fallback tap.
- **Action Xem/Sửa/Xoá trên dòng bảng:** nếu `screen-generation-guide.md`/`data-grid.md` đang thiết kế các action này chỉ hiện khi hover dòng, khi platform ≠ Desktop/nội bộ phải LUÔN hiển thị (hoặc gộp vào 1 icon "..." luôn hiển thị mở menu) — không có gì để hover trên touch.

## Touch target & form

- Tối thiểu 44×44px (theo chuẩn Apple HIG/Material) cho mọi phần tử chạm được, khoảng cách tối thiểu 8px giữa 2 target liền kề.
- Input: `type`/`inputmode` đúng để bàn phím ảo hiện đúng loại; font-size input tối thiểu 16px (dưới mức này Safari trên iOS tự zoom vào ô nhập, vỡ layout).
- Modal/form dài trên mobile: chuyển từ dialog căn giữa sang full-screen sheet (chiếm toàn màn hình, có nút đóng/back rõ ràng ở góc trên) — trên tablet vẫn có thể giữ dialog căn giữa nếu đủ rộng.
- Nút Lưu/Gửi trong form dài phải đảm bảo không bị bàn phím ảo che khuất (test bằng cách cuộn tới cuối form khi input đang focus).

## Orientation & layout tablet (2 cột, không phải 1 như mobile cũng không phải 3-4 như desktop)

- Hỗ trợ cả portrait và landscape — không giả định 1 chiều.
- Landscape đủ rộng (đặc biệt các màn hình quản lý/CRM): dùng master-detail 2 cột (danh sách bên trái, chi tiết bên phải, chọn 1 dòng để xem/sửa mà không rời trang).
- Portrait hẹp hơn: gộp về 1 cột, tap dòng "đẩy" sang view chi tiết riêng có nút quay lại.
- Toolbar filter/sort/group (xem `screen-generation-guide.md`/`data-grid.md`): trên portrait chật chỗ, chuyển từ hàng chip ngang sang slide-in filter panel thay vì cố nhồi 1 dòng.

## Bảng dữ liệu → card trên mobile

Bảng nhiều cột trong "Màn hình quản lý (danh sách/CRUD)" không cuộn ngang trên mobile — chuyển mỗi dòng thành 1 card dọc: cột chính (tên/mã) làm tiêu đề card, các cột còn lại thành cặp nhãn-giá trị xếp dọc bên dưới, action Xem/Sửa/Xoá đặt ở footer card (luôn hiển thị, không hover).

## Ẩn mọi thứ chỉ có ý nghĩa với chuột/bàn phím

Gợi ý phím tắt hiển thị trên UI (vd "Ctrl+S"), menu chuột phải — nếu tồn tại trong thiết kế desktop, phải ẩn trên touch và có nút/icon thay thế luôn hiển thị được bằng tap cho cùng chức năng đó.

## Safe-area (notch) & viewport

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```
```css
body { padding-top: env(safe-area-inset-top); padding-bottom: env(safe-area-inset-bottom); }
.app-header { padding-top: max(12px, env(safe-area-inset-top)); }
```

## PWA (chỉ khi câu 8 = Mobile-first/PWA)

Generate `./output/prototype/manifest.json`, giá trị màu lấy từ `ui-kit-brief.md`:
```json
{
  "name": "<Tên sản phẩm đầy đủ>",
  "short_name": "<Tên sản phẩm ngắn>",
  "start_url": "./index.html",
  "display": "standalone",
  "background_color": "<Primary-50 hoặc trắng>",
  "theme_color": "<Primary-dark>",
  "icons": [{ "src": "assets/img/icon-192.png", "sizes": "192x192", "type": "image/png" }]
}
```
Link trong `<head>` mọi màn hình: `<link rel="manifest" href="<đường dẫn tương đối tới manifest.json>">` cùng thẻ `apple-touch-icon` và `apple-mobile-web-app-capable`/`apple-mobile-web-app-status-bar-style` cho iOS homescreen.

**Standalone mode không còn nút back của trình duyệt luôn hiện** — mọi màn hình con phải có nút quay lại/breadcrumb hoạt động thật trong chrome của app (đã có breadcrumb sẵn theo `screen-generation-guide.md`, chỉ cần đảm bảo nó dẫn đúng chỗ), không dựa vào back của hệ thống lúc nào cũng có mặt.

**Không làm service worker/offline thật** — đây là demo tĩnh cho presale, không phải app sẽ ship. Chỉ đủ để "Add to Home Screen" hoạt động và app mở full-screen không thanh địa chỉ. Nếu khách hàng cụ thể yêu cầu demo tính năng offline như 1 điểm bán hàng, báo lại cho người dùng đây là phạm vi mở rộng ngoài quy trình chuẩn thay vì tự ý làm service worker phức tạp.
