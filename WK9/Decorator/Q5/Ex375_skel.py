def main():
    value1= int(input('Enter Value1:'))
    value2 = int(input('Enter Value2:'))
    res = divide(value1, value2)
    print('Result: ',res)

def no_zero_decorator(func):
    def closure(v1, v2):
        if v2 == 0:
            return "Zero arguments not allowed"
        else:
            return func(v1, v2)
    return closure

@no_zero_decorator
def divide(x,y):
    return x/y


main()