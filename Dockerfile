FROM ubuntu:latest
MAINTAINER Denis Skorikov 'skorikov.denis.o@gmail.com'
RUN apt-get update -y
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENV FLASK_APP "reading_books.py"
CMD flask db upgrade && flask run --host 0.0.0.0
