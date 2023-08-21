
FROM python:3.7.4-slim-buster as base

ARG ARG_USER_ID \
    ARG_GROUP_ID
ENV USER_ID=${ARG_USER_ID}
ENV GROUP_ID=${ARG_GROUP_ID}

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libssl-dev \
    libffi-dev \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Path: Dockerfile
RUN pip3 install --upgrade pip
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

FROM base as dev
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

FROM base as prod
COPY . /user
WORKDIR /user
RUN rm -rf /chatgpt-life/requirements.txt

