from threading import *
import time
import sys

x=0

def main():
    global x
    print()
    step()

def step():
    global x
    for i in range (1,10):
        x += 1
        time.sleep(1)

def print():
    global x
    for i in range (1,10):
        sys.stdout.write('x=:     ' + str(x) + "\n")
        time.sleep(1)

main()
