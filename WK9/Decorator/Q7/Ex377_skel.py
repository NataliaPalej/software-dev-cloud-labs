def main():
    value=input('Enter Name:' )
    printName(value)

def repeat_void_decorator(func):
    def closure(value):
        for el in range(0,2):
            func(value)
    return closure

def repeat_void(num_times=2):
    def repeat_void_decorator(func):
        def closure(value):
            for i in range(0, num_times):
                func(value)
        return closure
    return repeat_void_decorator

@repeat_void(num_times=5)
def printName(value):
    print("Name is: ", value)



main()
