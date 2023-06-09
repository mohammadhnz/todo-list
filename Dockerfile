FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN mkdir -p /app
RUN mkdir -p /app/logs

WORKDIR /app

COPY requirements/base.txt .


RUN pip install --no-cache-dir -r base.txt
RUN adduser --disabled-password --gecos '' myuser

COPY . .

EXPOSE 8000

CMD ["gunicorn", "_base.wsgi", ":8000"]
