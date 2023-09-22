import sys


def fun1():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    result1 = addInRange(a, b)
    result2 = recursion(a, b)
    print("Standard addInRange method:\nSum of {0} to {1} = {2}".format(a, b, result1))
    print("\nRecursion method:\nSum of {0} to {1} = {2}".format(a, b, result2))


def addInRange(first, last):
    result = 0
    for i in range(first, last+1):
        result += i
    return result


def recursion(first, last):
    if first > last:
        return 0
    else:
        return first + recursion(first+1, last)

fun1()
