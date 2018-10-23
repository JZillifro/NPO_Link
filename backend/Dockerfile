FROM python:3.7.0-alpine

RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd


WORKDIR /usr/backend

COPY ./requirements.txt /usr/backend/requirements.txt

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/backend/entrypoint.sh
RUN chmod 755 /usr/backend/entrypoint.sh


COPY . /usr/backend

EXPOSE 5000

ENTRYPOINT [ "/usr/backend/entrypoint.sh" ]
