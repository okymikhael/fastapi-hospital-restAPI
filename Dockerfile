# syntax=docker/dockerfile:1

FROM python:3.8.11

WORKDIR /app/python-fastapi/

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app/python-fastapi/

CMD [ "uvicorn", "main:app", "--reload" ]