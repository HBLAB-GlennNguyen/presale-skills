# Gợi ý lựa chọn cho phần Technical Solution

Dùng khi hỏi tương tác người tạo proposal ở Part 2 (Technical Solution) — mỗi câu hỏi đưa ra các lựa chọn dưới đây kèm mô tả ngắn, luôn có thêm lựa chọn "Khác — tự mô tả" để người dùng ghi thông tin không khớp gợi ý.

## Cloud provider / hạ tầng

- **AWS** — hệ sinh thái rộng nhất, phù hợp đa số dự án web/mobile, nhiều dịch vụ managed (RDS, S3, Lambda, CloudFront...)
- **Azure** — phù hợp nếu khách hàng đã dùng hệ sinh thái Microsoft (Active Directory, Office 365, .NET stack)
- **Google Cloud Platform (GCP)** — mạnh về data/AI/ML, BigQuery, phù hợp dự án nặng về phân tích dữ liệu
- **On-premise / dedicated server** — khi khách hàng có ràng buộc dữ liệu không được rời khỏi hạ tầng nội bộ (ngân hàng, chính phủ...)
- **Hybrid (on-premise + cloud)** — khi có hệ thống cũ cần giữ lại on-premise nhưng mở rộng thêm trên cloud

## Kiến trúc hệ thống

- **Monolithic** — 1 codebase/deploy unit duy nhất, phù hợp dự án quy mô nhỏ-vừa, team nhỏ, cần triển khai nhanh
- **Modular monolith** — tách module rõ ràng trong cùng 1 deploy unit, dễ tách microservices sau này nếu cần, cân bằng tốc độ phát triển và khả năng mở rộng
- **Microservices** — tách nhiều service độc lập, phù hợp hệ thống lớn (dự án >100 màn hình, nhiều team song song), phức tạp vận hành hơn
- **Serverless** — dùng function-as-a-service (AWS Lambda, Azure Functions), phù hợp workload không đều, muốn tối ưu chi phí vận hành

## Gợi ý stack theo loại dự án (điểm khởi đầu, không bắt buộc)

| Loại dự án | Backend | Frontend | Database |
|---|---|---|---|
| Web app quản lý nội bộ (CRUD-heavy) | Node.js (NestJS) hoặc Java (Spring Boot) | React / Next.js | PostgreSQL / MySQL |
| Mobile app | Node.js/Java backend (API) | React Native / Flutter | PostgreSQL / MongoDB |
| Nền tảng dữ liệu/phân tích | Python (FastAPI) + pipeline (Airflow/Spark) | React + dashboard (vd Metabase/Superset nếu phù hợp) | PostgreSQL + Data warehouse (BigQuery/Redshift) |
| Hệ thống tích hợp nhiều bên thứ 3 | Node.js/Java + message queue (Kafka/RabbitMQ) | React / Next.js | PostgreSQL |

## Infrastructure services thường dùng theo cloud (ví dụ AWS)

- Compute: EC2, ECS/Fargate, Lambda
- Database: RDS (PostgreSQL/MySQL), DynamoDB
- Storage: S3
- CDN: CloudFront
- API layer: API Gateway
- Networking/bảo mật: VPC, IAM, WAF

(Azure/GCP có nhóm dịch vụ tương đương — liệt kê tương tự khi khách hàng chọn provider đó.)
