# Legacy SpanTrace file
import re


def detect_sensitive(text):
    findings = []

    # Email address
    if re.search(r'\b[\w.-]+@[\w.-]+\.\w+\b', text):
        findings.append("EMAIL")

    # Indian phone number
    if re.search(r'\b(?:\+91[\s-]?)?[6-9]\d{9}\b', text):
        findings.append("PHONE")

    # Credit/debit-card-like number
    if re.search(r'\b(?:\d[ -]*?){13,16}\b', text):
        findings.append("FINANCIAL")

    # Password
    if re.search(
        r'\b(password|passwd|pwd)\s*[:=]\s*\S+',
        text,
        re.IGNORECASE
    ):
        findings.append("PASSWORD")

    # API keys / secret keys
    if re.search(
        r'\b(api[_-]?key|secret[_-]?key)\s*[:=]\s*\S+',
        text,
        re.IGNORECASE
    ):
        findings.append("API_KEY")

    return findings