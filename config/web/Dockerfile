FROM python:3.8

RUN mkdir /config

ADD /requirements.txt /config/
ADD /entry_point.sh /config/

RUN pip install -r /config/requirements.txt

RUN mkdir /src;

WORKDIR /src
