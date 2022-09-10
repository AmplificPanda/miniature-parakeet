#!/usr/bin/python

#This is for the DNS Exploration segment in Week 2
#----------------------------------------------------
#for python reading from a textfile:
#https://www.pythontutorial.net/python-basics/python-read-text-file/
#----------------------------------------------------
#set up target domain:
domain = "www.google.com"
searchlist = "subdomains.txt"

#create empty dictionary to hold all the subs within the txt file
dictionary = [] 

#read mode 
with open(domain,"r") as f:
    dictionary = f.read().splitlines()

def DomainSearcher():
    print("To implement")

DomainSearcher(domain,dictionary,True)