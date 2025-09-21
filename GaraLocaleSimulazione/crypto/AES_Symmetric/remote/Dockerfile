FROM python:3.9-slim

RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/*

WORKDIR /app0

COPY chall.py .

RUN pip install pycryptodome

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

EXPOSE 1337

ENTRYPOINT ["./entrypoint.sh"]

