"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
  "events"         trace của ticket; sự kiện do cổng ghi có dạng {"type": "guard", "kind": ...}
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""

ESCALATED_COST_VND = 10_000   # ops_facts.review_cost_per_ticket_vnd
# shortcut: kiểm lại tính cố định 4.000đ (= 0,4 ca × 10.000đ khi có ghi chú); monitor_view không có review_units nên
# không đọc được cấu hình. Nâng cấp: đưa review_units vào monitor_view và nhân với review_cost_per_ticket_vnd.
RECHECK_COST_VND = 4_000
MIN_TRIALS_PER_WAREHOUSE = 10  # dưới mức này một kho quá ít mẫu, không tính vào max


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def cost_per_ticket_worst_warehouse(trials):
    """Chi phí trung bình mỗi ticket (đồng) của kho đắt nhất: tiền máy + công người (chuyển người, kiểm lại).

    Không dùng nhãn. Kho không gắn được (warehouse None) và kho có dưới 10 trial bị bỏ khỏi max.
    Đây là con số "chi phí mỗi ticket theo kho" ở Phiếu C mục C8.
    """
    by_wh: dict = {}
    for t in trials:
        w = t.get("warehouse")
        if w is None:
            continue
        extra = ESCALATED_COST_VND if t.get("review_kind") == "escalated" \
            else RECHECK_COST_VND if t.get("review_kind") == "recheck" else 0
        by_wh.setdefault(w, []).append(t.get("cost_vnd", 0) + extra)
    costs = [sum(v) / len(v) for v in by_wh.values() if len(v) >= MIN_TRIALS_PER_WAREHOUSE]
    return max(costs, default=0.0)


def duplicate_refund_attempts(trials):
    """Tỉ lệ ticket mà cổng thấy đơn đã có khoản hoàn trong sổ cái (Phiếu C mục C2 Lỗi 1). Không cần nhãn."""
    n = sum(any(e.get("type") == "guard" and e.get("kind") == "duplicate_refund" for e in t.get("events", []))
            for t in trials)
    return n / max(1, len(trials))


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "cost_per_ticket_worst_warehouse": cost_per_ticket_worst_warehouse,   # mới, thẻ S5
    "duplicate_refund_attempts": duplicate_refund_attempts,               # mới, thẻ S5
}
STARTER_MONITORS = ("escalation_rate",)
