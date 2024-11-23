# Py_Serial_Montior
It's a pyserial made easy. Rather than using bunch of tedious code to initiate, run and to manipulate serial data, just use a decorator to manage realtime serialData from serial port.<br/>

### Usage
(only tested in Windows)
```python
from serialmonitor import SerialMonitor

sm = SerialMonitor(9600, 'COM4')

@sm.stream
def handleEvents():
    #your code goes here
```
### Documentation
- `SerialMonitor.checkPorts()` (static method) prints available ports
- `.isStreaming` returns true if reading serial
- `.getJsonFormat()` returns converted to dict()
- `.serialData` returns serial data
- all other `pyserial` methods.(since child class of pyserial)
<br>
see "example.py" for detail.

