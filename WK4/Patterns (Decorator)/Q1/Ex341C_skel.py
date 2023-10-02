from tkinter import messagebox


class Account:

    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
        self._message = ""

    def getBalance(self):
        return self.__balance

    def deposit(self, amt):
        self.__balance += amt

    def withdraw(self, amt):
        self.__balance -= amt

    def getName(self):
        return self.__name

    def writeMessage(self, msg):
        self._message = msg

    def readMessage(self):
        return self._message


# ------------end of class definition------------------
# Decorator

class Decorator(Account):

    def __init__(self, acc):
        super().__init__("", 0)
        self._account = acc


# Trace Account
class TestAcc(Decorator):
    def __init__(self, acc):
        super().__init__(acc)

    def getBalance(self):
        return self._account.getBalance()

    def deposit(self, amt):
        self.writeMessage(" -deposit() called")
        self._account.deposit(amt)

    def withdraw(self, amt):
        self.writeMessage(" -withdraw() called")
        self._account.withdraw(amt)

    def getName(self):
        return self._account.getName()

    def writeMessage(self, msg):
        self._account.writeMessage(msg)

    def readMessage(self):
        return self._account.readMessage()


# NoOverdraft Account
class NoOverdraft(Decorator):

    def __init__(self, acc):
        super().__init__(acc)

    def getBalance(self):
        return self._account.getBalance()

    def deposit(self, amt):
        self._account.deposit(amt)

    def withdraw(self, amt):
        if (amt > self.getBalance()):
            messagebox.showerror("Error", "Insufficient Funds")
        else:
            self._account.withdraw(amt)

    def getName(self):
        return self._account.getName()

    def writeMessage(self, msg):
        self._account.writeMessage(msg)

    def readMessage(self):
        return self._account.readMessage()


# Limited Account
class Limited(Decorator):
    def __init__(self, acc):
        super().__init__(acc)

    def getBalance(self):
        return self._account.getBalance()

    def deposit(self, amt):
        if amt > 300:
            messagebox.showerror("Error", "Max deposit amount allowed $300,\nYou tried deposit ${0}".format(amt))
        else:
            self._account.deposit(amt)

    def withdraw(self, amt):
        if amt > 300:
            messagebox.showerror("Error", "Max withdraw amount allowed $300,\nYou tried withdraw ${0}".format(amt))
        elif amt > self.getBalance():
            messagebox.showerror("Error", "Insufficient Funds")
        else:
            self._account.withdraw(amt)

    def getName(self):
        return self._account.getName()

    def writeMessage(self, msg):
        self._account.writeMessage(msg)

    def readMessage(self):
        return self._account.readMessage()