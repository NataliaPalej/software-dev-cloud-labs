def main():
    print('\nName: ', end='')
    printName("Joan Smith")
    print()

def titleMr_decorator(func):
    def closure(n):
        print('Mr ', end='')
        func(n)
    return closure

def titleMs_decorator(func):
    def f2(n):
        print("Ms ", end="")
        func(n)
    return f2

def equalBSc_decorator(func):
    def f2(n):
        print("Bsc ", end="")
        func(n)
    return f2

@titleMs_decorator
@equalBSc_decorator
def printName(name):
    print(name, end='')




main()
