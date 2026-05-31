import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_fixed_code(prompt):

    payload = {
        "model": "deepseek-coder:1.3b",
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": 300,
            "temperature": 0.1
        }
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=600
    )

    data = response.json()

    return data["response"]