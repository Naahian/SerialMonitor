from serialmonitor import SerialMonitor
import time

sm = SerialMonitor(9600, 'COM4')
print(f"available ports: ", end='')
sm.checkPorts()

print(f"selected baudrate: {sm.baudrate}")
print(f"selected port: {sm.port}")
time.sleep(3)


@sm.stream
def handleEvents():
    print(f"Is currently reading serial: {sm.isStreaming}")

    # as it named, reads serialData
    print(sm.serialData)
    # convert serialData to jsonData, if serial data is json string
    print(sm.jsonData)

    # assuming the serialData is {"distance":161.896}
    distance = sm.jsonData["distance"]
    print(f"distance is {distance}")
    # time.sleep(1) #use if your arduino code has small delay
from serialmonitor import SerialMonitor
import time

print(f"available ports: ", end='')
SerialMonitor.checkPorts()

sm = SerialMonitor(9600, 'COM3')

print(f"selected baudrate: {sm.baudrate}")
print(f"selected port: {sm.port}")
# time.sleep(3)   #just a delay


@sm.stream
def handleEvents():
    print(f"Is currently reading serial: {sm.isStreaming}")

    # as it named, reads serialData
    print(sm.serialData)
    # convert serialData to jsonData, if serial data is json string
    jsonData = sm.getJsonFormat()

    # assuming the serialData is like: {"distance": 161.896}
    distance = jsonData["distance"]
    print(f"distance is {distance}")
    # time.sleep(1) #use if your arduino code has small delay