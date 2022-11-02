

import os
print(os.getcwd()) # returns current directiroy path


f=open("test.txt")  #open ->built-in function

print(f)


f=open("test.txt","r+")
print(type(f))
f.close()

with open("test.txt","r") as f:
    print("file is open")
    print(type(f))

####################################################
f=open("test.txt","w")

f.write("this is a test \n")
f.write("this is a second test \n")

f.close()

with open("test.txt","w") as f:
    for i in range(10):
        f.write("Nums : {}".format(i))

f.close()

with open("test.txt","a+") as f:
    f.write("addition operation \n")
    for i in range(10):
        f.write(i)
############################


with open("test.txt","w") as f:
    
    while True:
        textVar =input("Give a word")
        if textVar=="exit":
            break
        f.write(textVar+"\n")
        
###################################

with open("test.txt","r+") as f:
    s =f.read(6) #number of chraracters needs to be read from file
    print(s)
    
#############################################

with open("main.py","r+") as f:
    while True:
        s =f.read(5)
        if s=="":
            break
        print(s,end="")