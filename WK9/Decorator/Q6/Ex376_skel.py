def main():
    printNames("John", "Joseph",  "Lennon")
    print()
    printNames("John", "Joseph","Michael", "Smith")
    print()
    printNames("John", "Joseph","Michael","Leo", "Jones")

def max_args_decorator(max_entry=2):
    def max_args_decorator(func):
        def closure(*args):
            if len(args) > max_entry:
                print("Only {0} arguments allowed".format(max_entry))
            else:
                return func(*args)
        return closure
    return max_args_decorator

@max_args_decorator(5)
def printNames(*args):
    for el in args:
        print(el,end=' ')


main()