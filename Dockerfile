FROM python:3.8-alpine

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 1

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev libffi-dev rust openssl-dev \
    && apk add postgresql-dev \
    && pip install --upgrade pip \
    && pip install psycopg2 \
    && pip install cryptography==2.8 \
    && apk del build-deps

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

RUN adduser -D myuser
USER myuser

CMD gunicorn movies.wsgi:application --bind 0.0.0.0:$PORT
