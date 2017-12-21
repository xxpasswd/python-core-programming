#coding=utf-8

# from time import ctime,sleep
import time

def dec(fun):
    print("enter dec")
    def wrapper():
        print("dec")
        start = time.time()
        fun()
        end = time.time()
        print(end-start)
    return wrapper

def dec2(fun):
    print("enter dec2")
    def wrapper():
        print("dec2")
        fun()
    return wrapper


#带参数的装饰器需要三层函数定义
def dec3(arg=True):
    if arg:
        def _dec(fun):
            def wrapper():
                start = time.time()
                print("有时间记录")
                fun()
                end = time.time()
                print(end-start)
            return wrapper

    else:
        def _dec(fun):
            def wrapper():
                print("没有时间记录")
                fun()
            return wrapper
    return _dec

# @dec
# def aaa():
#     pass
#
# #dec(myfun)
# @dec
# def myfun():
#     print("start")
#     time.sleep(2)
#     print("end")
#
#
# #dec(dec2(myfun))
# @dec
# @dec2
# def myfun2():
#     print("start")
#     time.sleep(1)
#     print("end")

@dec2
@dec
def myfun3():
    print("start")
    time.sleep(1)
    print("end")

myfun3()