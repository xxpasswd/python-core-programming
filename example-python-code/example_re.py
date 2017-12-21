#coding=utf-8

import re

s = """aaa@aa@a.com"""
s2 = "aaa@aaa.bbb.com"
s3 = "aaa@aaa.bbb.ccc.com"
s4 = "aaa@aaa.bbb.ccc.ddd.com"
s5 = "abcd"
s6 = "(aaaa(a(ddd)da)(adsfsa)ddd)"

r = '\w+@\w+(\.\w+)\.com'
r2 = '(a(b(c)))'
r3= '(.*?)@'
m = re.compile("\(.*?\)") #非贪婪模式,尽可能少的匹配
m2 = re.compile("\(.*\)")
res =m.findall(s6)
res2 = m2.findall(s6)
res3 = re.match(r2,s5)
re4 = re.match(r3,s)
print(res)
print(res2)
print(res3.groups())
print(re4.groups())
