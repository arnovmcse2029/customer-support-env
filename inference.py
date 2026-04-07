import requests
from groq import Groq

# 🔑 Put your API key here
client = Groq(api_key="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")

BASE_URL = "http://localhost:8000"

def ask_llm(ticket):
    prompt = f"""
You are a customer support AI.

Ticket: {ticket}

Respond ONLY in JSON:
{{
    "category": "...",
    "priority": "...",
    "action": "...",
    "response": "..."
}}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def run():
    print("[START]")

    obs = requests.post(f"{BASE_URL}/reset").json()
    print("[STEP] Observation:", obs)

    ticket = obs["ticket"]

    output = ask_llm(ticket)
    print("[STEP] Raw LLM Output:", output)

    import json
    try:
        action = json.loads(output)
    except:
        action = {
            "category": "complaint",
            "priority": "high",
            "action": "escalate",
            "response": "We are sorry for the inconvenience."
        }

    result = requests.post(f"{BASE_URL}/step", json=action).json()
    print("[STEP] Result:", result)

    print("[END]")


if __name__ == "__main__":
    run()