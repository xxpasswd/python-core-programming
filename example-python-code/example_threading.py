#coding=utf-8

import threading
from time import ctime,sleep
import sys

loops = [2,4]

def loop(nloop,nsec):
    sys.stdout.write("start loop %s at %s\n" %(nloop,ctime()))
    sleep(nsec)
    sys.stdout.write("loop %s done at %s\n" %(nloop,ctime()))

def main():
    print("start at",ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print("all done at",ctime())

if __name__ == '__main__':
    main()