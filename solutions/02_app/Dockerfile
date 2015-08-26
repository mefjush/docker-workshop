FROM ubuntu
COPY portal portal
RUN apt-get update 
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python easy_install
RUN easy_install web.py
CMD python portal/server.py
