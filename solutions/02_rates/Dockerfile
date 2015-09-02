FROM ubuntu
RUN apt-get update 
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python python-setuptools
RUN easy_install web.py
COPY rates rates
CMD ["python", "-u", "rates/server.py"]
EXPOSE 8080
