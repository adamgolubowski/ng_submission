FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /ng
WORKDIR /ng
ADD requirements.txt /ng/
RUN pip install -r requirements.txt
ADD . /ng