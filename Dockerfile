FROM python:3.10-slim

WORKDIR /app

COPY flask_app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY flask_app/ /app/flask_app/
COPY src/ /app/src/
COPY models/ /app/models/

ENV PYTHONPATH=/app

EXPOSE 5000

CMD ["python3", "-m", "flask_app.app"]

#Prod
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "120", "app:app"]