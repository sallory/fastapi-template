FROM python:3.11-slim-buster

WORKDIR /code

COPY ./src/requirements /code/requirements

RUN pip install --no-cache-dir --upgrade -r /code/requirements/local.txt

COPY ./scripts/prestart.sh /
COPY ./scripts/start-reload.sh /

RUN chmod +x /prestart.sh
RUN chmod +x /start-reload.sh

COPY ./src /code/src

CMD ["/start-reload.sh"]
