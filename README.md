##pyserial made easy<br/>
[under dev.] just use a decorator to manage realtime serialData from serial port.<br/>
available features:<br/>
`sm.checkPorts()` prints available ports<br/>
`sm.baudrate` returns selected baudrate<br/>
`sm.port` returns selected ports<br/>
`sm.isStreaming` returns true if reading serial<br/>
`sm.jsonData` returns converted to dict()<br/>
`sm.serialData` returns serial data<br/>
<br/>
(only tested in windows)
```python
from serialmonitor import SerialMonitor

sm = SerialMonitor(9600, 'COM4')

@sm.stream
def handleEvents():
    #your code goes here
```
