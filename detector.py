def detect_scam(history):
    scam_keywords = [
        "bank",
        "account",
        "blocked",
        "urgent",
        "otp",
        "upi",
        "verify"
    ]

    text = " ".join([msg["content"].lower() for msg in history])

    return any(word in text for word in scam_keywords)
