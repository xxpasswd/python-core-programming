#coding=utf-8

# 分别用递归和迭代求菲波那切数列
def digui(a):
    if a ==1:
        return 1
    elif a==2:
        return 1
    else:
        return digui(a-1)+digui(a-2)

def diedai(b):
    i =3
    m = 1
    n = 1
    while i<b+1:
        a = n
        n=n+m
        m = a
        i += 1
    return n

# 贪心算法实现TSP问题
def tsp():
    distance = {'AB':2,'AC':6,'AD':5,'BA':2,'BC':4,'BD':4,'CA':6,'CB':4,'CD':2,'DA':5,'DB':4,'DC':2}
    for i in 'ABCD':
        site = ['A', 'B', 'C', 'D']
        short = []
        while True:
            tmp = 100
            site.remove(i)
            if site:
                for j in site:
                    if distance[i+j]<tmp:
                        tmp = distance[i+j]
                        key = i+j
                else:
                    short.append(key)
                    i = key[1]
            else:
                short.append(i+short[0][0])
                break

        print(short,sum(distance[x] for x in short))


# 递归求全排列
full = ''
count = 0
def full_permutation(s):
    global full,count
    if len(s)>1:
        for i in s:
            tmp = full
            full = full+i
            num = s.index(i)
            s.remove(i)
            full_permutation(s)
            s.insert(num,i)
            full = tmp
    if len(s)==1:
        tmp = full
        full = full + s[0]
        print(full,count)
        count += 1
        full = tmp

def full_permutation2(s,begin,end):
    if begin >= end:
        print(s)
    else:
        num = begin
        for i in range(begin,end):
            s[num],s[i] = s[i],s[num]
            full_permutation2(s,begin+1,end)
            s[i],s[num] = s[num],s[i]




# 递归实现不确定层循环
# def recur(n):
#     if n >0:
#         for i in range(...):
#             recur(n-1)
#     else:
#         pass

# 一个求所有组合的例子
allperm = ''
m = 0
def all(string,n):
    global m
    if n>1:
        global allperm
        for i in string:
            tmp = allperm
            allperm = allperm + i
            all(string, n-1)
            allperm = tmp
    else:
        for i in string:
            tmp = allperm
            print(m,)
            print(allperm+i)
            m += 1
            allperm = tmp

full_permutation('abcde')