import re

def redact(text):
    text = re.sub(r"\b\d{3}-\d{2}-\d{4}\b", "[REDACTED-SSN]", text)
    text = re.sub(r"\b\d{2}/\d{2}/\d{4}\b", "[REDACTED-DOB]", text)
    return text
