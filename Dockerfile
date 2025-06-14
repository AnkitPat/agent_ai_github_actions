FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]



# gcloud run deploy ai-tool \
#   --image gcr.io/second-ai-agent/ai-tool \
#   --platform managed \
#   --region asia-south1 \
#   --allow-unauthenticated \
#   --timeout 300s \
#   --set-env-vars OPENAI_API_KEY=token