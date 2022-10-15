FROM alpine:3.16.2

WORKDIR /app

RUN apk add --no-cache bash

# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

COPY requirements.txt .

RUN pip3 install -r requirements.txt 

COPY . .

CMD [ "python", "main.py" ]