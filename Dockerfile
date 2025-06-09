# 1. Базовый образ
FROM python:3.10-slim

# 2. Установка зависимостей
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Копируем проект
COPY . .

# 4. Команда запуска
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
