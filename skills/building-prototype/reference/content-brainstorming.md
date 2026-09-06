# Brainstorm khung nội dung Homepage (trước khi viết content thật)

Áp dụng khi Loại dự án = Landing page, tại bước "Identify the entry flow / homepage" trong `SKILL.md` — đây là bản đầy đủ của mục "Bố cục Homepage" trong `reference/landing-page.md`: không chỉ chốt THỨ TỰ section mà còn chốt GÓC THÔNG ĐIỆP của từng section trước khi viết copy thật, theo tinh thần cộng tác giống skill brainstorming nhưng áp dụng riêng cho nội dung landing page (1 vòng đề xuất-xác nhận, không phải phỏng vấn nhiều vòng như brainstorming đầy đủ).

## Vì sao cần bước này

Nếu bỏ qua brainstorm khung nội dung mà generate copy luôn theo mặc định, dễ ra 1 landing page "đúng cấu trúc nhưng nhạt" — hero đúng công thức headline+subheadline nhưng không có góc nhấn riêng, value props liệt kê đúng 3-4 khối nhưng không phải đúng 3-4 điểm mạnh nhất của khách hàng cụ thể này. Bước này ép phải chọn góc tiếp cận CỤ THỂ cho từng section, dựa trên dữ liệu thật trong `requirements-summary.md`, trước khi viết copy hoàn chỉnh — tương tự cách "Điểm nhấn riêng" trong `ui-kit-qna.md` ép chọn 1 signature moment thị giác cụ thể thay vì generic-safe, chỉ khác đây là cho nội dung/copy.

## Quy trình (1 vòng đề xuất — xác nhận)

1. **Rút chất liệu:** đọc lại `requirements-summary.md`/`scope-and-sitemap.md`, liệt kê: 3-5 điểm mạnh/khác biệt CỤ THỂ của sản phẩm/dịch vụ khách hàng (không phải đặc điểm chung của cả ngành — áp dụng đúng bài kiểm tra "nếu ý tưởng dùng nguyên xi được cho khách hàng khác cùng ngành thì chưa đủ cụ thể" như `ui-kit-qna.md` đã dùng cho Điểm nhấn riêng), 1-2 số liệu/bằng chứng cụ thể nếu có, chân dung khách hàng mục tiêu chính.
2. **Đề xuất khung nội dung cho từng section** trong thứ tự đã chốt (Hero, Value props, How it works, Social proof, Bảng giá, FAQ, CTA cuối...):
   - **Hero:** đề xuất 2-3 HƯỚNG headline khác nhau (góc lợi ích/outcome, góc khác biệt cạnh tranh, góc nỗi đau→giải pháp...), mỗi hướng kèm 1 câu ví dụ minh hoạ — để người dùng chọn HƯỚNG tiếp cận, không phải chọn câu chữ hoàn chỉnh cuối cùng ngay từ bước này.
   - **Value props:** đề xuất ĐÚNG 3-4 điểm sẽ làm nổi bật (không liệt kê hết mọi tính năng có), lấy từ danh sách điểm mạnh ở bước 1, sắp theo độ thuyết phục giảm dần.
   - **Social proof:** đề xuất hình thức phù hợp (logo khách hàng mock / trích dẫn testimonial / số liệu cụ thể) tùy dự án có chất liệu thật để dùng hay phải mock hợp lý theo ngành.
   - **Bảng giá (nếu áp dụng):** đề xuất số gói + tên gọi từng gói phù hợp phân khúc khách hàng mục tiêu (không mặc định "Cơ bản/Nâng cao/Doanh nghiệp" nếu ngữ cảnh gợi ý tên khác sát hơn).
   - **FAQ:** đề xuất 4-6 câu hỏi mà đúng khách hàng mục tiêu của dự án này hay hỏi trước khi mua/dùng thử, không phải câu hỏi chung chung mọi landing page nào cũng có.
3. **Trình bày toàn bộ khung đề xuất trong 1 lần** cho người dùng xem — không hỏi tách lẻ từng section nhiều lượt (trừ khi người dùng chủ động muốn đào sâu 1 section cụ thể sau khi xem tổng thể). Người dùng có thể chấp nhận toàn bộ, chỉnh sửa vài mục, hoặc yêu cầu đề xuất thêm phương án khác cho 1 section.
4. **Ghi khung đã xác nhận** vào `ui-kit-brief.md` mục "Khung nội dung Homepage" — đây là input bắt buộc cho bước viết copy thật, không viết tự do lại từ đầu ở bước sau.

## Chuyển sang viết content thật

Sau khi khung nội dung được xác nhận, viết copy hoàn chỉnh cho từng section đúng theo góc/thông điệp đã chốt, áp dụng quy tắc viết + SEO/AI-SEO trong `reference/content-and-seo.md`. Nếu trong lúc viết phát hiện góc đã chọn thiếu chất liệu (vd `requirements-summary.md` không đủ thông tin cụ thể để viết đúng hướng đã chọn), quay lại hỏi người dùng bổ sung thay vì tự bịa chi tiết không có căn cứ.

## Áp dụng cho trang phụ khác Trang chủ

Trang phụ (About, Dịch vụ, Blog...) không lặp lại toàn bộ quy trình 4 bước trên — chỉ Trang chủ (nơi quyết định ấn tượng đầu tiên và có nhiều section cần góc tiếp cận riêng biệt) mới brainstorm khung nội dung đầy đủ kiểu này. Trang phụ áp dụng thẳng `reference/content-and-seo.md` theo từng loại trang, tham chiếu ngược lại các điểm mạnh/số liệu đã liệt kê ở bước 1 để giữ thông điệp nhất quán xuyên suốt site.
