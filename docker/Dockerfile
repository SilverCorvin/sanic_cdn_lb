FROM python:3.7-alpine

RUN apk update \
    && apk add build-base

COPY ./requirements /tmp/requirements
RUN pip install -r /tmp/requirements/prod.txt \
    && rm -Rf /tmp/requirements

ADD ./app /app
COPY ./docker/bin/entrypoint.sh /app
WORKDIR /app

ENTRYPOINT ["/app/entrypoint.sh"]
