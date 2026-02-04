import os
from google import genai

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def llm_scam_analysis(message: str) -> bool:
    prompt = f"""
You are a scam detection system.
If the message is asking for money, payment, UPI, bank transfer, or links, respond ONLY with YES or NO.

Message:
{message}
"""

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    answer = response.text.strip().upper()
    return "YES" in answer


