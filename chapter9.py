#coding=utf-8

import os

# 9-1
def filter():
    filename = input("Enter file name  ")
    fobj = open(filename,'r')
    for i in fobj:
        if i.strip():
            if i.strip()[0] == '#':
                continue
            print(i)

    fobj.close()

# 9-2
def fileAccess():
    filename = input("Enter file name  ")
    lines = int(input("Enter line numbers  "))
    fobj = open(filename,'r')
    i = 1
    while i <= lines:
        print(fobj.readline())
        i += 1

    fobj.close()

# 9-3
def lineNumber():
    filename = input("Enter file name  ")
    fobj = open(filename,'r')
    print(len(fobj.readlines()))
    fobj.close()

# 9-4
def fileread():
    n = 0
    filename = input("Enter file name  ")
    fobj = open(filename,'r')
    for i in fobj:
        print(i)
        n += 1
        if n%25 ==0:
            os.system('pause')
    fobj.close()

# 9-6
def findDiff():
    f1 = input("Enter file name  ")
    f2 = input("Enter file name  ")
    f1obj = open(f1,'r')
    f2obj = open(f2,'r')
    f1_text = f1obj.readlines()
    f2_text = f2obj.readlines()
    line = min(len(f1_text),len(f2_text))
    for i in range(line):
        if not f1_text[i]==f2_text[i]:
            print(i)
            break

    else:
        if len(f1_text) == len(f2_text):
            print("two file equal")

# 9-8
def moudleAtrr():
    name = input("Enter moudle name  ")
    moudle = __import__(name)
    print("Moudle name is %s" % name)
    # print("Moudle type is $s" % type(getattr(moudle,name)))
    print(dir(moudle))

# 9-9
num =1
def scanpydoc():
    # python 文件路径
    doc_path = '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7'
    all_py = [x for x in os.listdir(doc_path) if x.endswith('py')]
    file = open('aa','w')
    for j in all_py:
        global num
        path = os.path.join(doc_path,j)
        print(j)
        file.write('\n'+str(num)+j+'\n')
        num += 1
        fobj = open(path,'r')
        content = fobj.readlines()
        doc = False
        bracket = True
        for i in content:
            if i.strip().startswith('def'):
                print(i)
                file.write(i)
                if i.strip().endswith('):'):
                    bracket = True
                else:
                    bracket = False
            elif not bracket:
                print(i)
                file.write(i)
                if i.strip().endswith('):'):
                    bracket = True

            elif i.strip().startswith('class'):
                print(i)
                file.write(i)
            elif (i.strip().startswith('"""') or i.strip().startswith('r"""'))\
                    and i.strip().endswith('"""') and len(i.strip()) >6:
                print(i)
                file.write(i)
            elif doc:
                print(i)
                file.write(i)
                if i.strip().endswith('"""'):
                    doc = False
            elif i.strip().startswith('"""') or i.strip().startswith('r"""'):
                print(i)
                file.write(i)
                doc = True
        fobj.close()
    file.close()

if __name__ == '__main__':
    scanpydoc()