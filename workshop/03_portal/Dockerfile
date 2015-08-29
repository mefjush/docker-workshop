FROM ubuntu
RUN apt-get update 
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python easy_install
RUN easy_install web.py
COPY portal portal
CMD python portal/server.py
