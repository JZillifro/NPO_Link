FROM node:10.11.0

ARG app_env
ENV APP_ENV $app_env

WORKDIR /usr/frontend
COPY package*.json /usr/frontend/

COPY . /usr/frontend

CMD npm install

CMD if [ ${APP_ENV} = production ]; \
	then \
	npm install -g http-server && \
	npm run build && \
	cd build && \
	hs -p 3000; \
	else \
	npm start; \
	fi

EXPOSE 3000
