import sys


def fun1():
    target = int(sys.argv[1])
    list1 = [2, 5, 8, 11]
    list2 = [3, 4, 9, 11]
    result1 = search(target, list1)
    result2 = search(target, list2)

    if result1 == True or result2 == True:
        print("\n{0} found in list: ".format(target))
    else:
        print("\n{0} NOT found in list: ".format(target))


def search(target, list):
    print("Search")
    if target in list:
        print("Found")
        return True
    else:
        print("Not Found")
        return False


fun1()
