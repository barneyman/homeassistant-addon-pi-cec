#/bin/sh
docker build --build-arg BUILD_FROM=alpine:3.20 -t "local/pycec" .
