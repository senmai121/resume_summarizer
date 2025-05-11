import pdfplumber
from dotenv import load_dotenv
import os
import time
from Lib.openrouter_util import openrouter_request
from Lib.mongodb_util import find_experience


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
mongdb_uri = os.getenv("MONGODB_URI")
bearer=f"Bearer {openrouter_token}" 

print("################")
for count in range(3):
#while True:
  resume_text = extract_text_from_pdf(pdf_path)
  #print(resume_text)


  result = openrouter_request(resume_text,bearer)
  print("#########",flush=True)
  print(result,flush=True)

  experiences = find_experience(mongdb_uri)
  for experience in experiences :
    print("#######EXP########")
    print(experience, flush=True)
  time.sleep(300)

