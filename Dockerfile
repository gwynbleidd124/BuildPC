# Используем базовый образ Python
FROM python:3.10-slim

# Устанавливаем shell для выполнения команд
SHELL ["/bin/bash", "-c"]

# Настраиваем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Обновляем pip
RUN pip install --upgrade pip

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    libpq-dev \
    python3-dev \
    build-essential \
    libjpeg-dev \
    zlib1g-dev && \
    rm -rf /var/lib/apt/lists/*  # Очистка кэша apt для уменьшения размера образа

# Создаем пользователя и группу
RUN groupadd -r darkbe && useradd -r -g darkbe -ms /bin/bash darkbe

# Устанавливаем рабочую директорию
WORKDIR /app

# Создаем папки static и media и настраиваем права
RUN mkdir -p /app/static /app/media && \
    chown -R darkbe:darkbe /app && \
    chmod -R 755 /app

# Копируем только файл зависимостей на данном этапе
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект и назначаем владельца
COPY --chown=darkbe:darkbe . .

# Переключаемся на пользователя darkbe
USER darkbe

# Запускаем сервер Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]




