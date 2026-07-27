# QnA dựng UI Kit

Hỏi 6 câu dưới đây trước khi generate bất kỳ màn hình nào — đây là UI kit của SẢN PHẨM TƯƠNG LAI CỦA KHÁCH HÀNG, không dùng branding HBLAB. Ghi lại câu trả lời vào `output/prototype/ui-kit-brief.md` để dùng nhất quán cho mọi màn hình và để chỉnh sửa lại sau nếu cần.

## Câu hỏi

1. **Màu thương hiệu chính/phụ của khách hàng** — mã hex nếu có, hoặc mô tả chung (vd "xanh dương đậm") nếu chưa có mã cụ thể.
2. **Logo** — đường dẫn file nếu có sẵn; nếu không, dùng tên công ty dạng text làm logo placeholder.
3. **Phong cách/mood mong muốn** — chọn 1: Hiện đại (Modern) / Chuyên nghiệp-trang trọng (Professional) / Tối giản (Minimal) / Năng động-trẻ trung (Dynamic).
4. **Sản phẩm/app tham chiếu khách hàng thích** (tùy chọn) — nếu có, dùng làm cảm hứng layout, không copy nguyên xi.
5. **Đối tượng người dùng chính** — mức độ thành thạo công nghệ: Người dùng có năng lực CNTT tốt (nhân viên IT, kỹ thuật) / Người dùng văn phòng phổ thông / Người dùng đại chúng (public, đa dạng độ tuổi/kỹ năng).
6. **Loại phần mềm** — Nội bộ (internal, có đào tạo trước khi dùng — ưu tiên hiển thị nhiều thông tin/mật độ dữ liệu cao) hoặc Public (người dùng phổ thông — ưu tiên hiện đại, tối giản, dễ dùng ngay không cần hướng dẫn).

## Suy ra UI Kit từ câu trả lời

**Bảng màu:**
- Primary = màu chính khách hàng cung cấp (hoặc mã hex gần nhất nếu chỉ có mô tả chung).
- Sinh thêm: Primary-dark (đậm hơn ~15-20%, dùng cho hover/active), Primary-light (nhạt hơn, dùng cho background nhấn nhẹ), dải neutral gray (5-7 sắc độ cho text/border/background), và 3 màu trạng thái chuẩn: Success (xanh lá), Warning (vàng/cam), Error (đỏ) — không lấy trùng với primary nếu primary đã là các màu này.

**Typography:** chọn 1 cặp font Google Fonts sans-serif rõ ràng, dễ đọc (vd Inter, Roboto, hoặc tương tự) — không cần font đặc biệt trừ khi khách hàng có yêu cầu riêng.

**Border-radius & shadow (theo mood):**
- Modern/Dynamic: bo góc vừa-nhiều (8-16px), shadow rõ, có thể dùng gradient nhẹ.
- Professional/Minimal: bo góc ít (2-6px), phẳng, shadow rất nhẹ hoặc không có.

**Density (theo loại phần mềm):**
- Nội bộ: bảng dữ liệu nhiều cột, spacing chặt, hiển thị nhiều thông tin cùng lúc, filter/sort nâng cao hiển thị sẵn.
- Public: spacing thoáng, mỗi màn hình tập trung 1 tác vụ chính, ẩn bớt tùy chọn nâng cao sau menu phụ.

**Mức độ hỗ trợ người dùng (theo đối tượng sử dụng):**
- Người dùng IT/kỹ thuật: ít tooltip/hướng dẫn, có thể dùng thuật ngữ kỹ thuật.
- Người dùng văn phòng phổ thông: tooltip cho thao tác không hiển nhiên, label rõ ràng.
- Người dùng đại chúng: hướng dẫn/placeholder text đầy đủ ở mọi input, tránh thuật ngữ kỹ thuật, có empty-state hướng dẫn khi chưa có dữ liệu.
