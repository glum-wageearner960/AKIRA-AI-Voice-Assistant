import requests

def ask_ai(question):

    try:

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2:3b",
                "prompt": question,
                "stream": False
            }
        )

        data = response.json()

        return data["response"]

    except Exception as e:

        return f"AI Error: {e}"