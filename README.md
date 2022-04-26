# Raspberry Pi CEC server add-on

Starting from [HomeAssistant](https://www.home-assistant.io) 2021.7.0, the CEC
libraries included in HomeAssistant do no longer support CEC interfaces that are
not included in the Linux kernel itself. Therefore, it is no longer possible to
control the HDMI-CEC bus through the [hdmi-cec](https://www.home-assistant.io/integrations/hdmi_cec/) integration alone.

However, the hdmi-cec integration supports talking to an HDMI-CEC device over
a TCP socket. This add-on launches a HDMI-CEC server which supports the
Raspberry Pi hardware interface.

## Installation

Please refer to [Installing 3rd Party Addons](https://github.com/home-assistant/hassio-addons-example) and add 
my [parent repository](https://github.com/barneyman/ha-addons) for this repo 

## Configuration

After enabling this add-on and configuring it
to automatically start, one can use the following in HomeAssistant `configuration.yaml`:

```yaml
hdmi_cec:
  host: ffa7b53e-pi-cec
```

and restart HomeAssistant. You should then be able to control your HDMI-CEC devices
with the integration commands.

## Notes



For the curious, `ffa7b53e` is the [SHA-1](https://en.wikipedia.org/wiki/SHA-1) hash
of the string `https://github.com/barneyman/ha-addons` and is computed
from the repository name by HomeAssistant.

The icon is part of [iconscount display icon](https://iconscout.com/icon/display-171) collection.

## RPI GPU Memory

The libraries that pycec uses require there be 128M of memory allocatd to the GPU - if you see any
strange assertions in the logs, use `raspi-config` to change that value.

# Using the docker file as a remote

If you want to use just the dockerfile, ie not as an HA add-on, on a remote HDMI, follow this (it's
RPI specific but adapt as required

* Burn a lite version of Buster, using the Raspberry Imager
  * Give it a sensible name, wifi creds & enable SSH
* SSH to it
* update it
  * `sudo apt update && sudo apt upgrade && sudo apt install git`
* install docker
  * `curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh`
* add yourself to the docker group
  * `sudo usermod -aG docker $USER`
* Log out, log in (for the OS to re-eval your new group membership)
* Clone my fork (specifically for my 'helper' shell scripts)
  * `git clone https://github.com/barneyman/homeassistant-addon-pi-cec.git && cd homeassistant-addon-pi-cec`
* build the docker image - this will take a 'a cup of tea'
  * `sh ./build.sh`
* disable DRM VC4 V3D driver in `/boot/config.txt` (pycec needs `tvservice` which this driver disables)
  * `sudo nano /boot/config.txt` - find `Enable DRM VC4 V3D driver` and comment out that section
* while in that file, turn off the 'rpi switches TV input when it reboots' by adding `hdmi_ignore_cec_init=1` 
* reboot
* log back in, `cd homeassistant-addon-pi-cec`
* run the test - you may see a few deprecation warnings but no assertions or strange behaviour
  * `sh ./runtest.sh` 
* edit your `configuration.yaml`
  * add an `hdmi_cec` section with a `host` entry (details in my repo `Readme.md`, the host is your rpi hostname)
* restart your HA
* you should now have a bunch of `switch.hdmi_?` entities
* when you're happy that's worked, kill the `runtest.sh` above execute `run.sh` which will make it persistent across boots
  * beware! HA will vomit errors when pycec disappears, another reboot of HA won't hurt



