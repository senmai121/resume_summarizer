import requests
import json
import pdfplumber
from dotenv import load_dotenv
import os

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()


pdf_path = "./KANACHAI NIYOMSILPCHAI.docx 20250429.pdf"  # 🔁 เปลี่ยนเป็นพาธจริง

load_dotenv()

openrouter_token=os.getenv("OPENROUTER_TOKEN")
bearer=f"Bearer {openrouter_token}" 

print("################")

resume_text = extract_text_from_pdf(pdf_path)
#print(resume_text)


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
print(response.status_code)
print(response.json())

