# Nội dung & SEO/AI-SEO cho Landing page

Áp dụng khi viết copy hiển thị và chọn hình ảnh minh họa cho MỌI trang dùng `reference/landing-page.md` — cả khi cả dự án là Landing page thuần lẫn khi đó chỉ là 1 màn hình marketing nhúng trong hệ thống quản lý. Đây là prototype tĩnh chưa deploy domain thật, nên không gọi skill `seo-geo` (skill đó audit 1 site đã lên mạng) — các nguyên tắc dưới đây được BAKE thẳng vào cách generate HTML/copy.

## 1. Viết nội dung (copy)

**Nguyên tắc chung cho mọi loại trang:**
- Answer-first: câu đầu tiên của mỗi đoạn/section trả lời thẳng ý chính, không dẫn dắt vòng vo rồi mới vào vấn đề.
- Heading (H1-H3) mô tả ĐÚNG nội dung bên dưới, đủ cụ thể để đọc riêng heading vẫn hiểu section nói gì — không dùng heading mập mờ kiểu "Giải pháp của chúng tôi" cho mọi section.
- Cụ thể/có số liệu thay vì chung chung sáo rỗng (áp dụng đúng danh sách cấm marketing sáo rỗng đã có trong `reference/craft-and-qa.md`).
- Ngôn ngữ theo câu 7 trong `ui-kit-qna.md`, giọng điệu nhất quán xuyên suốt mọi trang (không đổi giọng trang trịnh trọng ở About rồi lại đùa cợt ở Blog).
- Không dùng Lorem ipsum hoặc nội dung placeholder rõ ràng giả — mọi copy phải đọc như bài viết/nội dung thật, gắn với ngành nghề khách hàng trong `requirements-summary.md`.

**Theo loại trang:**
- **Trang chủ (Hero/Value props):** xem chi tiết cấu trúc và ví dụ trong `reference/landing-page.md` mục "Cấu trúc section".
- **About/Giới thiệu:** kể câu chuyện công ty gắn với ngành cụ thể, không kể chung chung "công ty hàng đầu". Nêu 2-3 con số cụ thể (năm thành lập, số khách hàng/dự án, quy mô đội ngũ) — lấy từ `requirements-summary.md` nếu có, nếu không có thì tự đặt số hợp lý theo quy mô/ngữ cảnh dự án (không bịa số phi thực tế như "10.000+ khách hàng" cho 1 startup mới).
- **Dịch vụ/Sản phẩm:** mỗi dịch vụ 1 heading riêng (H2), đoạn mở đầu trả lời thẳng "dịch vụ này giải quyết vấn đề gì cho khách hàng" trong 1-2 câu, sau đó mới liệt kê lợi ích/tính năng cụ thể (bullet, không đoạn văn dài dòng), kết mỗi khối dịch vụ bằng 1 CTA riêng (không dồn hết vào 1 CTA cuối trang).
- **Blog:** tiêu đề chứa đúng chủ đề/từ khóa chính (không đặt tên mơ hồ kiểu "Cập nhật mới"), đoạn mở đầu (2-3 câu) trả lời thẳng câu hỏi mà tiêu đề ngụ ý trước khi mở rộng, chia nhỏ thân bài theo H2 theo từng ý con, kết bài có CTA quay lại trang chuyển đổi chính. Đủ dài để không bị coi là thin content — nội dung mock phải thực chất (nhiều đoạn, có ví dụ/số liệu cụ thể theo ngành), không phải 2-3 dòng cho có.

## 2. SEO kỹ thuật (bắt buộc trong `<head>` của mọi trang)

- `<title>` riêng từng trang, không trùng lặp giữa các trang, ~50-60 ký tự, chứa từ khóa chính của trang + tên sản phẩm (theo `ui-kit-qna.md` câu 2).
- `<meta name="description">` riêng từng trang, ~150-160 ký tự, viết như copy quảng cáo thật (không nhồi từ khóa lộ liễu) — không để trống, không copy y hệt giữa các trang.
- Đúng 1 thẻ `<h1>` mỗi trang, khớp đúng chủ đề/mục đích của trang đó.
- Open Graph + Twitter Card: `og:title`, `og:description`, `og:image` (dùng ảnh hero/ảnh đại diện bài viết thật của trang đó, không dùng chung 1 ảnh cho mọi trang), `og:type`, `og:url`, `twitter:card` (`summary_large_image`).
- Semantic HTML5: `<header>`, `<nav>`, `<main>`, `<article>` cho bài blog, `<section>` có heading rõ ràng, `<footer>` — không dùng toàn `<div>` lồng nhau.
- `alt` text mô tả cụ thể cho MỌI ảnh nội dung (không để trống, không dùng tên file làm alt) — ảnh thuần trang trí không mang thông tin thì mới dùng `alt=""`.
- Slug URL (tên thư mục màn hình) phản ánh đúng chủ đề cụ thể của từng bài/trang — vẫn giữ theo tên tiếng Việt trong sitemap như quy ước hiện có của skill, nhưng với Blog thì tên thư mục phải đặt theo đúng tiêu đề bài viết cụ thể (vd `bai-viet/toi-uu-chi-phi-van-hanh-kho`), không đặt tên chung chung "bai-viet-1"/"bai-viet-2".

## 3. AI-SEO / GEO — để nội dung dễ được AI answer engine (ChatGPT, Perplexity, Google AI Overviews) trích dẫn

- Thêm JSON-LD structured data phù hợp từng loại trang: `Organization` ở Trang chủ, `Article` ở trang chi tiết blog (kèm `headline`/`datePublished`/`author`), `FAQPage` cho section FAQ (mục 7 trong `reference/landing-page.md` — tận dụng đúng nội dung accordion đã có, không viết lại riêng).
- Đoạn mở đầu mỗi section/bài viết trả lời thẳng câu hỏi mà heading ngụ ý trong 1-2 câu đầu tiên, trước khi mở rộng chi tiết — đây là đoạn có khả năng cao nhất bị AI trích dẫn riêng lẻ, nên phải tự đứng độc lập được khi tách khỏi ngữ cảnh (tránh mở đầu bằng đại từ mơ hồ "Điều này..."/"Nó giúp...", nêu rõ chủ ngữ cụ thể).
- Ưu tiên câu khẳng định cụ thể có thực thể/số liệu rõ ràng thay vì tính từ mơ hồ ("giảm 30% thời gian xử lý" thay vì "xử lý nhanh hơn nhiều") — vừa đúng nguyên tắc chống marketing sáo rỗng ở `craft-and-qa.md`, vừa dễ được trích dẫn chính xác.

## 4. Tìm & chọn hình ảnh minh họa thật

Áp dụng cho ảnh minh họa bài blog, ảnh đội ngũ/văn phòng ở About, ảnh minh họa dịch vụ cụ thể — KHÔNG áp dụng cho hero visual dạng mockup sản phẩm (vẫn dùng ảnh chụp màn hình thật của prototype hoặc minh hoạ trừu tượng gắn "Điểm nhấn riêng" như `reference/landing-page.md` mục Hero đã mô tả).

**Quy trình bắt buộc — không được tự đoán URL ảnh:**
1. Dùng WebSearch tìm ảnh theo từ khóa nội dung cụ thể, giới hạn nguồn bằng `site:unsplash.com`, `site:pexels.com`, hoặc `site:pixabay.com` (3 nền tảng có giấy phép Unsplash License/Pexels License/Pixabay License — miễn phí, không cần ghi nguồn, được dùng thương mại, không watermark).
2. Dùng WebFetch mở đúng trang ảnh cụ thể tìm được để lấy URL file ảnh trực tiếp thật (domain CDN dạng `images.unsplash.com/...`, `images.pexels.com/photos/...`, `cdn.pixabay.com/photo/...`) — không dùng URL trang kết quả tìm kiếm, phải là URL file ảnh đã xác minh tồn tại qua WebFetch, không tự nhớ/đoán 1 URL "trông hợp lý".
3. Kiểm tra ảnh thực sự khớp nội dung (đúng chủ đề, không lệch ngữ cảnh ngành) và không có watermark/logo hãng ảnh đè lên.
4. Viết `alt` text mô tả cụ thể nội dung ảnh (phục vụ cả SEO lẫn accessibility) — không dùng lại cùng 1 ảnh cho nhiều bài viết/section có nội dung khác nhau.
5. Không bắt buộc ghi nguồn (Unsplash/Pexels/Pixabay License không yêu cầu attribution), nhưng có thể thêm 1 dòng credit nhỏ ở footer trang đó nếu muốn tăng tính xác thực cho demo.

**Fallback khi môi trường không có WebSearch/WebFetch** (hoặc không truy cập được internet): quay về minh hoạ SVG trừu tượng/placeholder có nhãn rõ ràng theo cách `reference/landing-page.md` đang mô tả cho hero visual — không tự bịa 1 URL ảnh stock để lấp chỗ trống.

**Cấm:**
- Không dùng ảnh từ kết quả tìm kiếm ảnh tổng quát (Google Images và tương tự) — nguồn không rõ giấy phép, dễ dính watermark/bản quyền của bên thứ 3.
- Không tự đoán/bịa URL Unsplash/Pexels/Pixabay theo trí nhớ mẫu — link chết hoặc sai ảnh là lỗi nghiêm trọng hơn không có ảnh.
- Không lặp lại đúng 1 ảnh cho nhiều nội dung khác nhau chỉ để "cho có ảnh".
