FROM ubuntu:20.04

ENV TZ=America/Chicago
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && \
    apt-get install -y vim software-properties-common python3.9 python3-pip libpq-dev build-essential libssl-dev libffi-dev python3-dev && \
    apt-get clean

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 2
RUN update-alternatives --config python3

WORKDIR app
COPY . /app

RUN pip3 install -r requirements.txt
RUN pip3 install --upgrade cython