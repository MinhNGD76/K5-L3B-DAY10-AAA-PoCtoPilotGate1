# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): AAA
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-AAA-PoCtoPilotGate1` — https://github.com/MinhNGD76/K5-L3B-DAY10-AAA-PoCtoPilotGate1
- Thẻ sự cố đã bốc (S1–S8):
- Tài liệu Lab 9 dùng chung: [`docs/lab9/PRD_v1.1.md`](docs/lab9/PRD_v1.1.md) và [`docs/lab9/eval_card.md`](docs/lab9/eval_card.md), chép từ repo Lab 9 của Nguyễn Đình Minh (`K5-L3B-Day09-NguyenDinhMinh-2A202603898-EvaluationandFailureAnalysis`, commit `2a34aaf`; baseline `E-swarm-20261118-df3d`).

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

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

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.


## NguyenNhatMinh-2A202603745

### Phần việc phụ trách

Vận hành và pháp lý (N3 trong `PLAN.md`): người trực, trách nhiệm, dữ liệu cá nhân, runbook, bài nộp.

- Đề: câu 1.2, 1.4, 2.4, 2.7 (cùng N1), 2.10, 3.3, 3.4 và 3.7 (tổng hợp cùng N1).
- Phiếu A: A1 (câu 1.2), A2 (câu 1.4). Phiếu B: B4 HAZOP, B5 checklist 9 nhóm, B7.2, B7.5–B7.6, runbook 1–3. Phiếu C: điều phối, C3, C4, C6, C9–C11, runbook 4–5.
- File: người ghi cuối `config/operating_gates.json` (`operations`, `legal`, tích hợp `business`), `templates/form-c-incident.md`, `submission/submission.json`, `config/switches.json` (cùng N1).
- Kiểm chéo: phần kinh doanh/tiêu chí của N2.

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## PhamTheHung-2A202603778

### Phần việc phụ trách

Kỹ sư cổng, phụ trách cổng (N1 trong `PLAN.md`): `pre_guard`, `write_gate`, phân tích nguyên nhân kỹ thuật.

- Đề: câu 2.2 (cùng N4), 2.6, 2.7, 2.8 (cùng N4), 3.1 (cùng N4), 3.5.
- Phiếu B: B2, B4 (hỗ trợ), B7.1–B7.3. Phiếu C: C2, C4, C6, C7 (phần kỹ thuật), C9.
- File: `lab10/guards.py` (vòng 1 và vòng 2), `config/switches.json` (cùng N3); review `lab10/monitors.py`.
- Kiểm chéo: code monitor của N4.

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## NgoDuyKhanh-2A202603870

### Phần việc phụ trách

Kỹ sư cổng, phụ trách kiểm thử, dữ liệu và giám sát (N4 trong `PLAN.md`): giữ checkout tích hợp, chạy mọi lần đo chính.

- Đề: câu 1.3, 1.5 (cùng N2), 2.1, 2.2, 2.8, 3.0, 3.1, 3.6.
- Phiếu A: A2 (câu 1.3), A3, A5 (kiểm ký). Phiếu B: B0–B2, B7.3. Phiếu C: C0–C2, C8.
- File: `lab10/monitors.py` (monitor mới), `runs/journal.jsonl` (chỉ do lệnh sinh), các lệnh K0–K8; chạy `check_submission --collect`.
- Kiểm chéo: `lab10/guards.py` của N1.

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.