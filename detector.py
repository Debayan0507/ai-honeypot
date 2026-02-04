import re

def is_scam_message(message: str) -> bool:
    patterns = [
        r"\bupi\b",
        r"\b@ybl\b",
        r"\b@oksbi\b",
        r"\b@okaxis\b",
        r"\b@okhdfc\b",
        r"\baccount\b",
        r"\bifsc\b",
        r"\bsend\b.*\d+",
        r"\bpay\b",
        r"\btransfer\b",
        r"\$\d+",
        r"₹\d+",
        r"http[s]?://"
    ]

    for pattern in patterns:
        if re.search(pattern, message.lower()):
            return True

    return False
