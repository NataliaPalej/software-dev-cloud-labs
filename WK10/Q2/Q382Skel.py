class Pair:
   @staticmethod
   def add(x, y):
      return x + y

   @staticmethod
   def power(x, y):
      return x ** y


def main():
   value1=int(input("Value 1: "))
   value2=int(input("Value 2: "))
   print('Initial Values = ({0},{1})'.format(value1, value2))

   result = Pair.add(value1,value2)
   print('{0} + {1} = {2}'.format(value1,value2,result))

   result = Pair.power(value1, value2)
   print('{0} To Power of {1} = {2}'.format(value1, value2, result))

main()