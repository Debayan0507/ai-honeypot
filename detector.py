from llm import generate_reply

SYSTEM_PROMPT = """
You are a cybersecurity system.
Analyze the conversation and answer ONLY one word:
YES if this looks like a scam.
NO if it does not.
"""

def detect_scam(history: list) -> bool:
    convo = "\n".join([f"{m['role']}: {m['content']}" for m in history])
    prompt = SYSTEM_PROMPT + "\n\n" + convo

    response = generate_reply(prompt).upper()
    return "YES" in response
