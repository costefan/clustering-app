FROM python:3.6-alpine

COPY . /clustering-app
WORKDIR /clustering-app

RUN pip install -r requirements.txt

EXPOSE 8000
