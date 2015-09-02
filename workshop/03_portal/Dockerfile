FROM ubuntu
RUN apt-get update 
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python python-setuptools
RUN easy_install web.py
COPY portal portal
WORKDIR portal
CMD ["python", "-u", "server.py", "8888"]
EXPOSE 8888
