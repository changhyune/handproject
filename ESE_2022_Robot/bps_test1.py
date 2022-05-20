from bluepy import btle
from bluepy.btle import AssignedNumbers

import struct
import binascii
import time

    

class MyDelegate(btle.DefaultDelegate):
    def __init__(self, handle):
        self.start_t = time.time()
        btle.DefaultDelegate.__init__(self)
        self.handle = handle
        print("Created delegate for handle", self.handle)
        # ... more initialise here

    def handleNotification(self, cHandle, data):
        if(cHandle == self.handle):
            #print("handleNotification for handle: ", cHandle, "; Raw data: ", data) #  binascii.b2a_hex(data)
            #Found somewhere. Not tested is this working, but leave here as decode example
            val = binascii.b2a_hex(data)
            val = binascii.unhexlify(val)
            # print("time:", time.time()-self.start_t)
            # self.start_t = time.time() 
            val = struct.unpack('<i', val)[0]
            print(val)

print("Connecting...")
dev = btle.Peripheral("56:ec:8a:8c:21:5d")

try:
    print("Device services list:")
    for svc in dev.services:
        print str(svc)


    HRService = dev.getServiceByUUID("6e400001-b5a3-f393-e0a9-e50e24dcca9e")
    print("HRService", HRService)

    print("HRService characteristics list: ")
    for char in HRService.getCharacteristics():
        print("HRService char[", char.getHandle(), "]: ", char)

    x_ACC = HRService.getCharacteristics("6e400002-b5a3-f393-e0a9-e50e24dcca9e")[0] #Notice! Check is characteristic found before usage in production code!
    y_ACC = HRService.getCharacteristics("6e400003-b5a3-f393-e0a9-e50e24dcca9e")[0] #Notice! Check is characteristic found before usage in production code!
    z_ACC = HRService.getCharacteristics("6e400004-b5a3-f393-e0a9-e50e24dcca9e")[0] #Notice! Check is characteristic found before usage in production code!

    # Assign delegate to target characteristic
    dev.setDelegate(MyDelegate(x_ACC.getHandle()))
    # dev.setDelegate(MyDelegate(y_ACC.getHandle()))
    # dev.setDelegate(MyDelegate(z_ACC.getHandle()))
    
    # We need to write into org.bluetooth.descriptor.gatt.client_characteristic_configuration descriptor to enabe notifications
    # to do so, we must get this descriptor from characteristic first
    # more details you can find in bluepy source (def getDescriptors(self, forUUID=None, hndEnd=0xFFFF))
    desc_x = x_ACC.getDescriptors(AssignedNumbers.client_characteristic_configuration)
    # desc_y = y_ACC.getDescriptors(AssignedNumbers.client_characteristic_configuration)
    # desc_z = z_ACC.getDescriptors(AssignedNumbers.client_characteristic_configuration)

    # print("Writing \"notification\" flag to descriptor with handle: ", desc[0].handle)
    dev.writeCharacteristic(desc_x[0].handle, b"\x01\x00")# Notice! Do not use [0] in production. Check is descriptor found first!
    # dev.writeCharacteristic(desc_y[0].handle, b"\x01\x00")# Notice! Do not use [0] in production. Check is descriptor found first!
    # dev.writeCharacteristic(desc_z[0].handle, b"\x01\x00")# Notice! Do not use [0] in production. Check is descriptor found first!

    print("Waiting for notifications...")

    while True:
        if dev.waitForNotifications(0.03):
            # handleNotification() was called
            continue

finally:
    dev.disconnect()