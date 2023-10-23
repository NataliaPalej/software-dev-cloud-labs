from abc import abstractmethod, ABC

class Iterator(ABC):
    @abstractmethod
    def hasNext(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> object:
        pass


class Container(ABC):
    @abstractmethod
    def getIterator(self) -> Iterator:
        pass


class Sentence(Container, Iterator) :
    def __init__(self, sentence):
        self.__sentence = sentence
        self.__index=0

    def toList(self):
        result = self.__sentence.split()
        return result

    def printDetails(self):
        print('\nSentence Details:')
        print('-----------------')
        print('Sentence: ', self.__sentence)

    #### Methods that needed to be added ####

    # Initialise getIterator method
    def getIterator(self):
        return Sentence(self.__sentence)

    # Check if there is another sentence
    def hasNext(self):
        return self.__index < len(self.toList())

    # Get the next word
    def next(self):
        myList = self.toList()
        word = myList[self.__index]
        self.__index += 1
        return word

    #### End of methods that needed to be added ####

def main():
    newSentence = input('Enter Sentence: ')
    s=Sentence(newSentence)
    s.printDetails()

    print('\nList of Words: ')
    printWords(s)

    target = input("\nEnter Word to search for: ")
    result = searchWord(s, target)
    if result:
        print("\"{0}\" occurs in Sentence \"{1}\"".format(target, newSentence))
    else:
        print("\"{0}\" does NOT occur in Sentence \"{1}\"".format(target, newSentence))


def printWords(n):
    value = n.getIterator();
    while value.hasNext():
        word=value.next()
        print(word)


def searchWord(s, target):
    value = s.getIterator();
    result = False
    while value.hasNext():
        word =value.next()
        if word.lower()==target.lower():
            result = True
    return result


main()