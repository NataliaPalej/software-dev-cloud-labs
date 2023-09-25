def main():
    val1 = int(input('Enter Value1: '))
    val2 = int(input('Enter Value2: '))
    val3 = int(input('Enter Value3: '))
    result1 = hCount(pIsEven, val1, val2, val3)
    print('Number  of Even Items=', result1)
    result2 = hCount(pSingleDigit, val1, val2, val3)
    print('Number of Single Digits=', result2)


pIsEven = lambda x: (x % 2 == 0)

pSingleDigit = lambda x : x < 10


def hCount(f, a, b, c):
    result = 0
    list1 = [f(a), f(b), f(c)]
    for i in list1:
        if i == True:
            result += 1
        else:
            result += 0
    return result


main()
