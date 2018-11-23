FROM python:3.6-alpine

RUN apk --no-cache --update-cache add gcc gfortran python python-dev py-pip build-base wget freetype-dev libpng-dev openblas-dev
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

COPY . /clustering-app
WORKDIR /clustering-app

RUN pip install -r requirements.txt

EXPOSE 8000
