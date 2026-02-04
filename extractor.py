import re

def extract_intel(history):
    text = " ".join([msg["content"] for msg in history])

    bank_accounts = re.findall(r"\b\d{9,18}\b", text)
    upi_ids = re.findall(r"[a-zA-Z0-9.\-_]{2,}@[a-zA-Z]{2,}", text)
    urls = re.findall(r"https?://\S+", text)

    return {
        "bank_accounts": bank_accounts,
        "upi_ids": upi_ids,
        "phishing_urls": urls
    }
