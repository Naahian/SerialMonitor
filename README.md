##pyserial made easy
[under dev.] just use a decorator to manage realtime serialData from serial port.
available features:
`sm.checkPorts()` prints available ports
`sm.baudrate` returns selected baudrate
`sm.port` returns selected ports
`sm.isStreaming` returns true if reading serial
`sm.jsonData` returns converted to dict()
`sm.serialData` returns serial data

(only tested in windows)
```python
from serialmonitor import SerialMonitor

sm = SerialMonitor(9600, 'COM4')

@sm.stream
def handleEvents():
    #your code goes here
```
