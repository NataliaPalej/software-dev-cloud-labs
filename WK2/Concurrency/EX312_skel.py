from threading import *
import time
import sys

def main():
    d1 = Incrementer_1_9()
    d2 = Decrementer_9_1()
    d1.change()
    d2.change()


class Incrementer_1_9():

    def change(self):
        for i in range(1,10):
            sys.stdout.write('Increment_1_9:    ' + str(i) + "\n")
            time.sleep(1)

class Decrementer_9_1():

    def change(self):
        for i in range(9,0,-1):
            sys.stdout.write('Decrement_9_1:     ' + str(i) + "\n")
            time.sleep(1)

main()
