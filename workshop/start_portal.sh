#!/bin/bash
docker run -d -p 8888:8888 \
  --name portal \
  --volumes-from portal_data \
  --link mocked_rates:rates \
  workshop/portal
