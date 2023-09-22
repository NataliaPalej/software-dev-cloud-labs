from threading import *
import time
import sys

x=0

def main():
    global x
    d1 = StepX()
    d2 = PrintX()
    d2.print()
    d1.step()



class StepX():

    def step(self):
        global x
        for i in range (1,10):
            x += 1
            time.sleep(1)

class PrintX():

    def print(self):
        global x
        for i in range (1,10):
            sys.stdout.write('x=:     ' + str(x) + "\n")
            time.sleep(1)

main()
