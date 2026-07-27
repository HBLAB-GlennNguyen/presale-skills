# Rubric buffer theo mức rủi ro

Áp dụng buffer (% cộng thêm) lên tổng effort bottom-up/PERT đã tính, dựa trên **mức rủi ro tổng thể** đọc từ `risk-assessment.md` (output của skill analyzing-rfp).

## Buffer theo mức rủi ro

`risk-assessment.md` kết luận mức rủi ro tổng thể theo ma trận Likelihood × Impact (4 mức). Buffer tương ứng:

| Mức rủi ro (từ risk-assessment.md) | Buffer |
|---|---|
| Rủi ro thấp | +10% |
| Rủi ro trung bình | +20% |
| Rủi ro cao | +35% |
| Rủi ro nghiêm trọng | +50% |

## Buffer bổ sung: tổ hợp Fixed Price + phạm vi chưa rõ

Nếu `risk-assessment.md` đã nêu bật tổ hợp **Fixed Price + rủi ro "Phạm vi bị hiểu sai/thay đổi giữa chừng" có Impact ≥ 4** (theo ghi chú trong rubric của analyzing-rfp), cộng thêm **+10%** vào buffer ở bảng trên — đây là tổ hợp rủi ro cao nhất cho vendor (cam kết giá cố định trên phạm vi chưa rõ), cần dự phòng thêm.

## Cách áp dụng

```
Tổng effort sau buffer = Tổng effort bottom-up/PERT × (1 + % buffer)
```

Nếu risk-assessment.md có mục chấm "?" (không đủ thông tin) ở Likelihood hoặc Impact, không tự nâng mức rủi ro lên — dùng đúng mức rủi ro tổng thể đã kết luận trong file, và nêu rõ trong effort-breakdown.md rằng buffer có thể cần điều chỉnh lại nếu các mục "?" được làm rõ sau này.
