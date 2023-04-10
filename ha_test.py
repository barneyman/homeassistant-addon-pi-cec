from pycec.cec import CecAdapter
from pycec.network import HDMINetwork, PhysicalAddress
from pycec.tcp import TcpAdapter
import time

initialised=False
devices=[]

def test_ha(host,display_name):

    adapter = TcpAdapter(host, name=display_name, activate_source=False)
    hdmi_network = HDMINetwork(adapter, loop=None)


    def _new_device(device):
        global devices
        devices.append(device)
        print("New device {} {}".format(device.name, device.type_name))

    hdmi_network.set_new_device_callback(_new_device)
    
    def _initialised():
        global initialised
        initialised=True
    
    hdmi_network.set_initialized_callback(_initialised)

    hdmi_network.start()

    while not initialised:
        pass

    while True:
        for device in devices:
            print("device {} type {} state {}".format(device.name,device.type_name,"ON" if device.is_on else "OFF"))
        pass
        time.sleep(30)


test_ha("hassio","rubble")
