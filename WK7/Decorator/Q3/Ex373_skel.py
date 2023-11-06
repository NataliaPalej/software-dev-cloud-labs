def main():
    price = float(input('Enter Initial Price: '))
    printTotalPrice(price)
    print('\nPrice including Vat @ 20%: ')
    vat_decorator(printTotalPrice)(price)
    print('\nPrice including Delivery Charge - Fixed at €10')
    delivery_decorator(printTotalPrice)(price)
    print('\nPrice including VAT + Delivery Charge')
    vat_decorator(delivery_decorator(printTotalPrice))(price)
    print("\nExtra decorator + €20: ")
    vat_decorator(delivery_decorator(extra_decorator(printTotalPrice)))(price)


def vat_decorator(func):
    def closure(n):
        func(n*1.2)
    return closure

def delivery_decorator(func):
    def closure(n):
        func(n+10)
    return closure

def extra_decorator(func):
    def f2(n):
        func(n+20)
    return f2

def printTotalPrice(price):
    print('Total Price =', round(price,2))

main()
