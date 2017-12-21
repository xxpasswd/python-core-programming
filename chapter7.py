#coding=utf-8

import random

# 7-3
def dict_sort():
    dictionary = dict(zip(('w','x','a','f','g'),(1,2,3,4,5,)))

    print("按顺序打印键")
    for i in sorted(dictionary):
        print(i)

    print("按键顺序打印键和键值")
    for i in sorted(dictionary):
        print(i,dictionary[i])

    print("按值顺序打印键和值")
    dic = sorted(dictionary.items(),key=lambda d:d[1])
    for i,j in dic:
        print(i,j)

# 7-4
def creat_dict():
    list1 = [1,2,3,4,5]
    list2 = ['qaz','wsx','edc','rfv','tgb']
    dic = {}
    for i in range(len(list1)):
        dic[list1[i]]=list2[i]
    print(dic)


# 7-6
def stock():
    all = []
    all_dict = {}
    while True:
        data = input("Input your data:  ").split()
        if data:
            all.append(data)
        else:
            break

    column = int(input("Enter a main column "))
    for i in all:
        all_dict[i[column-1]] = i[:column-1]+i[column:]

    keys = all_dict.keys()

    for i in sorted(keys):
        print(i,all_dict[i])

# 7-7
def reverse_dict():
    dictionary = {2:'a',3:'d',1:'c',5:'y'}
    reverse_dict = {d[1]:d[0] for d in dictionary.items()}
    print(reverse_dict)

# 7-8
def employee():
    all = {}
    while True:
        data = input("Inpur employee name and number  ").split()
        if data:
            all[data[0]] = data[1]
        else:
            return all
            break

def showmenu():
    all = employee()
    key = input("1.按照姓名输出，2.按照编号输出  ")
    if key == '1':
        for i in sorted(all):
            print(i,all[i])
    else:
        all2 = sorted(all.items(),key=lambda k:k[1])
        for i,j in all2:
            print(j,i)

# 7-9
def tr(srcstr,desstr,string):

    dicta = dict(zip(srcstr.lower(),desstr))
    aa = {}.fromkeys(srcstr[len(desstr):])
    dicta.update(aa)
    my_string = []
    for i in string:
        if i in dicta:
            my_string.append(dicta[i])
        else:
            my_string.append(i)

    my_string = [i for i in my_string if i]
    print(''.join(my_string))

# 7-10
def rot13():
    low_string = {chr(x):chr(x-13) for x in range(110,123)}
    low_string2 = {chr(x):chr(x+13) for x in range(97,110)}
    low_string.update(low_string2)
    upper_string = {chr(x):chr(x-13) for x in range(78,91)}
    upper_string2 = {chr(x):chr(x+13) for x in range(65,78)}
    upper_string.update(upper_string2)

    sentence = input("Enter an sentence ")
    rot13_sentence = []
    for i in sentence:
        if i in low_string:
            rot13_sentence.append(low_string[i])
        if i in upper_string:
            rot13_sentence.append(upper_string[i])
        else:
            rot13_sentence.append(i)

    print(''.join(rot13_sentence))

# 7-13 7-14
def rand_set():
    tmp = []
    for i in range(random.randint(0,9)):
       tmp.append(random.randint(0,9))
    A = set(tmp)
    tmp = []
    for i in range(random.randint(0,9)):
        tmp.append(random.randint(0,9))
    B = set(tmp)

    print("A",A)
    print("B",B)
    ans = input("Input your answer for A|B  ").split()
    ans = set(map(int,ans))
    print(ans)
    if ans == A|B:
        print("good,you are right")
    print("A|B",A|B)
    print("A&B",A&B)
    print("A-B",A-B)
    print("B-A",B-A)
    print("A^B",A^B)



if __name__ == '__main__':
    rand_set()