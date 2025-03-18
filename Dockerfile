FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Non-root user for better security
RUN useradd -m appuser
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
