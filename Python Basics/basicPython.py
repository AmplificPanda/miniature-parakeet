#!/usr/bin/python3
import os, glob

#Basic loop to go from 1-10
print("\n For loop: \n")
for i in range(1,11):
    print(i)

#basic while loop to go from 1-10
print(" \n While loop \n")
i = 1
while i<=10:
    print(i)
    i+=1

#basic if else statements
print("\n if and elif statements:")
a=30
c=12
if a<c:
    print("{} is less than {}".format(a,c))
elif a==40:
    print("{} is equal to {}".format(a,40))
else:
    print("{} is greater than {}".format(a,c))

#--------using the glob and os libraries
print("\n\n using the glob and os library to look for files in a directory")
#check specified directory in this case the downloads directory
os.chdir("C:/Users/Avian/Downloads")
#check for png files within this directory
for file in glob.glob("*.png"):
    print(file)
#from here we could move these to a different directory etc.

#Fizz buzz implementation
#for the range of numbers from 0 to 100:
print("\n\n Fizz buzz implementation but only with fizz buzz")
for num in range(1,101):
    if num % 5 == 0 and num % 3 == 0:
        print("Fizz buzz")
    else:
        print(num)

