import os
file='C:\\e'
x=10
for a in range(x):
    os.mkdir(file)
    smfile=open(file+'\\e.txt','w+')
    smfile.write("Hello __ ________")
    smfile.close()
    file+='\\e'
os.mkdir(file)
myfile=open(file+'\\e.txt','w+')
myfile.write("Password is 12345")
myfile.close()
file+='\\e'
for a in range(x):
    os.mkdir(file)
    smfile=open(file+'\\e.txt','w+')
    smfile.write("Hello __ ________")
    smfile.close()
    file+='\\e'
