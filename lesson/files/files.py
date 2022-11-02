

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

#############################################

with open("test.txt","r+") as f:
    while True:
        s =f.readline()
        if s =='':
            break
        print(s,end='')
        
        
with open("main.py","r+") as f:
    for line in f:
        print(line,end="")

with open("main.py","r+") as f:
    l =list(f)
    print(l)

###########################

with open("test.csv","w+") as f:
    f.write('ali,123\n')
    f.write('ali,123\n')
    f.write('ali,123\n')

d=dict()

with open("test.csv","r+") as f:
    for line in f:
        if line.strip()=="":
            continue
        l = line.split(",")
        d[l[0]]=l[1].strip()
        print(d)


#######################

def writeCSV(path,formatType,num_cols=None,header =False):
    with open(path,formatType) as f:
        f.write("name,IDno,lesson,grade\n")
        f.write("harun,1,cpp,12\n")
        f.write("kamil,3,dynamic,66\n")

    print()

def readCSV(path,formatType,num_cols=None,header =False):
    with open(path,formatType,encoding="utf-8") as f:
        if header:
            headList =f.readline()[:-1].split(",")
        
        l=[]
        for line in f:
            line =line[:-1].split(",")
            
            if line =="":
                continue
            
            if num_cols :
                for n, con_type in num_cols.items():
                    line[n] = con_type(line[n])
            
            l.append(line)
        
            
if __name__ =="__main__":
    writeCSV("student.csv","w+")
    
    l,h=readCSV("student.csv","r+",{3:int, 3 :float})
############################################

# Errors

def foo (a):
    
    print("foo beign")
    if not isinstance(a,int):
        raise TypeError
    
    if a<0:
        raise ValueError
    
try:
    foo(-1)
except ValueError:
    print("value is not okey")
except TypeError:
    print("number is not integer")