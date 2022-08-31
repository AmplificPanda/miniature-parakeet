#!/usr/bin/python
from struct import pack
from scapy.all import *

#This program is a basic packet viewer which allows you to view 
#the contents of a http packet stream (cap) and shows some notes on its
#functionality. Designed to understand the scapy library at a basic level.
#Part of the PRE-ATT&CK Network scanning segment of MITRE.

#---------------------------------------------------------------------#
#python -m venv venv - to make a virtual environment
#pip install sklearn - sklearn/any other libary to install to venv
#pip freeze > requirements.txt - to see what libraries are installed and create/update
#the requirements.txt file.

#Note: Default terminal set to CMD via Command Pallete --> Select Terminal: Select Default Profile
#---------------------------------------------------------------------#
print('\n\n')
print("Program successfully started \n")

#read a .cap file and assign it to packet variable (simple http connection)
packet = rdpcap('P1_PRE-ATT&CK_NetworkScanning\http.cap') 

#packet holds a collection of different packets...
#we can see this through print(packet)

#assign variable and read the first packet 
print("Contents of packet[0] shown below: ")
p = packet[0]
p.show() #show the packet data

#if we want to see some actual data, we need to look at the 4th packet in this capture
o = packet[3]
print("\n 4th Packet contains:")
o.show()
#we can see that an ethernet packet wrapping an ip packet wrapping a tcp packet
#however we have a raw section carrying the payload, a http packet.

#Demonstration: We can send a packet somewhere else
print("\n Modifying the packet to send to port 8080:")
o[TCP].dport = 8080
o.show() #we can see that the dport has changed to port 8080
#Note: Scapy is meant to recognize 8080 is a http-alt port

#We can also build packets using this library

#Create a bare-bones TCP IP packet
print("\n bare-bones TCP IP packet")
y = IP(dst="8.8.8.8")/TCP(dport=53)
y.show() #show contents of created packet

#we can also modify it further
print("\n Modified packet where we have wrapped it into a UDP wrapped as DNS packet:")
y=IP(dst="8.8.8.8")/UDP(dport=53)/DNS()
#y[TCP].dport = 35 #change the port
y.show() #show packet contents of the packet we have just modified.