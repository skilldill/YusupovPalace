# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python3 manage.py

RUN pip3 install -r requirements.txt

COPY . .

CMD "FLASK_APP=app.py FLASK_ENV=development flask run"