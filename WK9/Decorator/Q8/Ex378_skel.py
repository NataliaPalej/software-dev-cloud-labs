applyNo = int(input('Number of times to apply Function: '))

def main():
    value = int(input('Enter Value: ' ))
    value = stepValue(value)
    print('Value: ',value)

def apply_return_decorator(applyNo):
    def apply_return_decorator(func):
        def closure(value):
               res = func(value)
               for x in range(1, applyNo):
                   res = func(res)
               return res
        return closure
    return apply_return_decorator

@apply_return_decorator(applyNo)
def stepValue(value):
    return value + 1


main()