from llm import generate_reply

AGENT_PROMPT = """
You are a naive but cooperative victim.
Your goal is to keep the scammer talking and make them reveal:
- bank account numbers
- UPI IDs
- payment links
- phishing URLs

Never sound suspicious.
Never accuse them.
Ask innocent follow-up questions.
"""

def agent_reply(history: list) -> str:
    convo = "\n".join([f"{m['role']}: {m['content']}" for m in history])
    prompt = AGENT_PROMPT + "\n\n" + convo
    return generate_reply(prompt)
