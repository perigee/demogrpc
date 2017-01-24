FROM python:3.5-slim


ARG http_proxy
ARG https_proxy
ARG no_proxy

ENV http_proxy $http_proxy
ENV https_proxy $https_proxy
ENV no_proxy $no_proxy


WORKDIR /opt/hello/python
ADD requirements.txt /opt/hello/python/requirements.txt
RUN pip install -r requirements.txt


EXPOSE 3000
#ENTRYPOINT["python", "server.py"]

