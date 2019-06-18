FROM python:3.5-jessie

COPY app.py /

RUN mkdir -p /weather-rest-api

WORKDIR /weather-rest-api

ADD requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

ADD . /weather-rest-api

ADD app.py /

EXPOSE 80

CMD ["python", "./app.py"]
