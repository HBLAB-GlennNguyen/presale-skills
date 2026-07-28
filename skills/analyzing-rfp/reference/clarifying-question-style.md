# Văn phong câu hỏi làm rõ gửi khách hàng

`clarifying-questions.md` gửi cho KHÁCH HÀNG, không phải nội bộ. Mỗi câu hỏi phải đọc như một tư vấn viên có kinh nghiệm (chuyên gia kỹ thuật hoặc business analyst) đang trao đổi, không phải một form thu thập dữ liệu. Không viết câu hỏi mở/blank kiểu "X là gì?" — luôn có: (1) bối cảnh/khuyến nghị ngắn dựa trên kinh nghiệm ngành hoặc thông tin đã biết về khách hàng, rồi (2) câu hỏi dạng Yes/No hoặc 2-4 lựa chọn để khách hàng chọn nhanh.

Không tự bịa số liệu cụ thể (giá tiền, benchmark hiệu năng chính xác) nếu không có cơ sở — khuyến nghị nên dựa trên loại hình khách hàng/ngành nghề/mô hình hợp tác đã biết, không phải số liệu tự chế. Nếu không đủ cơ sở để đưa khuyến nghị, vẫn nêu lý do cần hỏi (business rationale) thay vì hỏi trống không.

## Ví dụ chuyển đổi

**Trước (kiểu cũ — hỏi mở, thu thập dữ liệu):**
> Hệ thống cần đáp ứng yêu cầu hiệu năng cụ thể nào không?

**Sau (kiểu mới — có khuyến nghị, có lựa chọn):**
> Theo kinh nghiệm triển khai các hệ thống quản lý vận đơn quy mô tương tự, chúng tôi thường đề xuất mức đáp ứng đủ cho vài nghìn giao dịch/ngày với thời gian phản hồi dưới 2 giây là hợp lý cho giai đoạn đầu. Mức này có phù hợp với kỳ vọng của Quý khách không?
> - [ ] Phù hợp, áp dụng mức đề xuất
> - [ ] Cần mức cao hơn (Quý khách vui lòng cho biết quy mô ước tính)
> - [ ] Chưa rõ, cần trao đổi thêm với đội kỹ thuật của Quý khách

**Trước:**
> Dự án có cần tuân thủ quy định pháp lý/ngành logistics cụ thể nào không?

**Sau:**
> Với các doanh nghiệp logistics vận chuyển nội địa, thường không phát sinh yêu cầu tuân thủ đặc biệt ngoài quy định chung về bảo vệ dữ liệu cá nhân. Quý khách có yêu cầu tuân thủ bổ sung nào khác (ví dụ vận chuyển hàng đặc thù, xuất nhập khẩu) không?
> - [ ] Không có yêu cầu đặc biệt, áp dụng chuẩn chung về bảo vệ dữ liệu
> - [ ] Có, cần tuân thủ thêm (Quý khách vui lòng nêu rõ)

**Trước:**
> Ngân sách dự kiến cho dự án là bao nhiêu?

**Sau (tránh bịa số tiền — chuyển hướng sang mô hình hợp tác, nơi có cơ sở để khuyến nghị):**
> Ngân sách sẽ ảnh hưởng đến mô hình hợp tác phù hợp. Nếu ngân sách tổng thể chưa cố định, chúng tôi đề xuất bắt đầu theo mô hình Time & Material (T&M) để linh hoạt điều chỉnh phạm vi thay vì cam kết Fixed Price ngay từ đầu. Quý khách đã có ngân sách cố định cho dự án chưa?
> - [ ] Đã có ngân sách cố định (Quý khách vui lòng cho biết khoảng ngân sách)
> - [ ] Chưa cố định, ưu tiên mô hình linh hoạt (T&M)
> - [ ] Cần tư vấn thêm để chọn mô hình phù hợp

## Khi nào giữ câu hỏi mở

Chỉ giữ dạng mở khi bản chất câu trả lời không thể đóng khung hợp lý (ví dụ: tên đầu mối liên hệ kỹ thuật cụ thể). Ngay cả khi đó, vẫn nên có 1 câu dẫn ngắn thể hiện lý do cần thông tin, không hỏi trống không.

## Phân loại câu hỏi theo 3 nhóm

Mỗi câu hỏi viết theo văn phong ở trên còn phải được xếp vào đúng 1 trong 3 nhóm dưới đây khi ghi vào `clarifying-questions.md`. Nhóm quyết định góc nhìn/persona của câu dẫn (không đổi cấu trúc context → lựa chọn đã nêu ở trên).

| Field / chủ đề | Nhóm | Góc nhìn persona |
|---|---|---|
| Người ra quyết định, đầu mối liên hệ kỹ thuật (chỉ xác nhận đầu mối, không phải nội dung kỹ thuật), ngân sách, timeline (khởi động/go-live/mốc trung gian), mô hình hợp tác, các bên liên quan khác, các dòng trống trong bảng "Vai trò & trách nhiệm hai bên" | **A. Sale** | Sales/Account Manager — quan tâm cam kết, nguồn lực, thời gian, hợp đồng |
| Mô tả phạm vi còn mơ hồ, các hạng mục ngoài phạm vi, đối tượng nghiệp vụ/vòng đời chưa rõ, đối tượng sử dụng & nhiệm vụ chưa rõ, workflow/luồng nghiệp vụ chưa rõ, tiêu chí thành công | **B. Domain/BA** | Business Analyst/Consultant — quan tâm logic nghiệp vụ, quy trình, người dùng |
| Stack công nghệ hiện tại, hệ thống cần tích hợp, yêu cầu công nghệ cụ thể, hiệu năng, bảo mật, tuân thủ / quy định (compliance), khả năng mở rộng | **C. Technical** | Technical Lead/Consultant — quan tâm ràng buộc kỹ thuật, khả thi triển khai |
