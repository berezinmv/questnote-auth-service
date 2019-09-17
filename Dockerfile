FROM python:3.7.3-slim-stretch

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "sh" ]

CMD [ "start.sh" ]