# Presale Skills (`hbg`)

Bộ 4 skill Claude Code hỗ trợ quy trình presale: từ phân tích RFP đến ước lượng effort, viết proposal, và dựng UI prototype.

```
analyzing-rfp ──┬──> estimating-effort ──> writing-proposal
                └──────────────────────────> building-prototype
```

- `estimating-effort` và `writing-proposal` cần chạy đúng thứ tự (mỗi skill đọc output của skill trước).
- `building-prototype` chỉ cần output của `analyzing-rfp` (function list + sitemap), chạy độc lập với `estimating-effort`/`writing-proposal`. Nếu đã chạy `building-prototype` từ trước khi chạy `writing-proposal`, proposal sẽ tự thêm mục "Demo tương tác" — nên cân nhắc chạy sớm dù thứ tự vẫn là tùy chọn.

## Cài đặt

### Từ GitHub (khuyến nghị — dùng được ở mọi máy, không phụ thuộc đường dẫn local)

```
/plugin marketplace add HBLAB-GlennNguyen/presale-skills
/plugin install hbg@presale-skills
```

### Từ thư mục local (khi đang phát triển/sửa skill trên máy này)

```
/plugin marketplace add "/Users/thinhnd1/Study/Presale Skill"
/plugin install hbg@presale-skills
```

Chỉ nên cài 1 trong 2 cách trên cho cùng máy — cài cả 2 sẽ tạo 2 marketplace trùng tên plugin, dễ nhầm bản đang dùng là bản nào. Nếu đang có bản local và muốn chuyển sang bản GitHub (hoặc ngược lại), gỡ marketplace cũ trước: `/plugin marketplace remove <tên marketplace cũ>`.

Sau khi cài, **mở phiên Claude Code mới** (đóng và mở lại cửa sổ/terminal) để nạp lại danh sách skill — phiên đang chạy lúc cài sẽ không thấy skill mới ngay.

Cài xong, 4 skill gọi được qua: `hbg:analyzing-rfp`, `hbg:estimating-effort`, `hbg:writing-proposal`, `hbg:building-prototype`.

## Hướng dẫn chạy end-to-end test

### Bước 0 — Tạo thư mục làm việc cho 1 deal

Tất cả output ghi vào `./output/` **tương đối theo thư mục đang mở**, nên tạo và mở riêng 1 thư mục cho từng deal trước khi bắt đầu, ví dụ:

```
mkdir -p ~/Deals/ABC-Logistics-presale
cd ~/Deals/ABC-Logistics-presale
```

Mở thư mục này trong Claude Code (hoặc `cd` vào đó nếu dùng CLI) rồi mới gọi skill.

### Bước 1 — `hbg:analyzing-rfp`

Gọi skill, đưa vào 1 trong các dạng input: file RFP đính kèm, ghi chú họp dán vào chat, hoặc mô tả ngắn từ sales.

Skill sẽ:
- Đọc/điền thông tin từ input, tự nhận định input là "tóm tắt/notes" hay "file RFP đầy đủ" và hỏi xác nhận — quyết định ngưỡng hoàn thiện áp dụng ở bước cuối (70% cho tóm tắt, 90% cho RFP đầy đủ)
- Đề xuất bổ sung các chức năng master data/quản trị hệ thống thường bị thiếu trong RFP, và dựng thảo bảng phân tích đối tượng nghiệp vụ & vòng đời — xin xác nhận từng phần
- Dựng thảo bảng đối tượng sử dụng & nhiệm vụ, sitemap, và 2-4 luồng nghiệp vụ chính (kèm state diagram + screen flow) — xin xác nhận từng phần
- Trò chuyện theo kiểu tư vấn để làm rõ các phần còn thiếu (không phải hỏi máy móc từng ô trống)
- Nếu độ hoàn thiện dưới ngưỡng áp dụng, cảnh báo và hỏi có muốn tiếp tục với giả định hay bổ sung thêm

**Output** (`./output/`):
- `requirements-summary.md`
- `scope-and-sitemap.md` — bao gồm phạm vi chức năng, bảng phân tích đối tượng nghiệp vụ & vòng đời (dùng để chọn độ phức tạp ở bước estimating-effort), bảng đối tượng sử dụng & nhiệm vụ, sitemap, và các luồng nghiệp vụ chính kèm state diagram/screen flow (building-prototype dùng lại danh sách này)
- `clarifying-questions.md` — chia 3 nhóm Sale / Domain-BA / Technical, mỗi câu dạng tư vấn (Yes/No hoặc lựa chọn) để gửi khách hàng
- `risk-assessment.md` — ma trận rủi ro Likelihood × Impact

### Bước 2 — `hbg:estimating-effort`

Chạy sau khi Bước 1 đã có đủ 4 file trên (đặc biệt `scope-and-sitemap.md` phải có sitemap, không còn "*Chưa có sitemap chi tiết*").

Skill sẽ:
- Chọn phương pháp: bottom-up theo function (≤100 màn hình) hoặc 3-point/PERT theo màn hình (>100 màn hình)
- Áp buffer theo mức rủi ro từ `risk-assessment.md`
- Dựng master schedule (dùng timeline khách hàng nếu có, hoặc tự đề xuất)
- Đề xuất cơ cấu team, gắn với từng giai đoạn

**Output** (`./output/`):
- `effort-breakdown.md`
- `master-schedule.md`
- `team-composition.md`

### Bước 3 — `hbg:writing-proposal`

Chạy sau khi Bước 1 và 2 đã đủ file (7 file input tổng cộng).

Skill sẽ hỏi 2 việc trước khi viết:
1. Dự án có phải migration/renewal hệ thống cũ không (1 câu hỏi trực tiếp)
2. Cổng tương tác Technical Solution: cloud provider, kiến trúc, tech stack — có gợi ý sẵn để chọn, có thể chọn "Khác" để tự mô tả

**Output** (`./output/`):
- `proposal-outline.md` — gồm phần Design & Theme brief (branding HBLAB) + Content detail (Part 0-5 theo cấu trúc chuẩn), sẵn sàng đưa vào công cụ AI generate slide

### Bước 4 — `hbg:building-prototype`

Chạy sau khi Bước 1 đã có `scope-and-sitemap.md` (không cần chờ Bước 2, 3). Chạy bước này trước Bước 3 là tùy chọn, nhưng nếu làm vậy, `proposal-outline.md` ở Bước 3 sẽ có thêm mục "Demo tương tác" trỏ tới prototype.

Skill sẽ hỏi:
1. Bộ QnA dựng UI kit (6 câu: màu thương hiệu, logo, mood, app tham chiếu, đối tượng người dùng, loại phần mềm)
2. Xác nhận 2-4 workflow chính (sẽ có tương tác đầy đủ, các màn hình khác chỉ có UI + điều hướng)

**Output** (`./output/prototype/`):
- `assets/css/global.css`, `assets/js/global.js`
- `index.html` (trang chủ, link tới tất cả màn hình)
- `screens/<module>/<tên màn hình>/{index.html, style.css, script.js}`
- `ui-kit-brief.md`, `progress.md`

Mở `output/prototype/index.html` trực tiếp bằng trình duyệt để xem, không cần server.

## Ghi chú

- Mỗi skill từ chối chạy nếu thiếu output của skill trước — sẽ báo rõ cần chạy skill nào trước.
- Chạy lại 1 skill sẽ ghi đè output cũ của skill đó (trừ `building-prototype`, có `progress.md` để resume thay vì làm lại từ đầu).
- File `docs/superpowers/specs/` và `docs/superpowers/plans/` trong repo này là lịch sử thiết kế/triển khai 4 skill — không phải một phần của plugin khi cài.
