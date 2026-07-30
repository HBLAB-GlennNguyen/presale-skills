# QnA dựng UI Kit

Hỏi 7 câu dưới đây trước khi generate bất kỳ màn hình nào — đây là UI kit của SẢN PHẨM TƯƠNG LAI CỦA KHÁCH HÀNG, không dùng branding HBLAB. Ghi lại câu trả lời vào `output/prototype/ui-kit-brief.md` để dùng nhất quán cho mọi màn hình và để chỉnh sửa lại sau nếu cần.

## Câu hỏi

1. **Màu thương hiệu chính/phụ của khách hàng** — mã hex nếu có, hoặc mô tả chung (vd "xanh dương đậm") nếu chưa có mã cụ thể.
2. **Logo** — đường dẫn file nếu có sẵn; nếu không, dùng tên công ty dạng text làm logo placeholder.
3. **Phong cách/mood mong muốn** — chọn 1: Hiện đại (Modern) / Chuyên nghiệp-trang trọng (Professional) / Tối giản (Minimal) / Năng động-trẻ trung (Dynamic).
4. **Sản phẩm/app tham chiếu khách hàng thích** (tùy chọn) — nếu có, dùng làm cảm hứng layout, không copy nguyên xi. Nếu khách hàng không nêu, TỰ chọn 2-3 phần mềm/app thực tế nổi tiếng cùng lĩnh vực dựa trên ngành nghề trong `requirements-summary.md` (vd hệ quản trị kho/ERP → tham khảo pattern kiểu SAP Fiori/NetSuite/Odoo; app đặt xe/giao hàng → tham khảo Grab/GoJek; nền tảng quản lý dự án → tham khảo Jira/Notion/Linear; dashboard vận hành/CRM → tham khảo Salesforce/HubSpot; hệ quản lý dữ liệu/danh sách dạng bảng nhiều trường → tham khảo Airtable) — không được bỏ trống mục này.
5. **Đối tượng người dùng chính** — mức độ thành thạo công nghệ: Người dùng có năng lực CNTT tốt (nhân viên IT, kỹ thuật) / Người dùng văn phòng phổ thông / Người dùng đại chúng (public, đa dạng độ tuổi/kỹ năng).
6. **Loại phần mềm** — Nội bộ (internal, có đào tạo trước khi dùng — ưu tiên hiển thị nhiều thông tin/mật độ dữ liệu cao) hoặc Public (người dùng phổ thông — ưu tiên hiện đại, tối giản, dễ dùng ngay không cần hướng dẫn).
7. **Ngôn ngữ giao diện prototype** — Tiếng Việt hoặc Tiếng Anh (mặc định đề xuất Tiếng Việt nếu khách hàng không nêu, vì đây là mẫu presale nội bộ; hỏi lại nếu đối tượng người dùng cuối/khách hàng là quốc tế). Chỉ chọn 1 ngôn ngữ chính cho toàn bộ prototype — không làm song ngữ trừ khi người dùng yêu cầu rõ ràng.

## Suy ra UI Kit từ câu trả lời

**Ngôn ngữ giao diện (ghi rõ vào `ui-kit-brief.md`):** ngôn ngữ đã chọn ở câu 7 áp dụng cho TOÀN BỘ nội dung hiển thị trên mọi màn hình — nhãn menu, breadcrumb, tiêu đề, nút hành động, placeholder, thông báo/toast, và mock data — nhất quán xuyên suốt, không trộn lẫn 2 ngôn ngữ trong cùng 1 màn hình. Các ví dụ tiếng Việt trong `screen-generation-guide.md`/`interactivity-guide.md` (vd "Lưu"/"Hủy", "Tạo thành công") chỉ là minh hoạ — dịch sang tiếng Anh tương đương nếu câu 7 chọn Tiếng Anh (vd "Save"/"Cancel", "Created successfully"). Tên thư mục/file màn hình (`screens/<module>/<tên màn hình>/`) vẫn giữ theo tên tiếng Việt trong `scope-and-sitemap.md` bất kể ngôn ngữ giao diện — đó là slug nội bộ, không phải nội dung hiển thị cho người dùng.

**Product archetype (suy luận tự động — không hỏi thêm câu nào, không tạo bộ ui-kit riêng theo từng ngành để đỡ phải bảo trì nhiều bộ):** dựa vào ngành nghề + bối cảnh dự án trong `requirements-summary.md` và câu trả lời Q6 (Loại phần mềm), xếp dự án vào 1 trong 4 archetype dưới đây — ghi rõ archetype đã chọn vào `ui-kit-brief.md`, dùng để hiệu chỉnh độ táo bạo màu, trọng tâm layout và tông giọng xuyên suốt mọi màn hình (thay cho phần "Density" cũ):

| Archetype | Khi nào áp dụng | Độ táo bạo màu | Trọng tâm layout | Tông giọng/copy |
|---|---|---|---|---|
| **Nội bộ/Vận hành** (ERP, CMS quản trị, dashboard vận hành, quản lý kho/logistics...) | Loại phần mềm = Nội bộ, ngành nghiêng về vận hành/quản lý | Vừa-cao: sidebar nền màu đặc, KPI card nhiều dải màu, nhưng content area giữ nền sáng để đọc dữ liệu lâu không mỏi mắt | Data-dense kiểu Airtable: sidebar thu gọn/mở rộng được (icon-rail khi thu gọn), toolbar ngang gọn (chip filter/sort/group) thay vì filter bar to, bảng nhiều cột mật độ cao — xem chi tiết `screen-generation-guide.md` | Ngắn gọn, thuật ngữ nghiệp vụ, ít giải thích (người dùng IT-savvy) |
| **Public/Thương mại** (booking, e-commerce, đặt hàng/đặt chỗ trực tiếp khách hàng) | Loại phần mềm = Public, có luồng bán hàng/đặt chỗ trực tiếp | Cao: dùng gradient, hình khối trang trí, ảnh minh họa nhiều hơn — nhất là màn hình Đăng nhập/Trang chủ | Marketing-led ở màn hình đầu (Trang chủ/Đăng nhập), balanced hơn ở màn hình tác vụ | Thân thiện, hướng dẫn rõ ràng, CTA nổi bật |
| **Tài chính/Compliance nặng** (ngân hàng, bảo hiểm, y tế, hàng không có chứng chỉ/audit) | `requirements-summary.md` có yêu cầu tuân thủ/audit cao ở mục "Yêu cầu phi chức năng" | Thấp-vừa: màu dùng để phân biệt trạng thái/mức rủi ro rõ ràng hơn là trang trí — tránh gradient/hình khối phù phiếm | Data-dense, ưu tiên số liệu chính xác (`tabular-nums`), badge trạng thái/audit trail phải rất rõ | Trang trọng, chính xác, không dùng ngôn ngữ kiểu marketing |
| **Nội dung/Marketing** (CMS nội dung, portal giới thiệu, trang thông tin) | Chức năng chính là quản lý & hiển thị nội dung, không phải giao dịch/vận hành | Vừa: màu dùng nhấn nhá cho ảnh/card nội dung, không tràn lan | Ảnh/card-led thay vì bảng dữ liệu dày đặc, nhiều khoảng trắng | Thân thiện, biên tập, câu chữ tự nhiên |

Nếu mood ở câu 3 và archetype có vẻ lệch nhau (vd khách chọn mood Dynamic nhưng archetype là Tài chính/Compliance nặng), ưu tiên mood khách hàng chọn cho phong cách thị giác (bo góc, gradient, độ rực màu), nhưng vẫn giữ nguyên yêu cầu về độ rõ ràng số liệu/badge trạng thái của archetype đó — 2 trục này không loại trừ nhau.

**Sản phẩm tham khảo (ghi rõ vào `ui-kit-brief.md`):** liệt kê 2-3 tên sản phẩm/app thực tế đã chọn ở câu 4, ưu tiên chọn trong cùng archetype vừa xác định ở trên (vd archetype Tài chính/Compliance → tham khảo Stripe Dashboard/hệ thống backoffice ngân hàng thay vì ERP chung chung) — đây là điểm neo bố cục & component pattern dùng LẠI cho mọi màn hình khi generate (không suy luận lại mỗi màn hình một kiểu). Khi dựng từng màn hình, tự hỏi "màn hình tương đương trong [sản phẩm tham khảo] trông thế nào" rồi áp dụng cấu trúc/pattern đó (không copy màu/logo/brand) — đây là cách để prototype trông như phần mềm thật đã hoàn thiện, không phải wireframe.

**Bảng màu (đủ chiều sâu — đây là nguyên nhân số 1 khiến prototype trông "trắng đen" nếu làm sơ sài):**
- Primary = màu chính khách hàng cung cấp (hoặc mã hex gần nhất nếu chỉ có mô tả chung).
- Primary-dark = bản đậm/tối của primary (đậm hơn ~50-70%, ngả sắc navy/tối chứ không chỉ đậm hơn 15-20%) — dùng cho: nền khu vực điều hướng chính (sidebar/header), màu chữ heading/số liệu nổi bật, nút primary.
- Primary-50, Primary-100 = 2 sắc nhạt gần trắng của primary — dùng cho background nhấn nhẹ, hover state, badge info.
- Accent = MỘT màu thứ hai khác primary (khách hàng cung cấp nếu có; nếu không, tự chọn màu tương phản/bổ túc với primary — vd primary lạnh thì accent ấm) — dùng cho nút CTA đặc biệt và 1 điểm nhấn nổi bật mỗi màn hình, không dùng tràn lan để không loãng với primary.
- Neutral gray: dải đầy đủ 9 sắc độ (gray-50 → gray-900, cách nhau đều) cho text/border/background — không rút gọn còn 5.
- 3 màu trạng thái chuẩn: Success (xanh lá), Warning (vàng/cam), Error (đỏ) — mỗi màu có thêm 1 bản nhạt riêng (vd success-bg) dùng làm nền badge/banner; không lấy trùng primary nếu primary đã là các màu này.

**Nguyên tắc dùng màu (bắt buộc — không được để UI mặc định thành trắng/xám + vài chấm màu nhỏ):**
- Khu vực điều hướng chính (sidebar nếu Nội bộ, header/topbar nếu Public) PHẢI có nền màu đặc hoặc gradient dựng từ Primary-dark — không dùng nền trắng/xám cho khu vực này. Đây là mảng màu lớn nhất trên màn hình, quyết định cảm giác "có màu" hay "trắng đen" ngay từ cái nhìn đầu.
- Heading (H1-H3), số liệu nổi bật trên KPI/stat card, và text nhấn mạnh (vd `cell-strong` trong bảng) dùng màu Primary-dark thay vì đen/gray-900 mặc định.
- Định nghĩa tối thiểu 4 kiểu nút trong `global.css` và dùng đúng vai trò, không lặp 1 kiểu nút cho mọi hành động: `btn-primary` (nền Primary-dark đặc), `btn-accent` (nền Accent đặc, chỉ 1 nút accent nổi bật mỗi màn hình), `btn-outline` (viền, nền surface), `btn-ghost` (không viền không nền, cho hành động phụ như Hủy).
- Badge/status pill luôn có nền màu nhạt tương ứng (`-bg`) + chữ màu đậm cùng tông (success/warning/error/info) — không dùng nền xám cho mọi trạng thái.
- KPI/stat card có 1 dải màu mỏng (3-4px, top hoặc trái) theo loại chỉ số (primary/accent/success/warning) để mỗi thẻ có điểm nhận diện màu riêng thay vì toàn bộ card trắng giống hệt nhau.

**Typography:** chọn 1 cặp font Google Fonts sans-serif rõ ràng, dễ đọc (vd Inter, Roboto, hoặc tương tự) — không cần font đặc biệt trừ khi khách hàng có yêu cầu riêng. Định nghĩa type scale rõ ràng trong `global.css` (không để mặc định trình duyệt): H1 28-32px/700, H2 22-24px/600, H3 18-20px/600, Body 14-15px/400, Caption/label 12-13px/500, line-height 1.4-1.6 cho body.

**Spacing scale:** dùng lưới bội số 4px xuyên suốt (4/8/12/16/24/32/48px) cho padding, margin, gap — không dùng số tùy tiện (vd 13px, 22px). Card/section padding tối thiểu 16-24px, khoảng cách giữa các block chính 24-32px — tránh nội dung dí sát cạnh trông như wireframe.

**Border-radius & shadow/elevation (theo mood):**
- Baseline mặc định cho MỌI mood (kể cả Professional/Minimal — sản phẩm B2B thật hiện nay vẫn bo tròn, không vuông cứng): card/modal 12-16px, input/button 8-10px, badge/pill/avatar dùng bo tròn tối đa (999px).
- Modern/Dynamic: lấy ở cận trên của baseline, shadow rõ rệt hơn, có thể dùng gradient nhẹ trên sidebar/nút chính/hero.
- Professional/Minimal: lấy ở cận dưới của baseline (không xuống dưới 8px cho card), shadow nhẹ hơn — nhưng KHÔNG bỏ bo góc hoàn toàn (0-2px chỉ dùng khi khách hàng yêu cầu rõ ràng phong cách vuông vắn kiểu form giấy tờ/chính phủ).
- Shadow nhuốm nhẹ sắc Primary-dark (vd `rgba(<primary-dark-rgb>, 0.08)`) thay vì đen thuần (`rgba(0,0,0,...)`) — giúp shadow đồng bộ với bảng màu thay vì trông xám xịt tách rời.
- Định nghĩa 3 cấp elevation trong `global.css` và dùng nhất quán, không tự chế mỗi màn hình một shadow khác nhau: cấp 0 (flat, dùng cho input/table row), cấp 1 (card mặc định, shadow nhẹ), cấp 2 (dropdown/hover card, shadow rõ hơn), cấp 3 (modal/popup, shadow đậm nhất + overlay nền mờ).

**Icon:** dùng 1 bộ icon outline nhất quán (style Lucide/Feather — stroke ~1.5-2px, `currentColor` để ăn theo màu chữ), nhúng trực tiếp dạng inline SVG trong HTML (không cần tải file ngoài). Icon là BẮT BUỘC, không phải tùy chọn — dùng cho: mục menu/sidebar, nút hành động chính (Tạo mới, Lưu, Xóa...), action trên từng dòng bảng (Xem/Sửa/Xóa), thẻ KPI/stat card ở dashboard, trạng thái rỗng (empty state), icon chuông/thông báo và avatar user ở header. Thiếu icon ở các vị trí này là dấu hiệu prototype đang trông như wireframe.

**Mức độ hỗ trợ người dùng (theo đối tượng sử dụng):**
- Người dùng IT/kỹ thuật: ít tooltip/hướng dẫn, có thể dùng thuật ngữ kỹ thuật.
- Người dùng văn phòng phổ thông: tooltip cho thao tác không hiển nhiên, label rõ ràng.
- Người dùng đại chúng: hướng dẫn/placeholder text đầy đủ ở mọi input, tránh thuật ngữ kỹ thuật, có empty-state hướng dẫn khi chưa có dữ liệu.
