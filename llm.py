import os
from google import genai

# Create Gemini client using environment variable
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Free + fast model
MODEL = "gemini-1.5-flash"

def generate_reply(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )
        return response.text.strip()
    except Exception:
        # Fallback reply if Gemini fails
        return "Please explain a little more. I am trying to understand."
