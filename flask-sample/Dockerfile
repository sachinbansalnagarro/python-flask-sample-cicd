FROM python:3.7-slim-stretch AS base

COPY . /
# COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt



ENTRYPOINT [ "python3", "app/app.py" ]


# docker build -t flask-sample:latest .

# docker run -ls -p 5000:5000 flask-sample

# https://linuxize.com/post/how-to-remove-docker-images-containers-volumes-and-networks/