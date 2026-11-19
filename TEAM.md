# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): AAA
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-AAA-PoCtoPilotGate1` — https://github.com/MinhNGD76/K5-L3B-DAY10-AAA-PoCtoPilotGate1
- Thẻ sự cố đã bốc (S1–S8): S5
- Tài liệu Lab 9 dùng chung: [`docs/lab9/PRD_v1.1.md`](docs/lab9/PRD_v1.1.md) và [`docs/lab9/eval_card.md`](docs/lab9/eval_card.md), chép từ repo Lab 9 của Nguyễn Đình Minh (`K5-L3B-Day09-NguyenDinhMinh-2A202603898-EvaluationandFailureAnalysis`, commit `2a34aaf`; baseline `E-swarm-20261118-df3d`).

## Thành viên

Họ tên đầy đủ và MSSV của mọi thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Nguyễn Đình Minh          | 2A202603898     | Sản phẩm và kinh doanh     | ✓             |
|   2 | Nguyễn Nhật Minh          | 2A202603745      | Vận hành và pháp lý    |             |
|   3 | Phạm Thế Hùng          | 2A202603778     | Kỹ sư cổng     |             |
|   4 | Ngô Duy Khánh          | 2A202603870      | Kỹ sư cổng     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenDinhMinh-2A202603898

### Phần việc phụ trách

Sản phẩm và kinh doanh, trưởng nhóm (N2 trong `PLAN.md`): điều phối quyết định và commit/push các mốc.

- Đề: câu 1.1, 1.5, 1.6, 2.3, 2.5 (tổng hợp), 2.9, 3.2; quyết định v1/v2 và ba dòng bắt buộc.
- Phiếu A: chủ trì A1–A5. Phiếu B: điều phối, viết B3, B6, B7.4, B8. Phiếu C: C3 (hỗ trợ), C5, C7 (phần kinh doanh), C12.
- File: `config/acceptance_criteria.json` (ký), mục `business` của `config/operating_gates.json`, `templates/form-a-criteria.md`, `templates/form-b-evaluation-gates.md`; duyệt `submission/submission.json`.
- Kiểm chéo: phần vận hành của N3.

### Đóng góp cụ thể

- Ký tiêu chí: lần ký 2026-11-19T15:55:23, hash `6e46a341…`, commit `386137a`, trước lần đo đầu tiên.
- Soạn Phiếu A (A1–A5) và `config/acceptance_criteria.json`: ngưỡng, hành động, ranh giới đầu ra, ngày xem lại 2026-11-30.
- Phiếu B: B3 bản đồ dữ liệu, B6 pre-mortem, B7.4 mục `business`, B8 quyết định v1 **Tiếp tục** (xác nhận 2026-11-19).
- Phiếu C: C5 specification và giả định môi trường; C12 quyết định v2 **Thu hẹp** (xác nhận 2026-11-19) và ba dòng bắt buộc.
- `submission/submission.json` (team, members, thẻ S5, v1/v2).

### Bằng chứng

- Commit ký: `386137a` "Sign acceptance criteria".
- Chốt vòng 1: hash `bf56420d`; `checkpoint verify` ok.
- Mã lần chạy chung của bàn (thẻ S5): base `R-S5-before-20261119-172437-319747`, prepared `R-S5-prepared-20261119-172437-319747`, after `R-S5-after-20261119-172437-319747`, tự kiểm tra `R-S5-grade-20261119-172436-319747`; bộ nền `R-base-before-20261119-161311-b45eeb`, `R-base-after-20261119-172232-319747`, `R-base-prepared-20261119-162921-381942`.
- Phiếu A A5; Phiếu B B8 cột v1; Phiếu C C12 cột v2 và ba dòng bắt buộc.

*Dùng AI:* Dùng trợ lý AI để soạn nháp phiếu, code và phân tích trace; các số đã được đối chiếu với report và trace trước khi ghi vào phiếu.

### Exit ticket

- Học được: ký tiêu chí và ngưỡng trước lần đo đầu tiên mới làm quyết định Tiếp tục/Thu hẹp có giá trị; nếu ký sau khi thấy số thì dễ chỉnh ngưỡng cho vừa kết quả.
- Còn chưa chắc: ngưỡng và ngày xem lại 2026-11-30 trong Phiếu A có đủ chặt khi lưu lượng thật tăng, vì mới kiểm trên bộ nền và gói S5.


## NguyenNhatMinh-2A202603745

### Phần việc phụ trách

Vận hành và pháp lý (N3 trong `PLAN.md`): người trực, trách nhiệm, dữ liệu cá nhân, runbook, bài nộp.

- Đề: câu 1.2, 1.4, 2.4, 2.7 (cùng N1), 2.10, 3.3, 3.4 và 3.7 (tổng hợp cùng N1).
- Phiếu A: A1 (câu 1.2), A2 (câu 1.4). Phiếu B: B4 HAZOP, B5 checklist 9 nhóm, B7.2, B7.5–B7.6, runbook 1–3. Phiếu C: điều phối, C3, C4, C6, C9–C11, runbook 4–5.
- File: người ghi cuối `config/operating_gates.json` (`operations`, `legal`, tích hợp `business`), `templates/form-c-incident.md`, `submission/submission.json`, `config/switches.json` (cùng N1).
- Kiểm chéo: phần kinh doanh/tiêu chí của N2.

### Đóng góp cụ thể

- Phiếu A: A1 (câu 1.2: chị Oanh, chị Hạnh), A2 (câu 1.4 telemetry).
- Phiếu B: B4 HAZOP vòng 1 (dòng ngoài kỹ thuật), B5 checklist 9 nhóm, B7.5 và B7.6 (PIC, ngưỡng, giờ cao điểm, runbook 1–3).
- `config/operating_gates.json` mục `operations` và `legal` (PIC NV-TUNG, người duyệt NV-HANH, 1 người trực, `pii_fields_blocked_to_third_party`, `carrier_fault_requires_recorded_cause`).
- Phiếu C: C3.5, C4 HAZOP của thẻ, C6 và C9 fault tree, C10 risk register (4 dòng), C11 checklist và runbook 4–5 (ba kịch bản).
- `submission/submission.json` đối chiếu với bài nộp (`check_submission --collect`: ĐỦ THÀNH PHẦN).

### Bằng chứng

- Mốc chốt vòng 1: `checkpoint` lúc 2026-11-19T16:29:20, hash `bf56420d`.
- Mã lần chạy chung của bàn (thẻ S5): base `R-S5-before-20261119-172437-319747`, prepared `R-S5-prepared-20261119-172437-319747`, after `R-S5-after-20261119-172437-319747`, tự kiểm tra `R-S5-grade-20261119-172436-319747`; bộ nền `R-base-before-20261119-161311-b45eeb`, `R-base-after-20261119-172232-319747`, `R-base-prepared-20261119-162921-381942`.
- Phiếu B B5 và B7.5–B7.6; Phiếu C C4, C6, C9, C10, C11.

*Dùng AI:* Dùng trợ lý AI để soạn nháp runbook và HAZOP; người này cần đọc lại và ghi phần mình đã sửa.

### Exit ticket

- Học được: lỗi ở phần vận hành/pháp lý (ai trực, ai duyệt, PII gửi hãng) cũng cần cổng và runbook cụ thể như lỗi kỹ thuật; HAZOP giúp tìm ra các dòng ngoài code.
- Còn chưa chắc: với chỉ 1 người trực, runbook 1–5 có đủ dùng vào giờ cao điểm hay không, vì chưa được diễn tập với sự cố thật.

## PhamTheHung-2A202603778

### Phần việc phụ trách

Kỹ sư cổng, phụ trách cổng (N1 trong `PLAN.md`): `pre_guard`, `write_gate`, phân tích nguyên nhân kỹ thuật.

- Đề: câu 2.2 (cùng N4), 2.6, 2.7, 2.8 (cùng N4), 3.1 (cùng N4), 3.5.
- Phiếu B: B2, B4 (hỗ trợ), B7.1–B7.3. Phiếu C: C2, C4, C6, C7 (phần kỹ thuật), C9.
- File: `lab10/guards.py` (vòng 1 và vòng 2), `config/switches.json` (cùng N3); review `lab10/monitors.py`.
- Kiểm chéo: code monitor của N4.

### Đóng góp cụ thể

- `lab10/guards.py` vòng 1: cổng sổ cái và cổng xác minh số ngày theo tracking, cổng 2 (fail_open), cổng 3 (thư gửi hãng bỏ PII).
- `lab10/guards.py` vòng 2: cổng hoàn phần còn lại theo sổ cái, cắt chữ dán kèm trong `pre_guard`, sự kiện `duplicate_refund`.
- Phiếu B: B2 bảng soát lỗi `T-002@55` (phần kỹ thuật), B7.1 cổng.
- Phiếu C: C2 bảng soát lỗi của thẻ (4 lỗi), C4 HAZOP (dòng `issue_refund`), C6 fault tree trước sửa, C7 bảng sửa nhánh [1] và [3], C9 fault tree sau sửa.
- `config/switches.json` (cùng N3) chưa đổi: bốn công tắc đều `on`.

### Bằng chứng

- Các cổng nằm trong `lab10/guards.py`; `R-base-after-20261119-172232-319747` không ca nền mới hỏng.
- `R-S5-after-20261119-172437-319747`: S5-21 hoàn 12.000đ, S5-02/03/05/20 chuyển người, 0đ.
- Phiếu C C2, C4, C6, C7, C9.

*Dùng AI:* Dùng trợ lý AI để viết code cổng và phân tích trace; các cổng đã được chạy lại trên bộ nền và gói S5 trước khi ghi nhận.

### Exit ticket

- Học được: cổng phải dựa trên sổ cái và dữ liệu có thật (hoàn phần còn lại, xác minh theo tracking) chứ không tin chữ trong ticket; vá một lỗi xong phải chạy lại bộ nền để chắc không làm hỏng ca khác.
- Còn chưa chắc: cắt chữ dán kèm trong `pre_guard` có bỏ sót cách diễn đạt khác của người dùng hay không, vì chỉ kiểm trên các ca đã biết.

## NgoDuyKhanh-2A202603870

### Phần việc phụ trách

Kỹ sư cổng, phụ trách kiểm thử, dữ liệu và giám sát (N4 trong `PLAN.md`): giữ checkout tích hợp, chạy mọi lần đo chính.

- Đề: câu 1.3, 1.5 (cùng N2), 2.1, 2.2, 2.8, 3.0, 3.1, 3.6.
- Phiếu A: A2 (câu 1.3), A3, A5 (kiểm ký). Phiếu B: B0–B2, B7.3. Phiếu C: C0–C2, C8.
- File: `lab10/monitors.py` (monitor mới), `runs/journal.jsonl` (chỉ do lệnh sinh), các lệnh K0–K8; chạy `check_submission --collect`.
- Kiểm chéo: `lab10/guards.py` của N1.

### Đóng góp cụ thể

- Chạy các lần đo chính trên checkout tích hợp: `R-base-before-…161311`, `R-base-after-…162351/162423/172232`, `R-base-prepared-…162921`, bộ thẻ S5.
- `lab10/monitors.py`: `cost_per_ticket_worst_warehouse` (chi phí mỗi ticket theo kho đắt nhất) và `duplicate_refund_attempts`.
- Phiếu A: A2 (câu 1.3, metric offline cho bước ghi lỗi hãng), A3, A5 kiểm ký.
- Phiếu B: B0 (nhật ký lần chạy), B1 (lần chạy đầu tiên), B2 (trace `T-002@55`), B7.3 (hai ticket hiểm).
- Phiếu C: C0 (nhật ký vòng 2), C1, C2, C8 (bảng ba ô cho chi phí mỗi ticket theo kho); chạy `check_submission --collect`.

### Bằng chứng

- Nhật ký: `runs/journal.jsonl` (ghi tự động từ `eval` và `grade`).
- Mã lần chạy chung của bàn (thẻ S5): base `R-S5-before-20261119-172437-319747`, prepared `R-S5-prepared-20261119-172437-319747`, after `R-S5-after-20261119-172437-319747`, tự kiểm tra `R-S5-grade-20261119-172436-319747`; bộ nền `R-base-before-20261119-161311-b45eeb`, `R-base-after-20261119-172232-319747`, `R-base-prepared-20261119-162921-381942`.
- Phiếu B B0 dòng 1–4; Phiếu C C0 dòng 1–4, C8.

*Dùng AI:* Dùng trợ lý AI để chạy lệnh và soạn nháp phiếu; số trong phiếu được lấy từ report và trace.

### Exit ticket

- Học được: một metric tổng (chi phí trung bình) che mất ca xấu; đo chi phí mỗi ticket theo kho đắt nhất và đếm `duplicate_refund_attempts` mới lộ ra rủi ro thật. Nhật ký do lệnh sinh ra giúp mọi số truy được về mã lần chạy.
- Còn chưa chắc: hai monitor mới có cảnh báo đủ sớm trên dữ liệu thật hay không, vì ngưỡng chỉ được đặt từ bộ nền và thẻ S5.