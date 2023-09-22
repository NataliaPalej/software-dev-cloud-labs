from threading import *
import time
import sys

Res=0

def main():
    global Res
    t1 = Thread(target=step1)
    t2 = Thread(target=step2)
    t2.start()
    t1.start()
    t1.join()
    t2.join()
    print('Final Value: ',Res)

def step1():
    global Res
    localVal1 = Res
    for i in range(1,101):
        localVal1 +=1
        time.sleep(0.02)
    Res = localVal1

def step2():
    global Res
    localVal2 = Res
    for i in range(1,101):
        localVal2 +=2
        time.sleep(0.02)
    Res = localVal2








main()
