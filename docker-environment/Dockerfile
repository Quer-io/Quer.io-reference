FROM frolvlad/alpine-python-machinelearning:latest
ADD . /code
WORKDIR /code
COPY . .

RUN apk add --no-cache bash

RUN pip install --upgrade pip && \
 apk update && \
 apk add gcc && \
 apk add libc-dev && \
 apk add linux-headers && \
 apk add postgresql-libs && \
 apk add mariadb-dev && \
 apk add python3-dev && \
 apk add --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt

