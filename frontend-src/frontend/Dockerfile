FROM node:10.11.0

ARG app_env
ENV APP_ENV $app_env

WORKDIR /usr
COPY package*.json /usr/

RUN npm install
RUN npm install -g http-server --silent
RUN npm install -g react-scripts@1.1.5 --silent
ENV PATH /usr/node_modules/.bin:$PATH

WORKDIR /usr/frontend
COPY . /usr/frontend

EXPOSE 3000
ENTRYPOINT [ "npm", "start" ]
