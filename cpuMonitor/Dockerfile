FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip2 install --no-cache-dir  requirements.txt

COPY . .

ENV HOST 0.0.0.0

EXPOSE 5000
# python app.py

CMD ["flask", "run"]

