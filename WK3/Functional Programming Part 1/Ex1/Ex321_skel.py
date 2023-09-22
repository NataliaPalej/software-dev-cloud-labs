import sys


def fun1():
    v1 = int(sys.argv[1])  # 4
    v2 = int(sys.argv[2])  # 6
    v3 = int(sys.argv[3])  # 14
    result = max_val(v1, v2, v3)
    print("Max of {0}, {1}, {2} = {3}".format(v1, v2, v3, result))


def max_val(value1, value2, value3):
    if value1 > value2 and value1 > value3:
        return value1
    elif value2 > value1 and value2 > value3:
        return value2
    else:
        return value3


fun1()
