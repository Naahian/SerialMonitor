# Py_Serial_Montior
(under development)<br>
It's a pyserial made easy. Just use a decorator to manage realtime serialData from serial port.<br/>

### Documentation
(only tested in Windows)
```python
from serialmonitor import SerialMonitor

sm = SerialMonitor(9600, 'COM4')

@sm.stream
def handleEvents():
    #your code goes here
```
Features:
- `.checkPorts()` prints available ports
- `.baudrate` returns selected baudrate
- `.port` returns selected ports
- `.isStreaming` returns true if reading serial
- `.jsonData` returns converted to dict()
- `.serialData` returns serial data
<br>
see "example.py" for detail.

