from threading import *
import sys
import time
def main():
    d1 = DisplayRoscommon()
    d2 = DisplayOffaly()
    d1.display()
    d2.display()


class DisplayRoscommon():

    def display(self):
        for i in range(1,6):
            sys.stdout.write('Roscommon\n')
            time.sleep(1)

class DisplayOffaly():

    def display(self):
        for i in range(1,6):
            sys.stdout.write('Offaly\n')
            time.sleep(1)
main()
