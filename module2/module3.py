import telnetlib
from time import sleep
import pdb
import socket
def differnces(x, y):
    try:
        ch = telnetlib.Telnet(x,y)
        sleep(1800)
        tp = ch.write("HI")
        tpl = ch.sock.send("Hi")
        pdb.set_trace()
        return tpl
    except Exception, e:
        pdb.set_trace()
