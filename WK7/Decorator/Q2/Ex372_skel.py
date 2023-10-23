def main():
    print('Price: £', end='')
    printPrice(2.34)
    print('\nPrice in Dollars: ', end='')
    dollar_decorator(printPrice)(round(2.34*1.13,2))
    print('\nPrice in Euro: ', end='')
    euro_decorator(printPrice)(round(2.34*1.15,2))

def dollar_decorator(func):
    def f2(x):
        print("$", end="")
        func(x)
    return f2

def euro_decorator(func):
    def f2(x):
        print("€", end="")
        func(x)
    return f2

def printPrice(price):
    print(price)




main()
