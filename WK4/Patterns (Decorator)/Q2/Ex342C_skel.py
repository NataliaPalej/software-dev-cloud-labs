from tkinter import messagebox


class Counter:
    def __init__(self, val):
        self.__value = val
        self._message = ''

    def getValue(self):
        return self.__value

    def increment(self):
        self.__value += 1

    def decrement(self):
        self.__value -= 1

    def writeMessage(self, msg):
        self._message = msg

    def readMessage(self):
        return self._message


# ------------end of class definition------------------

# Decorator
class Decorator(Counter):
    def __init__(self, val):
        super().__init__(0)
        self._value = val


class UpperLimit(Decorator):
    def __init__(self, val):
        super().__init__(val)

    def getValue(self):
        # When using Decorator, getValue must be called to read the value
        return self._value.getValue()

    def increment(self):
        if self._value.getValue() > 20:
            self.writeMessage("Upper Limit Reached")
        else:
            # Method to be called rather than assigning self._val += 1
            self._value.increment()

    def decrement(self):
        self._value.decrement()

    def writeMessage(self, msg):
        self._message = msg

    def readMessage(self):
        return self._message


class LowerLimit(Decorator):
    def __init__(self, val):
        super().__init__(val)

    def getValue(self):
        return self._value.getValue()

    def increment(self):
        if self._value.getValue() >= 20:
            self.writeMessage("Upper Limit Reached")
        else:
            self._value.increment()

    def decrement(self):
        if self._value.getValue() <= 0:
            self.writeMessage("Already 0")
        else:
            self._value.decrement()

    def writeMessage(self, msg):
        self._message = msg

    def readMessage(self):
        return self._message
