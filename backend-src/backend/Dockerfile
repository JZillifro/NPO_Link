# base image
FROM python:3.7.0-alpine


ARG app_env
ENV APP_ENV $app_env

# new
# install dependencies
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd

# set working directory
WORKDIR /usr/src/app

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# new
# add entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
COPY ./entrypoint-prod.sh /usr/src/app/entrypoint-prod.sh
RUN chmod +x /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint-prod.sh

# add app
COPY . /usr/src/app

EXPOSE 5000
# new
# run server
CMD if [ ${APP_ENV} = production ]; \
	then \
	/usr/src/app/entrypoint-prod.sh; \
	else \
	/usr/src/app/entrypoint.sh; \
	fi
