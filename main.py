from fastapi import FastAPI
from models import ScamRequest, ScamResponse
from detector import is_scam_message
from extractor import extract_scam_data
from llm import llm_scam_analysis

app = FastAPI(title="AI Scam Honeypot")

@app.get("/")
def root():
    return {"status": "AI Honeypot running"}

@app.post("/analyze", response_model=ScamResponse)
def analyze_scam(payload: ScamRequest):
    rule_scam = is_scam_message(payload.message)
    llm_scam = llm_scam_analysis(payload.message)

    is_scam = rule_scam or llm_scam
    extracted = extract_scam_data(payload.message)

    return ScamResponse(
        is_scam=is_scam,
        extracted_data=extracted,
        action="engage_scammer" if is_scam else "ignore"
    )
