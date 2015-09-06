docker run -it --rm -v "$PWD":/config-dir --volumes-from rates --net="container:elasticsearch" logstash logstash -f /config-dir/logstash.conf
