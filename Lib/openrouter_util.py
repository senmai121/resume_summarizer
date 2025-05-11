import requests
import json

def openrouter_request(resume_text,bearer):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
        "Authorization": bearer,
        "HTTP-Referer": "https://kanachain.vercel.app", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "nes", # Optional. Site title for rankings on openrouter.ai.
        },
        data=json.dumps({
        "model": "meta-llama/llama-3.2-3b-instruct:free", # Optional
        "messages": [
            {
            "role": "user",
            "content": f"give me the JSON object from this information : {resume_text}"
            }
        ],
        "max_tokens": 4000
        })
    )
    return response.json()
