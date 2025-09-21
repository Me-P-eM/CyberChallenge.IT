FROM python:3.9-slim

RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/*
RUN useradd -ms /bin/bash appuser

WORKDIR /app
COPY app/ /app

RUN echo '#!/bin/bash\nexec socat TCP-LISTEN:6005,reuseaddr,fork EXEC:"timeout 300 python3 -u /app/app.py",stderr' > /app/entrypoint.sh && \
    chmod +x /app/entrypoint.sh

USER appuser

ENTRYPOINT ["./entrypoint.sh"]