FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install -r requirement.txt

CMD ["python", "app.py"]
