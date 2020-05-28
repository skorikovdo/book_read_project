FROM ubuntu:latest
MAINTAINER Denis Skorikov 'skorikov.denis.o@gmail.com'
RUN apt-get update -y
RUN apt-get update -y \
  && apt-get install -y python3-pip python3-dev \
  && pip3 install --upgrade pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_APP "reading_books.py"
CMD ['flask run']