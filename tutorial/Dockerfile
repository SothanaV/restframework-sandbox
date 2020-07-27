FROM python:3.8
ADD requirements.txt /tutorial/requirements.txt
RUN pip install -r /tutorial/requirements.txt
RUN apt-get update && apt-get install -y netcat
ADD . /tutorial
WORKDIR /tutorial