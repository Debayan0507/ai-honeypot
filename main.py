import os
import time
from fastapi import FastAPI, Header, HTTPException
from dotenv import load_dotenv

from detector import detect_scam
from agent import agent_reply
from memory import store_message, get_history
from extractor import extract_intel

load_dotenv()

API_KEY = os.getenv("HONEYPOT_API_KEY")

app = FastAPI()

scam_sessions = set()

@app.post("/honeypot")
def honeypot(data: dict, x_api_key: str = Header(None)):

    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    convo_id = data["conversation_id"]
    message = data["message"]

    start_time = time.time()

    store_message(convo_id, "user", message)
    history = get_history(convo_id)

    if convo_id in scam_sessions:
        is_scam = True
    else:
        is_scam = detect_scam(history)
        if is_scam:
            scam_sessions.add(convo_id)

    if is_scam:
        reply = agent_reply(history)
        intel = extract_intel(history)
    else:
        reply = "Okay, can you explain more?"
        intel = {
            "bank_accounts": [],
            "upi_ids": [],
            "phishing_urls": []
        }

    store_message(convo_id, "assistant", reply)

    return {
        "is_scam": is_scam,
        "agent_activated": is_scam,
        "reply": reply,
        "engagement": {
            "turns": len(history),
            "duration_seconds": int(time.time() - start_time)
        },
        "extracted_intelligence": intel
    }
