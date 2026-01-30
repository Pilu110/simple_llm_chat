import requests
import os

API_URL = "https://router.huggingface.co/v1/chat/completions"
HUGGING_FACE_API_TOKEN = os.getenv('HUGGING_FACE_API_TOKEN', '')
HEADERS = {
    "Authorization": "Bearer " + HUGGING_FACE_API_TOKEN,
    "Content-Type": "application/json"
}

QUESTION = "Mi Hayao Miyakazi véleménye az AI-ról? Rövid, pár mondatos választ szeretnék."

MODEL = "openai/gpt-oss-120b"

PAYLOAD = {
    "model" : MODEL,
    "messages" : [
        {"role":"user", "content": QUESTION}
    ],
    "max_tokens": 1000
}


def main():
    print('Kérdés:')
    print('=' * 100)
    print(QUESTION)
    print('=' * 100)

    response = requests.post(API_URL, headers=HEADERS, json=PAYLOAD)

    print('Debug server response:')
    print(response.text)

    response.raise_for_status()
    response_json = response.json()

    print('Érvelés:')
    print('=' * 100)
    print(response_json['choices'][0]['message']['reasoning'])
    print('=' * 100)

    print('Válasz:')
    print(response_json['choices'][0]['message']['content'])

if __name__ == '__main__':
    main()
