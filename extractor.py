import re

def extract_intel(history: list):
    text = " ".join([m["content"] for m in history])

    bank_accounts = re.findall(r"\b\d{9,18}\b", text)
    upi_ids = re.findall(r"\b[\w.-]+@[\w]+\b", text)
    phishing_urls = re.findall(r"https?://[^\s]+", text)

    return {
        "bank_accounts": list(set(bank_accounts)),
        "upi_ids": list(set(upi_ids)),
        "phishing_urls": list(set(phishing_urls))
    }
