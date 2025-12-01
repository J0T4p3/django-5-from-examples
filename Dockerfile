# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /blog
COPY mysite/ /blog/
COPY requirements.txt /blog/
RUN pip install -r requirements.txt
