#!/usr/bin/python3 
#the above specifies which interpreter will be used to run the script.
from scapy.all import *
#--------------------------------
#Using Scapy library for a Network scan
#Reworked from prior programme which did not work.
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

#Get user inputs
try:
    host = (input("Please enter a host address: "))
    #get list of ports as input, split using , character
    portString =  (list(input("Please enter the ports to check: ").split(",")))
    #print(ports) //testing the input

    #convert the ports into integers...map function takes whats in port, and converts to int but stores as map obj
    #maps the input string to ints
    temp = map(int,portString)
    #to store as list, use list operator on it
    ports = list(temp)
    
    print("Scanning...")
    ans, unans = sr(IP(dst=host)/TCP(dport=ports,flags="S"),verbose=0, timeout=2)
    print(ans)

    for (s,r) in ans:
        print("{} open".format(s[TCP].dport))

except(ValueError, TypeError, RuntimeError, NameError):
    print("An error occurred...")