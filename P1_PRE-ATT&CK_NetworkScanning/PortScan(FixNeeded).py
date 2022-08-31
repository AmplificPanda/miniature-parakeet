#!/usr/bin/python 
#the above specifies which interpreter will be used to run the script.
from scapy.all import *
#--------------------------------
#Using Scapy library for a Network scan
#This has some errors preventing it from actually running... Perhaps libraries have been updated
#Thus a better scanner will be coded at a later date. OR this may run in Linux fine.
#--------------------------------

#ports we are going to look at
ports = [25,80,53, 123, 443,445,8080,8443] #common well known ports

#perform a syn and look for corresponding ack packet..half connection
#iterate over the specified ports above and inform us which ports are open or closed.
def synScanner(host):
    #sr = send a packet and wait to receive a packet
    #build IP packet wrapped in TCP, dst = target system, in this case host
    #specifying source port helpful if we want to perform traffic analysis/using wireshark
    #dport = specifies the destination TCP port we are scanning.
    #flags = S = packets specified to be a SYN packet
    #timeout = 2 wait 2 seconds before timeout = no response = port closed
    #verbose=0 : sr provides a lot of info, we just want the results of sr (packets answered & not)
    #closed ports will be set to noreply.
    
    reply,noreply = sr(IP(dst=host)/TCP(dport=ports,flags="S"), timeout=2, verbose=0)
    
     #output the responses
    print("\n ", reply)

    print("The open ports at specified host: %s:" % host)

    #loop through the answered packets
    for(s,r) in reply: 
        #verify appropiate response: at the TCP layer of the source port of the sent packet equals the 
        #destination port of the recieved packet.
        print(s[TCP].dport)
        if s[TCP].dport==r[TCP].sport:
            #print which ports are open 
            print(s[TCP].dport) 

#---------------------------
#it appears that the SYN packet may be being filtered at the network level as this is done through
#a university network...may work on a VPN? Testing on Auckland VPN resulted in same fail.

#testing for a particular application listening on a particular port
def DnsScan(host): 
    #connect to a specified port on a specified host and see if it responds to a DNS request
    #in this case, target is Google DNS server, requesting google.com...
    #send and receive the packet, build packet...UDP layer inside IP layer, port 53 for DNS...
    #there are no flags in UDP...add additonal DNS layer, build valid DNS packet, rd = 1 request,
    #DNSquery = google.com
    ans, unans = sr(IP(dst=host)/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="google.com")),timeout=2, verbose=0)
    if ans:
        print("DNS server detected at %s" %host)

synScanner(host="8.8.8.8")
DnsScan(host="8.8.8.8")

#Note that telnet is very unsecure as it is unencrypted text messages (blocked by many things)
#Telnet runs on port 23