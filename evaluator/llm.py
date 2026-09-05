import os
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

client = OpenAI(api_key=API_KEY) if API_KEY else None


def generate_response(prompt):

    # If API key is not available
    if not API_KEY:
        return {
            "response": "Demo response because OpenAI API key is not available.",
            "latency": 0.001,
            "tokens": 10,
            "mode": "DEMO"
        }

    # Use OpenAI
    try:
        start = time.time()

        response = client.responses.create(
            model=MODEL,
            input=prompt
        )

        latency = time.time() - start

        return {
            "response": response.output_text,
            "latency": round(latency, 3),
            "tokens": response.usage.output_tokens if response.usage else 0,
            "mode": "REAL OPENAI"
        }

    except Exception as e:

        print("OpenAI Error:", e)

        return {
            "response": "Demo response because OpenAI request failed.",
            "latency": 0.001,
            "tokens": 10,
            "mode": "DEMO"
        }