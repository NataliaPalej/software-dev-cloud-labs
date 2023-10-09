from abc import abstractmethod, ABC


class Customer(ABC):
    def __init__(self, name, age, priority, price):
        self._name = name
        self._age = age
        self._priority = priority
        self._price = price

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def getPriority(self):
        return self._priority

    def getGrossPrice(self):
        return self._price

    @abstractmethod
    def getNetPrice(self):  # After Discount
        pass

    @abstractmethod
    def getCustomerType(self):  # Priority, Regular, Child
        pass

    def updatePrice(self, price):
        self._price = price


# ------------------------------------------------------
class RegularCustomer(Customer):
    def __init__(self, name, age, priority, price):
        super().__init__(name, age, priority, price)

    def getNetPrice(self):
        return self._price

    def getCustomerType(self):
        return "Regular"


class CustomerFactory:
    def getCustomer(self, name, age, priority, price):
        if age < 17:
            return ChildCustomer(name, age, priority, price)
        elif age >= 17:
            return RegularCustomer(name, age, priority, price)
        elif priority:
            return PriorityCustomer(name, age, priority, price)


# Create new PriorityCustomer/ChildCustomer
class PriorityCustomer(Customer):
    def __init__(self, name, age, priority, price):
        super().__init__(name, age, priority, price)

    def getNetPrice(self):
        return self._price + 10

    def getCustomerType(self):
        return "Priority"


class ChildCustomer(Customer):
    def __init__(self, name, age, priority, price):
        super().__init__(name, age, priority, price)

    def getNetPrice(self):
        if self._priority:
            return (self._price / 2) + 10
        else:
            return self._price / 2

    def getCustomerType(self):
        return "Child"
