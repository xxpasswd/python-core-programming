#coding=utf-8

import os

for i in ('/tmp',):
    if os.path.isdir(i):
        break
else:
    print("no such directory!")

print(os.getcwd())

os.chdir(i)
print("****Current directory is:")
print(os.getcwd())

print("****Creat temporary directory")
os.mkdir('example')

os.chdir('example')
print("****Current directory:")
print(os.getcwd())

print("****Orignal directory listing:")
print(os.listdir(os.getcwd()))

print("****Creat test file")
f = open('test','w')
f.write('good\nworld\n')
f.close()

print("****Updated directory listing:")
print(os.listdir(os.getcwd()))

print("****Rename test to filetest")
os.rename('test','filetest')

path = os.path.join(os.getcwd(),os.listdir(os.getcwd())[0])
print("****Full file pathname")
print(path)

print("****(pathname,basename)")
print(os.path.split(path))

print("****(filename,extension)")
print(os.path.splitext(os.path.basename(path)))

print("****file basename")
print(os.path.basename(path))

print("****Display file content:")
f = open(path,'r')
for eachline in f:
    print(eachline,)

f.close()

print("****Delete filetest")
os.remove(path)

print("****Upatated directory listing:")
print(os.listdir(os.getcwd()))

os.chdir(os.pardir)
print(os.getcwd())
os.rmdir('example')
print("****Done")