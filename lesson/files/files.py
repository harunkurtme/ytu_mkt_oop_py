

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