import re

def extract_scam_data(message: str):
    data = {
        "upi_id": None,
        "bank_account": None,
        "ifsc": None,
        "phishing_url": None
    }

    upi_match = re.search(r"[a-zA-Z0-9.\-_]{2,}@[a-zA-Z]{2,}", message)
    if upi_match:
        data["upi_id"] = upi_match.group()

    bank_match = re.search(r"\b\d{9,18}\b", message)
    if bank_match:
        data["bank_account"] = bank_match.group()

    ifsc_match = re.search(r"\b[A-Z]{4}0[A-Z0-9]{6}\b", message)
    if ifsc_match:
        data["ifsc"] = ifsc_match.group()

    url_match = re.search(r"http[s]?://\S+", message)
    if url_match:
        data["phishing_url"] = url_match.group()

    return data
