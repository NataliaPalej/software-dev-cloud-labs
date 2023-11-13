class Euro:
   def __init__(self, euro,cent):
      self.__euro = euro
      self.__cent = cent

   def addCent(self, cent):
      self.__cent += cent
      if (self.__cent>99):
         self.__cent-=100
         self.__euro+=1

   @classmethod
   def createNewEuro(cls, amount):
       e = int(amount)
       c = int((amount-e)*100)
       return cls(e, c)

   def printDetails(self):
      if (self.__cent>9):
         print('\nEuro= €{0}.{1}'.format(self.__euro,self.__cent))
      else:
         print('\nEuro= €{0}.0{1}'.format(self.__euro,self.__cent))


def main():
      m1 = Euro(2,45)
      m1.printDetails()
      amt=int(input('\nEnter Amount of Cent to add: '))
      m1.addCent(amt)
      m1.printDetails()
      newAmt=float(input('Enter New amount of Euro (e.g 5.56) : '))
      m2=Euro.createNewEuro(newAmt)
      m2.printDetails()


main()



