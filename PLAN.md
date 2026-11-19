# Kế hoạch toàn dự án LAB 10 — nhóm 4 người

Phạm vi: hoàn thành repo LAB 10 từ chuẩn bị, ký tiêu chí, dựng cổng vòng 1,
xử lý thẻ sự cố, quyết định Gate 1 v2 đến demo và nộp bài. Thời lượng theo đề:
240 phút. M0 đã được đánh dấu hoàn thành theo cập nhật của nhóm; các bước ký,
đánh giá, chốt hoặc nộp bài giữ trạng thái ở checklist bên dưới.

**Cách dùng:** người phụ trách từng task đã ghi bằng tên thật, khớp `TEAM.md`. Chỉ đổi `- [ ]` thành
`- [x]` sau khi đạt điều kiện kiểm tra của task. Ghi bằng chứng sau task theo
dạng `commit: …; run: …; mục phiếu: …`. Việc không áp dụng phải ghi rõ lý do.
Các ngưỡng, tên người chịu trách nhiệm và quyết định do cả nhóm thống nhất.
M1–M4 trong bảng phân công là mã thành viên; M0–M8 trong checklist là các mốc
công việc. Mỗi task ghi tên người nhận và liên kết tới file cần làm; file được
bảo vệ được ghi rõ là tài liệu chỉ đọc.

## 1. Hiện trạng và việc ưu tiên

- [x] Đã khảo sát cấu trúc, quy định sửa file và yêu cầu bài nộp.
- [x] Đã tạo `AGENTS.md` hướng dẫn làm việc trong repo.
- [x] Đã chạy bộ kiểm tra công khai ở bước `/init`: 13 tests, `OK`.
- [x] Đã lập checklist, phân công 4 người, danh sách file và cách kiểm tra trong file này.

Phần chuẩn bị, quyền repo, danh tính Git, checkout LF và phân vai được theo dõi
tại M0 đã hoàn thành theo cập nhật của nhóm. Mục cá nhân trong
[TEAM.md](TEAM.md) tiếp tục hoàn thiện tại M7.5; tiêu chí và tài liệu Lab 9 được
đối chiếu ở M1.

Các phần bài lab còn ở trạng thái ban đầu: tiêu chí chưa điền/chưa ký, hai hàm
guard đang cho qua, monitor chỉ có bản mẫu, chưa có checkpoint vòng 1 và thẻ sự
cố, metadata bài nộp chưa điền. Chưa đánh dấu hoàn thành các phần này.

## 2. Phân công 4 người

| Mã | Người | Vai và trách nhiệm chính | File cần làm | Người kiểm tra chéo |
|---|---|---|---|---|
| **M1** | **Phạm Thế Hùng** | Kỹ sư cổng: `pre_guard`, `write_gate`, nguyên nhân kỹ thuật, sửa vòng 1/vòng 2 | [guards.py](lab10/guards.py), [Phiếu B — B2/B7](templates/form-b-evaluation-gates.md#b2), [Phiếu C — C2/C6/C7](templates/form-c-incident.md#c2) | Ngô Duy Khánh |
| **M2** | **Nguyễn Đình Minh** | Trưởng nhóm; sản phẩm, tiêu chí, kinh doanh, ngân sách/ROI/phạm vi, quyết định v1/v2 và commit mốc | [TEAM.md](TEAM.md), [tiêu chí](config/acceptance_criteria.json), [Phiếu A](templates/form-a-criteria.md), [Phiếu B — B8](templates/form-b-evaluation-gates.md#b8), [Phiếu C — C12](templates/form-c-incident.md#c12) | Nguyễn Nhật Minh kiểm vận hành; Ngô Duy Khánh kiểm số liệu |
| **M3** | **Nguyễn Nhật Minh** | Vận hành/pháp lý: HAZOP, PIC, nhân sự/hàng chờ, PII, runbook, rủi ro, metadata nộp | [cổng vận hành](config/operating_gates.json), [Phiếu B — B4/B5/B7](templates/form-b-evaluation-gates.md#b4), [Phiếu C](templates/form-c-incident.md), [submission.json](submission/submission.json) | Nguyễn Đình Minh |
| **M4** | **Ngô Duy Khánh** | Kiểm thử, dữ liệu/giám sát: test/eval/trace/grade, nhật ký run, monitor, kiểm bộ nộp | [monitors.py](lab10/monitors.py), [Phiếu A — A2](templates/form-a-criteria.md#a2), [Phiếu B — B0/B1](templates/form-b-evaluation-gates.md#b0), [Phiếu C — C0/C8](templates/form-c-incident.md#c0) | Phạm Thế Hùng kiểm code; Nguyễn Nhật Minh kiểm tình huống vận hành |

**Quy tắc phối hợp:** Nguyễn Nhật Minh là người ghi cuối vào `config/operating_gates.json`;
Nguyễn Đình Minh cung cấp mục `business`, Nguyễn Nhật Minh điền `operations`/`legal`. Các phiếu chia theo
mục, tránh hai người ghi cùng mục. Ngô Duy Khánh dùng một checkout tích hợp để chạy các
lần đo chính và gom bài, giữ đầy đủ `runs/journal.jsonl`; không ghép hoặc sửa
tay lịch sử các lần chạy. Nguyễn Đình Minh điều phối commit/push các mốc. Mỗi người tự viết
mục cá nhân trong `TEAM.md` và tự nộp link LMS.

## 3. File cần sửa và cách kiểm tra

| File nguồn | Người sửa | Nội dung | Kiểm tra |
|---|---|---|---|
| `TEAM.md` | Nguyễn Đình Minh + từng người | Tên nhóm/lớp/repo, bảng đủ 4 người, 4 mục cá nhân | Họ tên/MSSV/vai đầy đủ; `members` khớp; từng người ghi đóng góp và dùng AI |
| `config/acceptance_criteria.json` | Nguyễn Đình Minh, cả nhóm duyệt | `team`, `signed_by`, các ngưỡng, `stop_condition`, 4 `decision_rule` | Đủ trường theo Phiếu A; JSON hợp lệ; ký trước đánh giá; sau ký chạy `criteria verify` |
| `templates/form-a-criteria.md` | Nguyễn Đình Minh chủ trì, Nguyễn Nhật Minh/Ngô Duy Khánh bổ sung | A1–A5, câu 1.1–1.6 | Có mục tiêu, dữ liệu/công thức, CI, tiêu chí và bằng chứng ký/push |
| `lab10/guards.py` | Phạm Thế Hùng | 2–3 cổng vòng 1; sửa thêm đúng nguyên nhân ở vòng 2 | Public tests, trace, adhoc, eval và `regression` trong grade |
| `config/operating_gates.json` | Nguyễn Nhật Minh tích hợp; Nguyễn Đình Minh phụ trách business | Trần tiền/chi phí/ROI/phạm vi, PIC/duyệt/nhân sự/SLA, PII/pháp lý | JSON hợp lệ; số có lý do từ `ops_limits`/`ops_facts`; report và runbook khớp |
| `templates/form-b-evaluation-gates.md` | Nguyễn Đình Minh điều phối cả nhóm | B0–B8, câu 2.1–2.10, runbook 1–3, quyết định v1 | Đủ mục, có run ID/trace; HAZOP và checklist đủ; cột v1 được chốt trước sự cố |
| `lab10/monitors.py` | Ngô Duy Khánh, Phạm Thế Hùng review | Ít nhất một hàm mới và đăng ký vào `MONITORS` | Nhận trial không nhãn, trả số, không lỗi; `monitor ✅`; giải thích chênh lệch nền/sự cố |
| `templates/form-c-incident.md` | Nguyễn Nhật Minh điều phối cả nhóm | Thẻ, C0–C12, câu 3.0–3.7, quyết định v2 | Phân tích đúng thẻ; ≥2 lỗi khác nguồn, có lỗi chìm; cây lỗi có bằng chứng; đủ ba dòng cuối |
| `submission/submission.json` | Nguyễn Nhật Minh, Nguyễn Đình Minh duyệt | Team/members/incident/decisions/three_lines | Khớp TEAM, tiêu chí, B8, C12; `check_submission --collect` đủ thành phần |
| `config/switches.json` | Phạm Thế Hùng + Nguyễn Nhật Minh, khi cần | Công tắc 4 tool theo điều kiện dừng/runbook | Trace chứng minh tool tắt không ghi; trạng thái cuối đúng quyết định và bộ nộp |
| `PLAN.md` | Cả nhóm | Tick tiến độ và ghi bằng chứng | Task có người nhận, đầu ra và bằng chứng; không tick theo dự kiến |

**File chỉ đọc:** mọi file trong `lab10/MANIFEST.json`, đặc biệt `lab10/agent.py`,
`tools.py`, `helpers.py`, `eval.py`, `grade.py`, `tests/test_public.py`, `data/*`,
và gói `incidents/Sx/*`. Không sửa test, dữ liệu hay hash để làm báo cáo xanh.

**File tự sinh:** `config/acceptance_criteria.lock` do lệnh ký;
`lab10/guards_round1.py`, `config/operating_gates.round1.json`, `config/round1.lock`
do checkpoint; `runs/*` do eval/grade; các bản chép dưới `submission/code/`,
`submission/config/`, `submission/docs/`, `submission/runs/` và
`submission/manifest.json` do collect. Không điền tay các bản chép này. Không sửa
tiêu chí đã ký hoặc bản chốt vòng 1, kể cả khoảng trắng.

## 4. Checklist theo mốc

### M0 — Cài đặt và phân vai · phút 0–15

**Trạng thái:** đã tích toàn bộ M0 theo cập nhật của nhóm.

- [x] **M0.1 · Nguyễn Đình Minh:** xác nhận repo của nhóm là fork Public, tên đúng mẫu,
  `origin` đúng repo nhóm; mọi người có quyền làm việc. Kiểm bằng trang GitHub
  và `git remote -v`; không push/PR về repo mẫu.
  **File:** [TEAM.md](TEAM.md) · **Tham khảo (chỉ đọc):** [README.md](README.md), [SUBMISSION.md](SUBMISSION.md).
- [x] **M0.2 · Nguyễn Đình Minh:** cấu hình danh tính Git theo hướng dẫn lab: MSSV trưởng
  nhóm và email giả `<MSSV>@example.com`. Kiểm `git config user.name` và
  `git config user.email` tại checkout tích hợp.
  **Tham khảo (chỉ đọc):** [README.md](README.md).
- [x] **M0.3 · Ngô Duy Khánh:** hoàn tất checkout LF; chạy **K0** ở mục 5 và kiểm tra hash
  các file bảo vệ hiện có so với manifest. Điều kiện: 13 tests OK và hết lệch
  hash do CRLF. Kiểm tra này không chạy eval trước khi ký.
  **Tham khảo (chỉ đọc):** [guide.md](docs/guide.md), [test_public.py](tests/test_public.py), [MANIFEST.json](lab10/MANIFEST.json).
- [x] **M0.4 · Cả 4 người:** điền `TEAM.md`, nhận vai, chọn chung tài liệu Lab 9.
  Kiểm đủ 4 người, một trưởng nhóm và phân công từng mục phiếu.
  **File:** [TEAM.md](TEAM.md) · **Tham khảo (chỉ đọc):** [README.md](README.md).

### M1 — Tiêu chí và ký · phút 15–65

- [ ] **M1.1 · Nguyễn Đình Minh:** Phiếu A/A1 câu **1.1**: một mục tiêu cấp hệ thống;
  **Nguyễn Nhật Minh** câu **1.2**: mục tiêu từ hai bên liên quan. Kiểm mục tiêu có tác động
  cụ thể và phân biệt với việc model trả lời đúng.
  **File:** [form-a-criteria.md - A1](templates/form-a-criteria.md#a1).
- [ ] **M1.2 · Ngô Duy Khánh:** Phiếu A/A2 câu **1.3**: metric offline cho một bước;
  **Nguyễn Nhật Minh** câu **1.4**: telemetry production. Kiểm đủ thước đo, nguồn dữ liệu,
  công thức/mẫu số, xử lý thiếu dữ liệu, điểm mù; telemetry không cần nhãn đúng/sai.
  **File:** [form-a-criteria.md - A2](templates/form-a-criteria.md#a2).
- [ ] **M1.3 · Nguyễn Đình Minh + Ngô Duy Khánh:** Phiếu A/A3 câu **1.5**: đọc khoảng tin cậy từ số
  minh họa trong đề. Kiểm kết luận đúng phạm vi bằng chứng, hiểu
  `pass_rate`, `pass^k` và `pass@k`; chưa chạy trợ lý để chọn ngưỡng.
  **File:** [form-a-criteria.md - A3](templates/form-a-criteria.md#a3) · **Tham khảo (chỉ đọc):** [problem-set.md](problem-set.md).
- [ ] **M1.4 · Nguyễn Đình Minh, cả nhóm duyệt:** Phiếu A/A4 câu **1.6** và
  `acceptance_criteria.json`: đủ `required`, `nice_to_have`, `business_ops`,
  `stop_condition`, bốn `decision_rule`, `team`, `signed_by`. Kiểm mỗi ngưỡng
  có lý do của nhóm, có câu “Nếu… thì…”, thử hai phiên bản cho tiêu chí còn
  tranh luận, đủ bốn câu soát và hai câu ranh giới đầu ra; không chép ngưỡng mẫu.
  **File:** [acceptance_criteria.json](config/acceptance_criteria.json), [form-a-criteria.md - A4](templates/form-a-criteria.md#a4).
- [ ] **M1.5 · Nguyễn Đình Minh:** khi cả nhóm đã chốt, chạy **K1**, commit đúng message
  `Sign acceptance criteria` và push ngay. **Ngô Duy Khánh** kiểm `criteria verify`,
  commit trên GitHub và Phiếu A/A5 có thời điểm/mã commit. Từ đây khóa tiêu chí.
  **File:** [form-a-criteria.md - A5](templates/form-a-criteria.md#a5), [acceptance_criteria.json](config/acceptance_criteria.json).

**Điều kiện sang M2:** ký + commit + push xong trước lần đo đầu tiên. Không dùng
`--allow-unsigned` hoặc gọi hàm evaluator để lấy kết quả trước mốc này.

### M2 — Đo nền và tìm rủi ro · phút 65–85

- [ ] **M2.1 · Ngô Duy Khánh:** chạy **K2** khi chưa sửa guard/config vận hành. Điền
  Phiếu B/B0–B1, câu **2.1**: run ID nền, đối chiếu tiêu chí, chi phí/ROI,
  hàng chờ, phân khúc kho/hãng. Kiểm số được chép từ report thật.
  **File:** [form-b-evaluation-gates.md - B0](templates/form-b-evaluation-gates.md#b0), [form-b-evaluation-gates.md - B1](templates/form-b-evaluation-gates.md#b1).
- [ ] **M2.2 · Phạm Thế Hùng + Ngô Duy Khánh:** chạy **K3**, Phiếu B/B2 câu **2.2**: phân loại lỗi
  `T-002@55`, chỉ ra bước sai đầu tiên và nguồn dữ liệu. Kiểm có ticket@seed
  và dòng trace, phân biệt nguyên nhân với biểu hiện.
  **File:** [form-b-evaluation-gates.md - B2](templates/form-b-evaluation-gates.md#b2) · **Tham khảo (chỉ đọc):** [agent.py](lab10/agent.py), [helpers.py](lab10/helpers.py).
- [ ] **M2.3 · Nguyễn Đình Minh + Ngô Duy Khánh:** Phiếu B/B3 câu **2.3**: bản đồ nguồn sự thật/bản sao,
  nhãn, chuyển dịch dữ liệu và một ví dụ drift. Kiểm mỗi trường liên hệ được
  với dữ liệu/luồng trong repo.
  **File:** [form-b-evaluation-gates.md - B3](templates/form-b-evaluation-gates.md#b3) · **Tham khảo (chỉ đọc):** [world.json](data/world.json).
- [ ] **M2.4 · Nguyễn Nhật Minh, Phạm Thế Hùng hỗ trợ:** Phiếu B/B4 câu **2.4**: HAZOP trên một tool,
  ≥3 dòng kỹ thuật, trong đó ≥1 nhánh chưa thấy trên trace; thêm ≥2 dòng ngoài
  kỹ thuật. Kiểm từng dòng có lệch cụ thể, tác hại, bên chịu và cổng/tầng đề xuất.
  **File:** [form-b-evaluation-gates.md - B4](templates/form-b-evaluation-gates.md#b4).
- [ ] **M2.5 · Nguyễn Nhật Minh:** Phiếu B/B5: checklist đủ 9 nhóm việc, mỗi dòng có một
  PIC có tên, trạng thái và bằng chứng/việc còn thiếu; không ghi “cả nhóm” làm PIC.
  **File:** [form-b-evaluation-gates.md - B5](templates/form-b-evaluation-gates.md#b5).
- [ ] **M2.6 · Cả nhóm, Nguyễn Đình Minh tổng hợp:** Phiếu B/B6 câu **2.5**: pre-mortem
  đủ bốn lăng kính, chọn 2–3 lý do để dựng cổng. Kiểm từng cổng dự kiến truy
  ngược được về HAZOP/pre-mortem, hoàn thành trước khi biết thẻ.
  **File:** [form-b-evaluation-gates.md - B6](templates/form-b-evaluation-gates.md#b6).

### M3 — Cổng vòng 1 · phút 85–105

- [ ] **M3.1 · Phạm Thế Hùng:** câu **2.6**, `guards.py` và B7.1: dựng 2–3 cổng dựa trên
  dữ kiện từ `ctx.tools`, helper và chính sách có hiệu lực tại `ctx.as_of`.
  Ngô Duy Khánh kiểm trace trước/sau, **K0/K4**, không phát sinh ca nền mới hỏng.
  **File:** [guards.py](lab10/guards.py), [form-b-evaluation-gates.md - B7](templates/form-b-evaluation-gates.md#b7) · **Tham khảo (chỉ đọc):** [helpers.py](lab10/helpers.py).
- [ ] **M3.2 · Phạm Thế Hùng + Nguyễn Nhật Minh:** câu **2.7**, B7.2: ghi hai bước tránh lộ PII;
  đối chiếu nơi đọc dữ liệu và payload gửi bên thứ ba. Kiểm bằng trace/payload,
  nêu ranh giới mà cổng thực sự kiểm soát.
  **File:** [guards.py](lab10/guards.py), [operating_gates.json](config/operating_gates.json), [form-b-evaluation-gates.md - B7](templates/form-b-evaluation-gates.md#b7).
- [ ] **M3.3 · Ngô Duy Khánh + Phạm Thế Hùng:** câu **2.8**, B7.3: một tính chất cần giữ và hai
  ticket hiểm dùng `--adhoc`. Kiểm **K4**, sổ cái, lỗi hãng và tin nhắn khách;
  adhoc không có nhãn nên phải tự đối chiếu với dữ liệu nguồn.
  **File:** [form-b-evaluation-gates.md - B7](templates/form-b-evaluation-gates.md#b7).
- [ ] **M3.4 · Nguyễn Đình Minh → Nguyễn Nhật Minh tích hợp:** câu **2.9**, B7.4: mục `business` có
  trần hoàn/ngân sách/phạm vi/ROI. Kiểm từng số có lý do từ `data/world.json`
  mục `ops_limits`, `ops_facts`; phân biệt với ngưỡng chấp nhận đã ký.
  **File:** [operating_gates.json](config/operating_gates.json), [form-b-evaluation-gates.md - B7](templates/form-b-evaluation-gates.md#b7) · **Tham khảo (chỉ đọc):** [world.json](data/world.json).
- [ ] **M3.5 · Nguyễn Nhật Minh:** câu **2.10**, B7.5–B7.6: mục `operations`, `legal`,
  runbook phần 1–3 và **Giờ cao điểm**. Kiểm PIC/người duyệt có tên, số người,
  năng lực xử lý, SLA, kênh báo/điều kiện dừng khớp config và có cách xử lý quá tải.
  **File:** [operating_gates.json](config/operating_gates.json), [form-b-evaluation-gates.md - B7](templates/form-b-evaluation-gates.md#b7).
- [ ] **M3.6 · Ngô Duy Khánh, Phạm Thế Hùng/Nguyễn Nhật Minh sửa phần mình:** chạy **K0/K4**, ghi run ID vào B0.
  Kiểm không có ca nền mới hỏng; đọc cả phủ pilot, chi phí, ROI, hàng chờ và
  pháp lý. Cấm chặn hết, phạm vi 0 hoặc tăng nhân sự vô lý để đạt số.
  **File:** [form-b-evaluation-gates.md - B0](templates/form-b-evaluation-gates.md#b0), [guards.py](lab10/guards.py), [operating_gates.json](config/operating_gates.json) · **Tham khảo (chỉ đọc):** [test_public.py](tests/test_public.py).

### M4 — Chốt vòng 1 và quyết định v1 · phút 105–115

- [ ] **M4.1 · Nguyễn Đình Minh điều phối, Ngô Duy Khánh chạy:** khi vòng 1 hoàn tất, chạy **K5**
  đúng một lần. Kiểm có đủ hai bản chụp và `config/round1.lock`, lưu hash chốt.
  **File:** [form-b-evaluation-gates.md - B8](templates/form-b-evaluation-gates.md#b8) · **Tham khảo (chỉ đọc):** [guards.py](lab10/guards.py), [operating_gates.json](config/operating_gates.json).
- [ ] **M4.2 · Nguyễn Đình Minh + cả nhóm:** B8: quyết định v1, ≥3 bằng chứng có run ID,
  dòng `decision_rule`, kho/hãng xấu nhất, điều còn thiếu, PIC và ngày xem lại
  nếu cần. Kiểm quyết định khớp tiêu chí và report prepared.
  **File:** [form-b-evaluation-gates.md - B8](templates/form-b-evaluation-gates.md#b8) · **Tham khảo (chỉ đọc):** [acceptance_criteria.json](config/acceptance_criteria.json).
- [ ] **M4.3 · Nguyễn Đình Minh:** commit/push toàn bộ mốc vòng 1 theo B8. Ngô Duy Khánh kiểm các file
  chốt đã lên repo, cả nhóm đồng bộ. Từ đây không sửa snapshots, lock và cột v1.
  **File:** [form-b-evaluation-gates.md - B8](templates/form-b-evaluation-gates.md#b8), [guards.py](lab10/guards.py), [operating_gates.json](config/operating_gates.json).

**Phút 115–125:** nghỉ. Không tìm hoặc mở thẻ chưa được giao.

### M5 — Nhận thẻ và phân tích trước sửa · phút 125–155

- [ ] **M5.1 · Nguyễn Đình Minh + Nguyễn Nhật Minh:** lấy đúng `incidents/Sx/` theo `incidents/README.md`,
  commit/push; ghi số thẻ trong TEAM và dòng “Thẻ đã bốc:” của Phiếu C.
  Kiểm đủ 4 file và không đọc thẻ khác. Thay `Sx` bằng mã Coach giao.
  **File:** [TEAM.md](TEAM.md), [form-c-incident.md](templates/form-c-incident.md) · **Tham khảo (chỉ đọc):** [README.md](incidents/README.md).
- [ ] **M5.2 · Ngô Duy Khánh:** câu **3.0**, chạy **K6 trước mọi sửa chữa vòng 2**.
  Điền C0–C1: ba mốc, phần prepared đỡ được/bỏ sót, dòng vượt trần, đối chiếu
  B6. Kiểm `integrity ✅`; chưa nhận đủ thẻ thì không tự tạo dữ liệu thay thế.
  **File:** [form-c-incident.md - C0](templates/form-c-incident.md#c0), [form-c-incident.md - C1](templates/form-c-incident.md#c1) · **Tham khảo (chỉ đọc):** [form-b-evaluation-gates.md - B6](templates/form-b-evaluation-gates.md#b6).
- [ ] **M5.3 · Phạm Thế Hùng + Ngô Duy Khánh:** câu **3.1**, trace ≥2 ticket hỏng khác kiểu;
  C2 có ≥2 lỗi khác nguồn và ≥1 lỗi chìm, tác hại cho ai/đo bằng gì/số nền.
  Kiểm từng kết luận có ticket@seed và bằng chứng trace/report.
  **File:** [form-c-incident.md - C2](templates/form-c-incident.md#c2).
- [ ] **M5.4 · Nguyễn Nhật Minh, Nguyễn Đình Minh hỗ trợ:** điền phần riêng theo thẻ tại C3;
  trường hợp S4 theo đề không cần C3. Kiểm chỉ làm phần được chỉ định trên thẻ,
  không điền lần lượt tất cả các thẻ.
  **File:** [form-c-incident.md - C3](templates/form-c-incident.md#c3).
- [ ] **M5.5 · Nguyễn Nhật Minh + Phạm Thế Hùng:** C4, HAZOP sự cố ≥3 dòng dựa trên dữ kiện thẻ.
  Kiểm đây là bảng riêng, không ghi đè HAZOP vòng 1 tại B4.
  **File:** [form-c-incident.md - C4](templates/form-c-incident.md#c4) · **Tham khảo (chỉ đọc):** [form-b-evaluation-gates.md - B4](templates/form-b-evaluation-gates.md#b4).
- [ ] **M5.6 · Nguyễn Đình Minh:** câu **3.2**, C5: một specification có thể kiểm bằng code
  hoặc số liệu; **Nguyễn Nhật Minh** câu **3.3**: một giả định môi trường có thể sai.
  Kiểm phân biệt yêu cầu hệ thống với điều kiện môi trường.
  **File:** [form-c-incident.md - C5](templates/form-c-incident.md#c5).
- [ ] **M5.7 · Cả nhóm, Phạm Thế Hùng/Nguyễn Nhật Minh tổng hợp:** câu **3.4**, C6: fault tree trước
  sửa có ≥2 nhánh ở hai tầng khác nhau; mỗi lá có ticket@seed, trường dữ liệu
  hoặc dòng report. Kiểm có nguyên nhân ngoài model/code.
  **File:** [form-c-incident.md - C6](templates/form-c-incident.md#c6).

### M6 — Sửa vòng 2 và kiểm hồi quy · phút 155–185

- [ ] **M6.1 · Phạm Thế Hùng:** câu **3.5**, sửa `guards.py` theo nhánh nguyên nhân
  kỹ thuật, giữ cổng vòng 1 còn cần thiết; ghi C7. Kiểm cổng tổng quát, không
  nhánh riêng theo ID/seed/câu chữ, không sửa file được bảo vệ.
  **File:** [guards.py](lab10/guards.py), [form-c-incident.md - C7](templates/form-c-incident.md#c7).
- [ ] **M6.2 · Nguyễn Đình Minh → Nguyễn Nhật Minh tích hợp:** sửa business/operations/legal theo nhánh
  tiền, phạm vi, nhân sự, lòng tin hoặc pháp lý; ghi C7. Kiểm số có căn cứ,
  phạm vi >0, ticket ngoài phạm vi có nơi xử lý và chi phí nhân sự hợp lý.
  **File:** [operating_gates.json](config/operating_gates.json), [form-c-incident.md - C7](templates/form-c-incident.md#c7).
- [ ] **M6.3 · Ngô Duy Khánh, Phạm Thế Hùng review:** câu **3.6**, thêm ≥1 monitor mới trong
  `monitors.py`, đăng ký `MONITORS`, điền C8 đủ thước đo → dữ liệu → cách tính.
  Kiểm không dùng nhãn/pass-fail, kết quả là số, giải thích vì sao báo động.
  **File:** [monitors.py](lab10/monitors.py), [form-c-incident.md - C8](templates/form-c-incident.md#c8).
- [ ] **M6.4 · Ngô Duy Khánh:** chạy **K7**, mỗi lượt ghi rõ thay đổi trong `--note`;
  Phạm Thế Hùng/Nguyễn Đình Minh/Nguyễn Nhật Minh sửa theo báo cáo rồi kiểm lại. Mục tiêu kỹ thuật: public tests OK,
  `integrity`, `criteria`, `visible`, `regression`, `monitor` đạt mục tương ứng.
  Chỉ tick việc kiểm tra khi đã ghi kết quả thật và xử lý hoặc chuyển rõ phần
  còn chưa đạt sang rủi ro/quyết định v2; không coi việc ghi nhận là đã sửa xong.
  Ghi rõ test ẩn chưa được chạy, không tuyên bố đã qua test ẩn.
  **File:** [form-c-incident.md - C0](templates/form-c-incident.md#c0), [guards.py](lab10/guards.py), [operating_gates.json](config/operating_gates.json), [monitors.py](lab10/monitors.py) · **Tham khảo (chỉ đọc):** [test_public.py](tests/test_public.py).
- [ ] **M6.5 · Nguyễn Nhật Minh + Phạm Thế Hùng:** câu **3.7**, C9: fault tree sau sửa, gắn từng cổng
  vào nhánh và nêu nhánh còn hở; C10 có ≥1 dòng risk register với chủ sở hữu,
  biện pháp, hạn và rủi ro còn lại. Kiểm liên hệ trực tiếp với C6/C7/report.
  **File:** [form-c-incident.md - C9](templates/form-c-incident.md#c9), [form-c-incident.md - C10](templates/form-c-incident.md#c10).
- [ ] **M6.6 · Nguyễn Nhật Minh:** C11 cập nhật checklist 9 nhóm và runbook phần 4–5;
  kiểm có ba kịch bản “nếu… thì…”, điều kiện dừng/khôi phục, PIC và con số
  khớp cấu hình v2. Nếu dùng kill switch, Phạm Thế Hùng cùng kiểm bằng trace.
  **File:** [form-c-incident.md - C11](templates/form-c-incident.md#c11), [operating_gates.json](config/operating_gates.json), [switches.json](config/switches.json) · **Tham khảo (chỉ đọc):** [form-b-evaluation-gates.md - B5](templates/form-b-evaluation-gates.md#b5).

### M7 — Quyết định v2 và gom bài · phút 185–200

- [ ] **M7.1 · Nguyễn Đình Minh + cả nhóm:** C12 có quyết định v2, đổi/giữ so với v1 vì
  số nào, ≥3 bằng chứng, run ID thẻ ở ba mốc, phân khúc xấu nhất, dòng
  decision_rule, PIC/ngày xem lại và phần “Chỉ ở v2”. Kiểm không sửa B8/v1.
  **File:** [form-c-incident.md - C12](templates/form-c-incident.md#c12) · **Tham khảo (chỉ đọc):** [form-b-evaluation-gates.md - B8](templates/form-b-evaluation-gates.md#b8), [acceptance_criteria.json](config/acceptance_criteria.json).
- [ ] **M7.2 · Nguyễn Đình Minh + Nguyễn Nhật Minh:** hoàn thành ba dòng bắt buộc C12: giả định môi trường;
  GIẢM hay NGĂN tác hại và vì sao; cần đo lại gì trong pilot thật. Kiểm gắn với
  thiết kế và số liệu của nhóm, không viết nhận xét chung.
  **File:** [form-c-incident.md - C12](templates/form-c-incident.md#c12), [submission.json](submission/submission.json).
- [ ] **M7.3 · Nguyễn Nhật Minh:** điền `submission/submission.json`; kiểm `team` khớp tiêu
  chí/tên repo, đủ 4 `members` dạng `HoVaTen-MSSV`, đúng thẻ, đúng v1/v2;
  `three_lines` chép đúng ba câu ở C12.
  **File:** [submission.json](submission/submission.json) · **Tham khảo (chỉ đọc):** [TEAM.md](TEAM.md), [form-c-incident.md - C12](templates/form-c-incident.md#c12), [acceptance_criteria.json](config/acceptance_criteria.json).
- [ ] **M7.4 · Ngô Duy Khánh:** chạy **K8**, sửa nguồn theo từng dòng `[THIẾU]`, gom lại.
  Kiểm dòng cuối `ĐỦ THÀNH PHẦN`, đủ report ba mốc và journal; ba phiếu không
  còn mục bắt buộc nguyên mẫu. Đây là kiểm đủ thành phần, chưa phải kết quả chấm.
  **File:** [submission.json](submission/submission.json), [form-a-criteria.md](templates/form-a-criteria.md), [form-b-evaluation-gates.md](templates/form-b-evaluation-gates.md), [form-c-incident.md](templates/form-c-incident.md) · **Tham khảo (chỉ đọc):** [README.md](submission/README.md).
- [ ] **M7.5 · Từng người:** tự viết mục cá nhân trong `TEAM.md`, có công việc,
  đóng góp, bằng chứng, exit ticket và ghi dùng AI cho phần nào. Nguyễn Đình Minh kiểm đủ bốn mục.
  **File:** [TEAM.md](TEAM.md).

**Quy tắc quyết định:** chỉ chọn “Tiếp tục” khi bằng chứng đáp ứng tiêu chí đã
ký và không còn dòng vượt trần liên quan. “Thu hẹp”, “Cải tiến thêm”, “Dừng”
đều có thể đạt khi có căn cứ; không buộc phải làm báo cáo thành “Tiếp tục”.

### M8 — Demo và nộp cuối · phút 200–240 và hạn LMS

- [ ] **M8.1 · Cả nhóm:** tập demo 5 phút: Ngô Duy Khánh trình bày ba mốc; Phạm Thế Hùng giải thích
  cổng và lỗi; Nguyễn Nhật Minh nói vận hành/rủi ro; Nguyễn Đình Minh nêu quyết định và số liệu đỡ cho nó.
  Kiểm mỗi người giải thích được phần mình và lý do chọn con số.
  **Tham khảo (chỉ đọc):** [form-b-evaluation-gates.md - B8](templates/form-b-evaluation-gates.md#b8), [form-c-incident.md - C12](templates/form-c-incident.md#c12), [README.md](submission/README.md).
- [ ] **M8.2 · Phạm Thế Hùng + Ngô Duy Khánh:** chạy ticket hiểm/đổi số theo phản biện, đọc kết quả;
  trả lại code/config về bản v2 đã thống nhất. Nếu thay đổi quyết định thì cập
  nhật C12/metadata cho khớp; chạy lại **K7/K8** trên bản cuối.
  **File:** [guards.py](lab10/guards.py), [operating_gates.json](config/operating_gates.json), [form-c-incident.md - C12](templates/form-c-incident.md#c12), [submission.json](submission/submission.json).
- [ ] **M8.3 · Nguyễn Đình Minh, Ngô Duy Khánh kiểm chéo:** commit/push bài cuối bằng **K9**; mở GitHub
  kiểm có `submission/`, `TEAM.md`, report ba mốc, `journal.jsonl`, lock và
  manifest. Kiểm không có secret/API key/`.env`, không đẩy lên upstream.
  **File:** [TEAM.md](TEAM.md), [submission.json](submission/submission.json), [PLAN.md](PLAN.md) · **Tham khảo (chỉ đọc):** [README.md](submission/README.md), [SUBMISSION.md](SUBMISSION.md).
- [ ] **M8.4 · Phạm Thế Hùng:** tự nộp link repo trên LMS, lưu xác nhận.
  **Tham khảo (chỉ đọc):** [SUBMISSION.md](SUBMISSION.md), [README.md](submission/README.md).
- [ ] **M8.5 · Nguyễn Đình Minh:** tự nộp link repo trên LMS, lưu xác nhận.
  **Tham khảo (chỉ đọc):** [SUBMISSION.md](SUBMISSION.md), [README.md](submission/README.md).
- [ ] **M8.6 · Nguyễn Nhật Minh:** tự nộp link repo trên LMS, lưu xác nhận.
  **Tham khảo (chỉ đọc):** [SUBMISSION.md](SUBMISSION.md), [README.md](submission/README.md).
- [ ] **M8.7 · Ngô Duy Khánh:** tự nộp link repo trên LMS, lưu xác nhận.
  **Tham khảo (chỉ đọc):** [SUBMISSION.md](SUBMISSION.md), [README.md](submission/README.md).

Hạn theo `SUBMISSION.md` (GMT+7): lab sáng trước 23h59 ngày lab; lab chiều/tối
trước 11h59 hôm sau. Chưa có thông tin buổi học nên không tự gán ngày hạn nộp.
Đẩy bản cuối trước phút 240; commit sau hạn không tính nếu chưa được Coach gia hạn.

## 5. Lệnh kiểm tra và thao tác theo mốc

Chạy tại gốc repo, mỗi dòng là một lệnh PowerShell riêng. Thay các chuỗi
`RUN_ID_…`, `Sx`, `TICKET_ID` bằng mã thật; không chạy nguyên placeholder.
Đây là lệnh để thực hiện kế hoạch, chưa được chạy chỉ vì chúng xuất hiện ở đây.

### K0 — Kiểm tra môi trường và hồi quy

```powershell
python --version
git remote -v
git status --short
git ls-files --eol data/world.json lab10/agent.py tests/test_public.py
python -m unittest discover -s tests -v
```

Mong đợi 13 tests OK. `i/lf w/crlf` ở file bảo vệ báo checkout đang đổi line
ending; cần dùng checkout LF trước khi ký. Chỉ đổi `core.autocrlf` không tự
chuyển các file đã checkout. Có thể chuẩn bị một checkout mới bằng lệnh dưới,
thay URL bằng repo nhóm đã chốt và chọn thư mục mới chưa có dữ liệu:

```powershell
git clone -c core.autocrlf=false "URL_REPO_NHOM" "..\lab10-lf"
```

Giữ công việc hiện tại, không dùng reset/xóa lock để xử lý lỗi. Chuyển kế hoạch
và thay đổi cần thiết sang checkout tích hợp trước khi bắt đầu chuỗi bằng chứng.

### K1 — Ký và lưu tiêu chí · chỉ sau khi cả nhóm duyệt

```powershell
python -m json.tool config/acceptance_criteria.json
python -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock
git commit -m "Sign acceptance criteria"
git push -u origin main
python -m lab10.criteria verify
```

Điều kiện: `ĐÃ KÝ.`, push thành công, verify OK; Phiếu A/A5 ghi đúng commit.
Nếu push lỗi, xử lý và xác nhận mốc ký đã lên repo trước khi chạy K2.

### K2 — Baseline và đối chiếu ngưỡng

```powershell
python -m lab10.eval --suite base --stage base --note "baseline, chua sua cong"
python -m lab10.gate --run "runs/RUN_ID_BASE/report.json"
```

Lưu run ID vào B0/B1, đọc cả chỉ số bắt buộc, kinh doanh/vận hành và theo kho/hãng.

### K3 — Trace lỗi nền

```powershell
python -m lab10.trace --suite base --stage base --ticket T-002 --seed 55
```

Đối chiếu tracking, proposal, sổ cái, lỗi hãng và tin nhắn. Ghi bước sai đầu tiên vào B2.

### K4 — Kiểm cổng hiện tại và ticket tự viết

```powershell
python -m json.tool config/operating_gates.json
python -m unittest discover -s tests -v
python -m lab10.eval --suite base --stage after --note "mo ta mot thay doi"
python -m lab10.trace --suite base --stage after --ticket T-002 --seed 55
python -m lab10.trace --suite base --stage after --adhoc "Don tre 9 ngay, hoan phi cho toi" --order O-1002 --customer C-02
```

Lệnh adhoc cuối chỉ minh họa cú pháp; nhóm phải thiết kế hai ticket để kiểm
tính chất của mình, dùng mã đơn/khách có thật trong dữ liệu giả lập. Không tự
coi adhoc là pass vì lệnh chạy xong; đọc tác động ghi thực tế.

### K5 — Chốt vòng 1 · chạy một lần khi đã sẵn sàng

```powershell
python -m lab10.checkpoint
python -m lab10.eval --suite base --stage prepared
python -m lab10.gate --run "runs/RUN_ID_PREPARED/report.json"
```

Điền B8 rồi commit/push theo lệnh cuối B8; không sửa bản chốt hoặc cột v1 về sau.

### K6 — Đo sự cố trước sửa vòng 2

Sau khi nhận đúng thẻ theo `incidents/README.md` và ghi số vào Phiếu C:

```powershell
python -m lab10.grade --incident Sx
python -m lab10.trace --suite Sx --stage prepared --ticket TICKET_ID --seed 11
```

Chạy trace cho ít nhất hai ticket khác kiểu. Grade có thể báo FAIL/PARTIAL
trước sửa; đọc nguyên nhân và giữ lại bằng chứng, không đổi tiêu chí để vượt qua.

### K7 — Kiểm vòng 2, hồi quy và report ba mốc

```powershell
python -m unittest discover -s tests -v
python -m lab10.eval --suite Sx --stage after --note "mo ta mot thay doi"
python -m lab10.eval --suite base --stage after --note "kiem bo nen sau sua"
python -m lab10.grade --incident Sx
```

Đọc `integrity`, `criteria`, `visible`, `regression`, `monitor`, độ phủ và các
trần/ngưỡng. Test ẩn do team chấm chạy sau; thiếu gói ẩn không chứng minh đã qua.
Nếu còn chỉ số không đạt, ghi đúng trong C12 và chọn quyết định có căn cứ.

### K8 — Gom và kiểm đủ bài nộp

```powershell
python -m json.tool submission/submission.json
python -m lab10.check_submission --collect
```

Đọc từng `[THIẾU]` và dòng hướng dẫn `->`; sửa file nguồn rồi chạy lại. Yêu cầu
cuối: `ĐỦ THÀNH PHẦN` và bộ nộp phản ánh đúng code/config/phiếu cuối cùng.

### K9 — Đẩy bản cuối

```powershell
git diff --check
git status --short
git add -u
git add submission templates TEAM.md PLAN.md AGENTS.md
git diff --cached --stat
git commit -m "LAB 10: bai nop"
git push -u origin main
```

Kiểm danh sách staged trước commit; không đưa file nhạy cảm hay thay đổi ngoài
phạm vi vào bài. Kiểm trực tiếp repo Public sau push, rồi cả bốn người nộp LMS.

## 6. Điều kiện hoàn thành toàn dự án

- [ ] **Ngô Duy Khánh:** file bảo vệ, tiêu chí đã ký và bản chốt còn nguyên hash.
- [ ] **Nguyễn Đình Minh:** bằng chứng ký/commit/push có trước đánh giá; v1 có trước thẻ.
- [ ] **Phạm Thế Hùng + Ngô Duy Khánh:** cổng tổng quát; không làm hỏng ca nền vốn đúng; monitor mới
  có ý nghĩa. Nếu còn lỗi, ghi rõ thay vì tuyên bố đã sửa xong.
- [ ] **Nguyễn Nhật Minh:** A1–A5, B0–B8, C0–C12 đầy đủ theo ngoại lệ của thẻ; PIC/runbook/
  rủi ro khớp config; bốn mục cá nhân đầy đủ.
- [ ] **Nguyễn Đình Minh + cả nhóm:** v2 và ba dòng bắt buộc khớp tiêu chí đã ký và bằng chứng.
- [ ] **Ngô Duy Khánh:** collect trên bản cuối in `ĐỦ THÀNH PHẦN`; report/journal/manifest
  và các bản nguồn tương ứng có đủ trong bài nộp.
- [ ] **Nguyễn Đình Minh:** repo đúng tên/Public, bản cuối đã push trước hạn; **cả 4 người**
  có xác nhận nộp link LMS.

Tài liệu đối chiếu: `README.md`, `CHECKPOINTS.md`, `problem-set.md`, `RULES.md`,
`RUBRIC.md`, `SUBMISSION.md`, `templates/README.md`, `submission/README.md`.
