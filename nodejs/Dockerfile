FROM node:7.4


ARG http_proxy
ARG https_proxy
ARG no_proxy

ENV http_proxy $http_proxy
ENV https_proxy $https_proxy
ENV no_proxy $no_proxy

ADD . /opt/hello/nodejs


WORKDIR /opt/hello/nodejs
RUN mkdir -p /opt/app && cp package.json /opt/app/package.json

WORKDIR /opt/app
RUN npm install

WORKDIR /opt/hello/nodejs

EXPOSE 3000


