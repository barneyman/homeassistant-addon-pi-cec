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
