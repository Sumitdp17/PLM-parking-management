"""
Payment Gateway - Handles card, cash, and QR payments.
"""


def process_card_payment(card_number: str, amount: float) -> dict:
    """Mock card payment processing."""
    if len(card_number) == 16 and card_number.isdigit():
        return {"status": "success", "method": "card", "amount": amount, "message": "Card payment successful"}
    return {"status": "failed", "reason": "Invalid card number", "message": "Card payment failed"}


def process_cash_payment(amount: float) -> dict:
    """Cash payment is always valid."""
    return {"status": "success", "method": "cash", "amount": amount, "message": "Cash accepted"}


def process_qr_payment(qr_code: str, amount: float) -> dict:
    """Mock QR validation: Only accepts codes starting with VALID_QR."""
    if qr_code.startswith("VALID_QR"):
        return {"status": "success", "method": "qr", "amount": amount, "message": "QR payment successful"}
    return {"status": "failed", "reason": "Invalid QR code", "message": "QR payment failed"}


# ✅ Wrapper class used by exit_handler
class PaymentGateway:
    @staticmethod
    def process_payment(amount: float, method: str = "cash") -> dict:
        method = method.lower()

        if method == "cash":
            return process_cash_payment(amount)

        elif method == "card":
            return process_card_payment("1234567812345678", amount)

        elif method == "qr":
            return process_qr_payment("VALID_QR_123", amount)

        else:
            return {"status": "failed", "reason": "Invalid payment method", "message": "Invalid payment method"}
