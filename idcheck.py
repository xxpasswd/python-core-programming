#coding=utf-8

import keyword
import random
import datetime

# 6-2
def idcheck():
	keywords = keyword.kwlist
	while True:
		key = raw_input("Please input your string  ")
		if key in keywords:
			print "It is a key word,please choose other word"
		else:
			print "It can be used to your variate"

# 6-3
def sequence_sort():
	num = raw_input("Please input numbers  ").split()
	nums = map(int,num)
	return sorted(nums)

def key_sort():
	pass

# 6-5
def compare():
	string1 = raw_input()
	string2 = raw_input()
	for i,j in enumerate(string1):
		try:
			if string2[i] != j:
				print "false"
				break
		except Exception as e:
			print "false"
			break
	else:
		print "True"

def ishas():
    print "Please input two strings:"
    string1 = raw_input()
    string2 = raw_input()
    flag = string1.find(string2)
    if  flag != -1:
        print "true"
    else:
        print "false"
def reverse_copy():
    string = raw_input("Please input your string ")
    string = string + string[::-1]
    print string

def my_strip(string):
    string = raw_input("Input your string   ")
    length = len(string)
    for i in range(length):
        if string[i] != ' ' :
            string = string[i:]
            break

    length = len(string)
    for i in range(-1,-length,-1):
        if string[i] != ' ':
            string = string[:i+1]
            break

    print "the result:",string,".strip()"
    print string

# 6-8
def numtoeng():
    unit = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',
           12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',
           20:'twenty'}
    decades = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}


    num = raw_input("Enter a number  (0<num<1000)  ").lstrip('0')

    if 0<int(num)<21:
        print unit[int(num)]
    elif 20<int(num)<100:
        print decades[int(num[0])]+"-"+unit[int(num[-1])]
    elif 99<int(num)<1000:
        if num[1] == 0 and num[2] == 0:
            print num[0],"hundreds"
        elif 0 < int(num[1:]) < 21:
            print unit[int(num[0])],"hundreds and",unit[int(num)]
        elif 20 < int(num[1:]) < 100:
            print unit[int(num[0])],"hundreds and",decades[int(num[0])] + "-" + unit[int(num[-1])]

# 6-10
def reversal():
    string = raw_input("Enter a string  ")
    print string.swapcase()

# 6-11
def ip_convert():
    key = raw_input("1.binary  2.decimal  ")
    if key == '1':
        ip = raw_input("Enter your IP address of binary ")
        ip_list = ip.split('.')
        if len(ip_list) == 4:
            print "%s.%s.%s.%s" % (int(ip_list[0],base=2),int(ip_list[1],base=2),int(ip_list[2],base=2),
                                   int(ip_list[3],base=2))
        else:
            print "Your input is wrong!"
    else:
        ip = raw_input("Enter your IP adress of decimal  ")
        ip_list = ip.split('.')
        ip_list = map(int,ip_list)
        if len(ip_list) == 4:
            print "%s.%s.%s.%s" % (str(bin(ip_list[0]))[2:].zfill(8),str(bin(ip_list[1]))[2:].zfill(8),
                                   str(bin(ip_list[2]))[2:].zfill(8),str(bin(ip_list[3]))[2:].zfill(8))

        else:
            print "Your input is wrong!"

# 6-12
def findchr(string,char):
    length = len(string)
    length2 = len(char)
    for i in range(length):
        if string[i:i+length2] == char:
            print i
            break
    else:
        print "-1"

def rfindchr(string,char):
    length = len(string)
    length2 = len(char)
    if string[-length2:] == char:
        print length-length2-1
    else:
        for i in range(-1,-length,-1):
            if string[-length2+i:i] == char:
                print i
                print length+i-length2
                break
        else:
            print "-1"

def subchr(string,orchar,char):
    length = len(string)
    length2 = len(orchar)
    for i in range(length):
        if string[i:i + length2] == orchar:
            string = string[0:i]+char+string[i+length2:]
            print string
            break
    else:
        print "-1"

# 6-14
def rochambeau():
    computer = {-1:"石头",-2:"剪刀",-3:"布"}
    human = {1:"石头",2:"剪刀",3:"布"}
    while True:
        key = int(raw_input("1.石头  2.剪刀  3.布 "))
        rad = random.randint(-3,-1)
        res = key+rad
        if key>3:
            print "输入错误"
            continue
        if res == 0:
            print "平局:",human[key],"=",computer[rad]
        elif res%3 == 1:
            print "输了:",human[key],"<",computer[rad]
        elif res%3 == 2:
            print "赢了:",human[key],">",computer[rad]

# 6-15
def isLeapYear(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True

def span():
    month1 = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    month2 = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    day1 = 0
    day2 = 0
    day3 = 0
    try:
        time1 = map(int,raw_input("输入第一个时间：DD/MM/YYYY ").split('/'))
        time2 = map(int,raw_input("输入第二个时间：DD/MM/YYYY ").split('/'))
        if (len(time1) != 3) and (len(time2) != 3):
            print "格式错误！"
        else:
            # 把小年份的时间放在前面
            if time1[2] > time2[2]:
                time1,time2 = time2,time1

            # 计算第一个时间到年开头的时间
            if isLeapYear(time1[2]):
                for i in range(time1[1]):
                    day1 += month2[i]
                day1 = day1+time1[0]
            else:
                for i in range(time1[1]):
                    day1 += month1[i]
                day1 = day1 + time1[0]

            # 计算第二个年份到年初的时间
            if isLeapYear(time2[2]):
                for i in range(time2[1]):
                    day2 += month2[i]
                day2 = day2+time2[0]
            else:
                for i in range(time2[1]):
                    day2 += month1[i]
                day2 = day2 + time2[0]

            # 计算第二个年份年初到第一个年份年初的时间
            for i in range(time1[2],time2[2]):
                if isLeapYear(time1[2]):
                    for i in range(13):
                        day3 += month2[i]
                else:
                    for i in range(13):
                        day3 += month1[i]

            day2 = day2 + day3
            print day2 - day1

    except:
        print "格式错误"

# 用内置函数解决
def alive_day():
    time = map(int,raw_input("Enter a date(YYYY/MM/DD) ").split('/'))
    date1 = datetime.date(time[0],time[1],time[2])
    date2 = datetime.date.today()
    date3 =  date2 - date1
    print date3.days

# 6-17
def mypop(list):
    tem = list[-1]
    del list[-1]
    return tem

# 6-18
def form_out(list):
    num = int(raw_input("Enter your colunm "))
    for i,j in enumerate(list):
        print j,
        if (i+1)%num ==0:
            print

