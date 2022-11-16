import time
import sys
import ibmiotf.application
import ibmiotf.device
import random

organization = "9y2uod"
deviceType = "Microcontroller"
deviceId = "1407"
authMethod = "token"
authToken = "9585786415"



try:
    deviceOptions = {"org":organization,"type":deviceType,"id": deviceId,"auth-method":authMethod,"auth-token":authToken}
    deviceCli = ibmiotf.device.Client(deviceOptions)

except Exception as e:
    print("Caught exception connecting device: %s" % str(e))
    sys.exit()

deviceCli.connect()



def publish(data):
    def myOnPublishCallback():
        print("Published data: %s", data)
        
    success = deviceCli.publishEvent("micro_event","json",data,qos=0,on_publish=myOnPublishCallback) #uploading data onto the IBM IoT Platform...
    if not success:
        print("Not connected to IoTF")

while True:
    data = {'name' : 'Vaigai EXP', 'lat' : 13.0480438,'long' : 79.9288083}#Chennai
    publish(data)
    time.sleep(5)

    data = {'name' : 'Pandiyan EXP', 'lat' : 72.7410979,'long' : 72.7410979}#Mumbai
    publish(data)
    time.sleep(5)

    data = {'name' : 'Pothigai EXP', 'lat' : 22.6763858,'long' : 88.0495278}#Kolkata
    publish(data)
    time.sleep(5)

    data = {'name' : 'Pearl City EXP', 'lat' : 28.6443981,'long' : 76.8130326}#Delhi
    publish(data)
    time.sleep(5)

    data = {'name' : 'Kollam EXP', 'lat' : 9.9179987,'long' : 78.0527826}#Madurai
    publish(data)
    time.sleep(5)
    
deviceCli.disconnect()
