from openai import OpenAI
from config import OPENAI_API_KEY, LLM_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def extract_scenario(query):
    prompt = f"""
    The user asked: '{query}'.
    Extract the scenario or intent in 1 concise sentence.
    """
    resp = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.choices[0].message.content.strip()
