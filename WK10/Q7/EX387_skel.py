class Account:
    def __init__(self, number, balance):
        self.__number = number
        self.__balance = balance

    def deposit(self, amt):
        self.__balance += amt

    def withdraw(self, amt):
        self.__balance -= amt

    @property
    def Balance(self, balance):
        self.__balance = balance

    @Balance.setter
    def Balance(self, new_Balance):
        self.__balance == new_Balance

    @Balance.getter
    def Balance(self):
        return self.__balance

    @Balance.deleter
    def Count(self):
        del self.__count


def main():
    a = Account('B234234', 200)
    choice = 0
    while choice != 4:
        print('\nOptions')
        print('1. Deposit')
        print('2. Withdraw')
        print('3. Read Balance')
        print('4. Exit')
        choice = int(input('Enter Choice:'))
        if choice == 1:
            amt = int(input('Enter Amount:'))
            a.deposit(amt)
            print('\nBalance after Deposit: ', a.Balance)
        elif choice == 2:
            amt = int(input('Enter Amount:'))
            if amt > a.Balance:
                print('\nInsufficient Funds')
            else:
                a.Balance = a.Balance - amt
                a.withdraw(amt)
                print('\nBalance after Widthraw: ', a.Balance)
        else:
            print('\nBalance=', a.Balance)


main()
