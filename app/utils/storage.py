from threading import Lock


lock = Lock()

receipts = {}


def store_receipt(receipt_id: str, points: int):
    with lock:
        receipts[receipt_id] = points


def get_receipt_points(receipt_id: str) -> int:
    with lock:
        return receipts.get(receipt_id)
