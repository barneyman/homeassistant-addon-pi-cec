from pycec.cec import CecAdapter
from pycec.network import HDMINetwork, PhysicalAddress
from pycec.tcp import TcpAdapter
import time
import datetime

initialised=False
devices=[]

def test_ha(host,display_name):

    adapter = TcpAdapter(host, name=display_name, activate_source=False)
    hdmi_network = HDMINetwork(adapter, loop=None)


    def _new_device(device):
        global devices
        devices.append(device)
        # name is the only thing valid at this point
        print("{} New device {}".format(datetime.datetime.now(), device.name))

    def _device_removed(exit_device):
        global devices
        devices=[device for device in devices if device.name != exit_device.name]
        print("{} remove device {} {}".format(datetime.datetime.now(), exit_device.name, exit_device.type_name))


    hdmi_network.set_new_device_callback(_new_device)
    hdmi_network.set_device_removed_callback(_device_removed)
    
    def _initialised():
        global initialised
        initialised=True
    
    hdmi_network.set_initialized_callback(_initialised)

    hdmi_network.start()

    while not initialised:
        pass

    while True:
        for device in devices:
            print("{} device {} type {} state {}".format(datetime.datetime.now(), device.name,device.type_name,"ON" if device.is_on else "OFF"))
        time.sleep(120)


test_ha("hassio","rubble")
