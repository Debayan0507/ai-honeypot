from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI()

API_KEY = "test-key"  # temporary

class Message(BaseModel):
    role: str
    content: str

class HoneypotRequest(BaseModel):
    conversation: list[Message]

@app.post("/honeypot")
def honeypot(
    data: HoneypotRequest,
    x_api_key: str = Header(None)
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    return {
        "is_scam": True,
        "confidence": 0.75,
        "reason": "Suspicious banking message detected"
    }
