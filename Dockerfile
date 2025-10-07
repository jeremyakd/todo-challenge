FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

WORKDIR /app/todo_project

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "todo_project.wsgi:application", "--bind", "0.0.0.0:8000"]
