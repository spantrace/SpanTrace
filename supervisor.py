# Legacy SpanTrace file
import re
from detector import detect_sensitive


def supervise(user_message):

    findings = detect_sensitive(user_message)

    # Extremely sensitive information
    if "PASSWORD" in findings:
        return {
            "allowed": False,
            "message": "BLOCKED: Your message contains a password.",
            "findings": findings
        }

    if "API_KEY" in findings:
        return {
            "allowed": False,
            "message": "BLOCKED: Your message contains an API key or secret key.",
            "findings": findings
        }

    # Redact information that can safely be removed
    cleaned = user_message

    if "PHONE" in findings:
        cleaned = re.sub(
            r'\b(?:\+91[\s-]?)?[6-9]\d{9}\b',
            '[PHONE REDACTED]',
            cleaned
        )

    if "EMAIL" in findings:
        cleaned = re.sub(
            r'\b[\w.-]+@[\w.-]+\.\w+\b',
            '[EMAIL REDACTED]',
            cleaned
        )

    if "FINANCIAL" in findings:
        cleaned = re.sub(
            r'\b(?:\d[ -]*?){13,16}\b',
            '[FINANCIAL INFORMATION REDACTED]',
            cleaned
        )

    return {
        "allowed": True,
        "message": cleaned,
        "findings": findings
    }