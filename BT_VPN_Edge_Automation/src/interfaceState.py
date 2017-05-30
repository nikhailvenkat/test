from utils import *
from Device import Device
import telnetlib
def interfaceState():
	R = Device('R2')
	RTelnet = telnetlib.Telnet(GET_IP, 23, 60)
	RTelnet.write(GET_USERNAME+"\n")
	RTelnet.write(GET_PASSWORD+"\n")
	
	if verifyInterfaceState(RTelnet, 'lo0', state= "up"):
		return 1
	else:
		return 0
	
	