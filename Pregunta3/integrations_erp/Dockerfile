FROM python:3.10.12

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY .env /code/.env

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate", "python", "manage.py", "runserver", "0.0.0.0:8000"]