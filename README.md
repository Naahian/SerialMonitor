##pyserial made easy\n
[under dev.] just use a decorator to manage realtime serialData from serial port.\n
available features:\n
`sm.checkPorts()` prints available ports\n
`sm.baudrate` returns selected baudrate\n
`sm.port` returns selected ports\n
`sm.isStreaming` returns true if reading serial\n
`sm.jsonData` returns converted to dict()\n
`sm.serialData` returns serial data\n
\n
(only tested in windows)
```python
from serialmonitor import SerialMonitor

sm = SerialMonitor(9600, 'COM4')

@sm.stream
def handleEvents():
    #your code goes here
```
