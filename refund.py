# Legacy SpanTrace file
def process_refund(amount):
    if amount > 100:
        return f"REJECTED: Refund of ${amount:.2f} is over the $100 limit."
    else:
        return f"APPROVED: Refund of ${amount:.2f} is allowed."
