# Cấu trúc Proposal Outline

Cấu trúc "Content detail" của `proposal-outline.md`. Mỗi Part bắt đầu bằng 1 slide Header chuyển phần (xem `design-theme.md`). Với mỗi mục dưới đây: nguồn dữ liệu chỉ rõ lấy từ đâu — nếu ghi "tổng hợp", nghĩa là cần tổng hợp/diễn giải từ nhiều nguồn, không copy nguyên văn.

## Part 0: Opening (1-3 slide)

- **Cover page** — tên dự án, tên khách hàng (từ "Tên khách hàng/công ty" trong requirements-summary.md), ngày, logo HBLAB.
- **About HBLAB** — giới thiệu công ty. Không có nguồn tự động từ 2 skill trước; dùng nội dung boilerplate chung (kinh nghiệm, quy mô, thế mạnh) và đánh dấu rõ để người dùng tự cập nhật nội dung mới nhất trước khi gửi khách hàng.
- **Agenda** — tự sinh danh sách từ tên các Part và mục con chính bên dưới (không phải liệt kê từng slide chi tiết, chỉ các đầu mục lớn).

## Part 1: Business Value

- **About customer business & customer expectation** — tổng hợp từ "Thông tin khách hàng & bối cảnh dự án" và "Tiêu chí thành công" trong requirements-summary.md.
- **As-is System** *(optional — chỉ thêm nếu người dùng xác nhận đây là dự án migration/renewal, hỏi ngay đầu quy trình)* — tổng hợp từ "Công nghệ / hệ thống liên quan" (stack hiện tại) và phần bối cảnh liên quan đến hệ thống cũ.
- **Pain Points** — tổng hợp: suy ra từ "Bối cảnh / lý do triển khai dự án", "Ràng buộc & giả định", và các rủi ro có Likelihood cao trong risk-assessment.md. Viết dạng danh sách ngắn gọn, mỗi pain point 1 câu, cụ thể (không viết chung chung).
- **Risk matrix** — trực tiếp từ risk-assessment.md: bảng 8 rủi ro với Likelihood, Impact, điểm, mức (Thấp/Trung bình/Cao/Nghiêm trọng).
- **Pain Points & Solution Mapping** — tổng hợp: bảng 2 cột nối mỗi Pain Point với module/tính năng (trong "Danh sách chức năng/module chính" của scope-and-sitemap.md) giải quyết nó trực tiếp.
- **Business value impact** — tổng hợp: 1 core message định vị giá trị tổng thể (1 câu), kèm 2-4 value driver cụ thể (vd: giảm thời gian xử lý X%, giảm sai sót thao tác thủ công, tăng khả năng ra quyết định nhờ báo cáo real-time...) suy ra từ pain points + ngành nghề + loại hình khách hàng.

## Part 2: Technical Solution

- **Phương án tiếp cận chung** — từ master-schedule.md: liệt kê từng giai đoạn (phase) kèm output/kết quả kỳ vọng của giai đoạn đó (tổng hợp từ module liên quan + mục tiêu giai đoạn).
- **Danh sách modules chính** — trực tiếp từ "Danh sách chức năng/module chính" trong scope-and-sitemap.md.
- **Đối tượng sử dụng chính** — trực tiếp từ bảng "Đối tượng sử dụng & nhiệm vụ" trong scope-and-sitemap.md (vai trò người dùng + nhiệm vụ chính, tóm gọn theo vai trò và nhiệm vụ cốt lõi — không cần chép lại mô tả chi tiết nếu quá dài).
- **Luồng nghiệp vụ chính** — tái sử dụng trực tiếp state diagram và screen flow (dạng Mermaid) từ mục "Luồng nghiệp vụ chính (Workflow)" trong scope-and-sitemap.md cho các workflow đã xác nhận — không vẽ lại hay diễn giải thành văn xuôi, giữ nguyên dạng diagram.
- **To-be System** *(nếu migration/renewal)* **hoặc High-level System Architecture** *(nếu không)* — từ kết quả cổng tương tác Technical Solution (xem `SKILL.md` bước tương ứng và `tech-solution-options.md`).
- **Technologies stack** — từ lựa chọn ở cổng tương tác, đối chiếu với "Công nghệ / hệ thống liên quan" hiện tại của khách hàng để đảm bảo tương thích/tích hợp được.
- **Infrastructure diagram** — mô tả bằng text luồng kết nối giữa các service đã chọn (đây là outline text để AI tool tự vẽ diagram, không phải hình ảnh thật).
- **Infrastructure description** — giải thích lý do chọn từng service, đối chiếu với yêu cầu phi chức năng (hiệu năng/bảo mật/khả năng mở rộng) trong requirements-summary.md.
- **Đảm bảo chất lượng (QA, testing strategy, UAT)** — tổng hợp từ vai trò QA trong team-composition.md, giai đoạn Kiểm thử & UAT trong master-schedule.md, và mô tả quy trình test chuẩn (unit test, integration test, UAT với khách hàng trước go-live).
- **Warranty & Maintenance model** — từ `warranty-communication.md`.

## Part 3: Working Model

- **Engagement model** — trực tiếp từ "Mô hình hợp tác / hợp đồng mong muốn" (ODC/T&M/Fixed Price) trong requirements-summary.md.
- **Team structure** — sơ đồ tổ chức 3 cấp chuẩn:
  - Cấp 1 (đầu mối dự án): Project Manager (PM) — làm việc trực tiếp với đầu mối khách hàng.
  - Cấp 2 (kỹ thuật): Tech Lead, BA Lead — báo cáo PM.
  - Cấp 3 (thực thi): Dev team và QA team báo cáo Tech Lead; Designer báo cáo PM hoặc Tech Lead tùy quy mô dự án.
- **Role & Responsibilities** — trực tiếp từ bảng "Vai trò & trách nhiệm hai bên" trong requirements-summary.md.
- **Communication plan** — từ `warranty-communication.md`.

## Part 4: Closing

- **Master schedule** — trực tiếp từ master-schedule.md.
- **Deliverable** — 2 phần, vị trí tách biệt:
  1. Danh sách deliverable chuẩn theo loại output bàn giao: mã nguồn đầy đủ (source code + quyền truy cập version control), tài liệu kỹ thuật (kiến trúc, API spec, database schema), tài liệu hướng dẫn sử dụng, đào tạo người dùng/đội vận hành, triển khai lên môi trường production/staging theo thỏa thuận, bảo hành sau go-live.
  2. Tham chiếu ngắn gọn lại "Danh sách modules chính" đã trình bày ở Part 2 (không lặp lại chi tiết, chỉ nhắc đây là các module được bàn giao).
- **Resource plan** — trực tiếp từ team-composition.md (bảng headcount theo giai đoạn).
- **Demo tương tác** *(chỉ thêm nếu `./output/prototype/index.html` đã tồn tại)* — 1 dòng dẫn tới đường dẫn demo tương tác đã dựng ở building-prototype, đặt trước Quotation để củng cố niềm tin trước khi chốt. Bỏ qua mục này hoàn toàn (không để placeholder) nếu file này chưa tồn tại.
- **Quotation** — từ team-composition.md + effort-breakdown.md: bảng "Vị trí | Effort (man-day) | Đơn giá | Thành tiền" — cột Đơn giá và Thành tiền để trống, ghi chú "Cần điền đơn giá theo thời điểm báo giá".

## Part 5: Appendix

Chỉ tạo 1 slide Header "Appendix" — nội dung chi tiết do người dùng tự bổ sung sau khi có phản hồi cụ thể từ khách hàng hoặc tài liệu bổ trợ khác.
