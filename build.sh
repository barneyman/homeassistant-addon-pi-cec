#/bin/sh
docker build --target=consumer --build-arg BUILD_FROM=alpine -t "local/pycec" .
