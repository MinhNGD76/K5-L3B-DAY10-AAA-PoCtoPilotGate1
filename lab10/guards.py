"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Cổng vòng 1 của bàn AAA (Phiếu B mục B6, B7.1):
  Cổng 1 · Ghi theo nguồn sự thật: số tiền, kiện, hãng, số ngày lấy từ tracking + chính sách theo NGÀY (không theo model).
  Cổng 2 · Model hỏng hoặc bị điều khiển thì không ghi: fail_open (429), làm theo chỉ thị trong chữ khách, ghi lặp.
  Cổng 3 · Ranh giới đầu ra (Phiếu A) và trần đã thống nhất (ops_limits): phê duyệt hợp lệ, trần mỗi khách, trần lỗi
           mỗi hãng, thư gửi hãng chỉ chứa trường chính sách cho phép.

Vòng 2 (thẻ S5, Phiếu C mục C7):
  Nhánh [1] Hoàn nhiều lần: cổng 1 đổi từ "đã có khoản hoàn thì chuyển người" sang "chỉ ghi phần còn lại
           quyền lợi − đã hoàn trong sổ cái; đã đủ thì chuyển người xem". Ghi sự kiện `duplicate_refund` để đo.
  Nhánh [3] Chữ dán kèm: pre_guard chỉ giữ phần yêu cầu trước dấu `---` và tối đa 500 ký tự.
"""
from . import helpers as H
from .tools import Verdict

MONEY_AND_FAULT = ("issue_refund", "file_carrier_fault", "notify_carrier")
# shortcut: cắt chữ ticket ở dấu `---` và 500 ký tự; nâng cấp: tách đoạn yêu cầu bằng mô hình khi có dữ liệu thật.
TEXT_CAP = 500


def _policy(ctx):
    return H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)


def _request_part(text: str) -> str:
    """Chỉ phần yêu cầu của khách: bỏ danh sách/ghi chú dán kèm sau dấu `---`, và giới hạn độ dài."""
    return text.split("\n---", 1)[0][:TEXT_CAP]


def pre_guard(ctx):
    # Cổng 1: đơn ghi trong ticket không có trong DB thì chuyển người ngay, khỏi tốn tiền LLM đọc (B6: phạm vi).
    oid = ctx.ticket.get("order_id")
    if oid and ctx.tools.lookup_order(oid) is None:
        return Verdict.escalate(f"không có đơn {oid} trong DB")
    # Cổng 1: ghim chính sách theo ngày hiệu lực, không theo cờ index_active (B4 dòng INVALID).
    pol = _policy(ctx)
    if pol is None:
        return Verdict.escalate(f"không có chính sách hiệu lực ngày {ctx.as_of}")
    # Nhánh [3] (C4 dòng PERTURBED): chữ dán kèm không được đưa vào model như yêu cầu của khách.
    part = _request_part(ctx.ticket["text"])
    if part != ctx.ticket["text"]:
        ctx.log("text_trimmed", chars_cut=len(ctx.ticket["text"]) - len(part))
        return Verdict.rewrite("chỉ đọc phần yêu cầu, bỏ danh sách dán kèm", part, policy_id=pol["policy_id"])
    return Verdict.allow(policy_id=pol["policy_id"])


def write_gate(ctx, action):
    tool = action["tool"]
    if tool not in MONEY_AND_FAULT:
        return Verdict.allow()
    v = _model_state_gate(ctx)
    if v:
        return v
    if tool == "issue_refund":
        return _refund_gate(ctx, action)
    if tool == "file_carrier_fault":
        return _fault_gate(ctx, action)
    return _notice_gate(ctx, action)


def _model_state_gate(ctx):
    """Cổng 2: trạng thái model hỏng hoặc bị chữ bên ngoài điều khiển thì không lệnh ghi nào được chạy."""
    for e in ctx.events:
        if e.get("type") == "llm_fallback" and e.get("mode") == "fail_open":
            return Verdict.escalate("LLM lỗi 429, agent đang fail_open: không ghi tiền/lỗi hãng khi chưa kiểm chính sách")
        if e.get("type") == "directive_obeyed":
            return Verdict.escalate("chữ khách/ghi chú đơn chứa chỉ thị cho model: không làm theo, chuyển người")
    return None


def _refund_gate(ctx, a):
    t = ctx.tools
    order = t.lookup_order(a["order_id"])
    if order is None:
        return Verdict.escalate("không có đơn trong DB")
    # Cổng 2: agent ghi lại khi không chắc lệnh đầu đã vào sổ (confirm bị 429) -> bỏ lệnh lặp.
    if t.ledger_rows(ticket_id=a["ticket_id"]):
        return Verdict.deny("ticket này đã có dòng hoàn trong sổ cái: chặn ghi lặp")
    if a.get("payer", "LOGIX") != "LOGIX":
        return Verdict.escalate(f"người trả {a.get('payer')} không có căn cứ trong chính sách")
    pol = _policy(ctx)
    if pol is None:
        return Verdict.escalate(f"không có chính sách hiệu lực ngày {ctx.as_of}")
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of)
    owed = H.entitlement_vnd(pol, order, delay, parcel.get("delay_cause"))
    # Cổng 1: số tiền phải đúng quyền lợi tính từ tracking, không từ số ngày khách khai (T-002@55).
    if a["amount_vnd"] != owed:
        return Verdict.escalate(f"số tiền {a['amount_vnd']}đ khác quyền lợi theo tracking {owed}đ "
                                f"(trễ {delay} ngày, {pol['policy_id']})")
    # Cổng 1 (C5 specification): tổng đã hoàn trong sổ cái của đơn không vượt quyền lợi.
    # Cờ refund_status chỉ cập nhật ban đêm nên không dùng; sổ cái gồm cả khoản CSKH hoàn tay.
    paid = sum(r["amount_vnd"] for r in t.ledger_rows(order_id=a["order_id"]))
    if paid > 0:
        ctx.log("duplicate_refund", order_id=a["order_id"], paid_vnd=paid, owed_vnd=owed)
    remaining = owed - paid
    if remaining <= 0:
        # Đã đủ quyền lợi: chuyển người xem, không ghi thêm. Không dùng "từ chối" vì câu trả lời của agent
        # sẽ nói "chưa hoàn khoản nào", sai với đơn này.
        return Verdict.escalate(f"đơn {a['order_id']} đã hoàn {paid}đ trong sổ cái, đủ quyền lợi {owed}đ: chuyển người xem")
    amount = min(a["amount_vnd"], remaining)
    lim = t.ops_limits()
    # Cổng 3: vượt hạn mức tự động thì phải có phê duyệt còn hiệu lực, đúng ticket, đủ hạn mức.
    if amount > pol["auto_limit_vnd"]:
        appr = t.lookup_approvals(approval_id=a.get("approval_id")) if a.get("approval_id") else []
        ok = appr and appr[0]["status"] == "valid" and appr[0]["ticket_id"] == a["ticket_id"] \
            and appr[0]["expires_at"] >= ctx.as_of and appr[0]["max_vnd"] >= amount
        if not ok:
            return Verdict.escalate(f"vượt hạn mức tự động {pol['auto_limit_vnd']}đ mà phê duyệt "
                                    f"{a.get('approval_id')} không hợp lệ cho ticket này")
    else:
        # shortcut: ledger_rows còn gồm dòng sổ cái cũ (ledger_seed) nên cộng dồn thận trọng hơn "trong ngày";
        # đổi sang lọc theo ngày khi sổ cái có trường ngày.
        cap = lim.get("max_auto_refund_per_customer_per_day_vnd")
        auto = sum(r["amount_vnd"] for r in t.ledger_rows(customer_id=order["customer_id"]) if not r.get("approval_id"))
        if cap is not None and auto + amount > cap:
            return Verdict.escalate(f"tổng hoàn tự động cho khách {order['customer_id']} sẽ vượt {cap}đ/ngày")
    # Cổng 3: từ lỗi thứ 3 của cùng một hãng trong ngày phải có người duyệt -> chuyển người TRƯỚC khi ghi tiền.
    strikes = lim.get("max_auto_strikes_per_carrier_per_day")
    if strikes is not None and H.carrier_at_fault(pol, parcel, delay) \
            and len(t.fault_rows(carrier_id=parcel["carrier_id"])) >= strikes:
        return Verdict.escalate(f"hãng {parcel['carrier_id']} đã có {strikes} lỗi tự động hôm nay")
    if amount != a["amount_vnd"]:
        return Verdict.modify(f"đơn đã hoàn {paid}đ trong sổ cái: chỉ ghi phần còn lại {amount}đ", amount_vnd=amount)
    return Verdict.allow()


def _fault_gate(ctx, a):
    """Cổng 1: chỉ ghi lỗi cho đúng kiện trễ, đúng hãng, đúng số ngày tracking, nguyên nhân thuộc fault_causes."""
    order = ctx.tools.lookup_order(a["order_id"])
    pol = _policy(ctx)
    if order is None or pol is None:
        return Verdict.deny("thiếu đơn hoặc chính sách để kiểm lỗi hãng")
    at_fault = [p for p in order["parcels"] if H.carrier_at_fault(pol, p, H.db_delay_days(p, ctx.as_of))]
    asked = next((p for p in at_fault if p["parcel_id"] == a.get("parcel_id")), None)
    if asked and a.get("carrier_id") == asked["carrier_id"] and a.get("delay_days") == H.db_delay_days(asked, ctx.as_of):
        return Verdict.allow()
    if len(at_fault) == 1:          # agent lấy kiện đầu tiên / số ngày khách khai: sửa về đúng kiện theo tracking
        p = at_fault[0]
        return Verdict.modify("sửa lỗi hãng về đúng kiện trễ theo tracking", parcel_id=p["parcel_id"],
                              carrier_id=p["carrier_id"], driver_id=p.get("driver_id"),
                              delay_days=H.db_delay_days(p, ctx.as_of))
    return Verdict.deny("tracking không cho thấy kiện nào trễ do hãng: không ghi lỗi")


def _notice_gate(ctx, a):
    """Cổng 3: thư gửi hãng chỉ giữ các trường chính sách cho phép (carrier_notice_fields), bỏ chữ khách và liên hệ người nhận."""
    pol = _policy(ctx)
    allowed = set(pol["carrier_notice_fields"]) if pol else {"order_id", "parcel_id", "delay_days"}
    payload = a.get("payload") or {}
    extra = sorted(set(payload) - allowed)
    if extra:
        return Verdict.modify(f"bỏ trường không được gửi cho hãng: {extra}",
                              payload={k: v for k, v in payload.items() if k in allowed})
    return Verdict.allow()
