#/bin/sh
# run this once, it'll detach and run, over reboots, until stopped 
docker run -d --privileged --restart=unless-stopped --name=pycec --net=host "local/pycec"

