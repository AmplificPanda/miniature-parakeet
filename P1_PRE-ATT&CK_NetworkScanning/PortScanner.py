#!/usr/bin/python3 
#the above specifies which interpreter will be used to run the script.

from distutils.log import error
from scapy.all import *
import pyfiglet #for fancy graphics
import sys #handling exceptions
import socket #use for port, internet and more
from datetime import datetime #for banner to print date and time

#--------------------------------
#--------------------------------

#----------------------------------
#What is a port scanner?
#Imagine a server which is hosting a web server on port 80, ssh on port 22, and ftp on port 21
#However an attacker does not know that the server is hosting these services, 
#thus we use a port scanner to find these open ports on the server
#-----------------------------------

#------------------------------------
#Functionality: 
# 1) Allow user to specify target
# 2) Make requests to every port
# 3) Return open ports
#-------------------------------------

#THE TCP THREE WAY HANDSHAKE IS AS FOLLOWS:
# Client sends SYN to server, server sends SYN-ACK, client sends ACK

#Create banner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

#allow user to specify target IP
target = input(str("Enter target IP: "))

#now run through every port possible on the target IP
try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)

        #return the open ports
        results = s.connect_ex((target,port))

        if results == 0:
            #if 0 that means connection success
            print("{} is open".format(port))
        s.close() #close the socket

except KeyboardInterrupt:
    print("Keyboard interupt, exiting now...")
    sys.exit()

except socket.error:
    print("host not responding")
    sys.exit()