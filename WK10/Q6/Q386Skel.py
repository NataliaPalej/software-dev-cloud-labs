class Stepper:
    def __init__(self, value1):
        self.__count = value1

    def stepUp(self):
        self.__count += 1

    @property
    def Count(self):
        return self.__count

    @Count.setter
    def Count(self, new_Value):
        self.__count = new_Value

    @Count.getter
    def Count(self):
        return self.__count

    @Count.deleter
    def Count(self):
        del self.__count


def main():
    s = Stepper(4)
    print('Initial Value: ', s.Count)
    s.stepUp()
    print('After Step Up: ', s.Count)
    s.Count = s.Count + 5
    print('After Adding 5: ', s.Count)


main()
