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
    data = {'name' : 'Vaigai EXP', 'lat' : 17.6387448,'long' : 78.4754336}
    publish(data)
    time.sleep(3)

    data = {'name' : 'Vaigai EXP', 'lat' : 17.6341908,'long' : 78.4744722}
    publish(data)
    time.sleep(3)

    data = {'name' : 'Vaigai EXP', 'lat' : 17.6340889,'long' : 78.4745052}
    publish(data)
    time.sleep(3)

    data = {'name' : 'Vaigai EXP', 'lat' : 17.6248626,'long' : 78.4720259}
    publish(data)
    time.sleep(3)

    data = {'name' : 'Vaigai EXP', 'lat' : 17.6188577,'long' : 78.4698726}
    publish(data)
    time.sleep(3)

    data = {'name' : 'Vaigai EXP', 'lat' : 17.6132382,'long' : 78.4707318}
    publish(data)
    time.sleep(3)
    
   
deviceCli.disconnect()

