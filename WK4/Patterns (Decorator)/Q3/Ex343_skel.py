def main():
    # d1 = Display("Athlone")

    #d1 = UnderLine(Display("Athlone"))
    #d1 = OverLine(Display("Athlone"))
    d1 = UnderLine(OverLine(Display("Athlone")))

    option = menu()
    print()
    while option != 3:
        if option == 1:
            d1.printName()
        elif option == 2:
            newName = input('Enter new Name:')
            d1.updateName(newName)
        option = menu()
        print()


def menu():
    print("\nMenu ")
    print("--------------")
    print("1.  print Name")
    print("2.  Change Name")
    print("3. Exit")
    result = int(input('Enter Choice:'))
    return result


class Display:
    def __init__(self, nm):
        self._name = nm

    def printName(self):
        print("Name= ", self._name)

    def updateName(self, nm):
        self._name = nm


class Decorator(Display):
    def __init__(self, name):
        super().__init__("")
        self._name = name


# Trace name
class UnderLine(Decorator):
    def __init__(self, name):
        super().__init__(name)

    def printName(self):
        self._name.printName()
        print("===========")

    def updateName(self, name):
        self._name.updateName(name)


class OverLine(Decorator):
    def __init__(self, name):
        super().__init__(name)

    def printName(self):
        print("===========")
        self._name.printName()

    def updateName(self, name):
        self._name.updateName(name)


main()
