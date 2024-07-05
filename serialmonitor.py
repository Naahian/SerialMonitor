import json
import serial
import serial.tools.list_ports


class SerialMonitor:
    def __init__(self, baudrate: int = 115200, port: str = 'COM3'):
        self.port = port
        self.baudrate = baudrate
        self.isStreaming = False
        self.serialData = ""
        self.jsonData = {}
        self.buffer = serial.Serial(self.port, self.baudrate)

    def checkPorts(self):
        ports = serial.tools.list_ports.comports()
        for port in ports:
            print(port.device)

    def stream(self, func):
        self.isStreaming = True

        def inner(*args, **kwargs):
            while self.isStreaming:
                temp = {}
                self.serialData = self.buffer.readline().decode().strip()
                try:
                    temp = json.loads(self.serialData)
                except:
                    print(
                        "SerialMonitor Error: cannot convert to json or serialData is not json string.")

                self.jsonData.update(temp)
                func(*args, **kwargs)
                self.buffer.flushInput()
        inner()
