FROM python:3.7-slim-stretch AS base
COPY . /
WORKDIR /
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3", "app/app.py" ]