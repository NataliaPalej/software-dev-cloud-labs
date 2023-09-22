import sys

# To run the below in PyCharm -> Edit Run Configuration -> Enter Parameters -> Ok -> Run

def fun1():
    # total number of arguments
    n = len(sys.argv)
    print("Total arguments passed: ", n)

    v1 = int(sys.argv[1])
    v2 = int(sys.argv[2])

    result = sum(v1, v2)
    print("\n{0} + {1} = {2}".format(v1, v2, result))


def sum(v1, v2):
    return v1 + v2


fun1()
