import json
import serial
import serial.tools.list_ports

#TODO: write Data to serial

class SerialMonitor(serial.Serial):
    def __init__(self, baudrate:int, port:str):
        super().__init__()
        self.baudrate = baudrate
        self.port = port
        if(not self.is_open): self.open()
        self.isStreaming = False
        self.serialData = ""
    
    def checkPorts():
        ports = serial.tools.list_ports.comports()
        for port in ports:
            print(port.device)

    def stream(self, func):
        self.isStreaming = True
        self.flushInput()
        def inner(*args, **kwargs):
            while self.isStreaming:
                #removes decode error due to parity bytes at start
                try:
                    self.serialData = self.readline().decode()
                except UnicodeDecodeError:
                    self.serialData = self.readline().decode()

                func(*args, **kwargs)
                self.flushInput()
        inner()

    def getJsonFormat(self):
        try:
            return json.loads(self.serialData)
        except:
            print("Convertion Error: serialData might not be json string.")
