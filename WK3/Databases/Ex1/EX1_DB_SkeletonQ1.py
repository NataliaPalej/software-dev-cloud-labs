import sqlite3


# ============================================================
# General Methods to Display Data


def displayAll():
    cur.execute("select * from Person")
    list = cur.fetchall()
    print('\nList of Persons')
    print(' Name        Age')
    print('--------------------')
    for currentPerson in list:
        print("[", currentPerson[0], "\t", currentPerson[1], "]")


def createTable():
    try:
        cur.execute("CREATE TABLE Person(Name, Age)")
        data = [
            ("J.Smith", 25),
            ("T.Jones", 33),
            ("L.Shine", 55),
            ("M.Moore", 45),
            ("W.Lemon", 66), ]

        cur.executemany("INSERT INTO Person VALUES(?, ?)", data)

        con.commit()

    except:
        print("Person Aready Exists")


# ========= Definitions ============================


def cmdDisplayAge(name):
    cur.execute("select * from Person where Name = " + "\'" + str(name) + "\'")
    currentPerson = cur.fetchall()[0]
    print("Age= " + str(currentPerson[1]))


def cmdDelete(name):
    try:
        cur.execute("Delete from Person where Name = \'" + name + "\'")
        con.commit()
    except:
        print('Person: ', name, ' does not exist in Database')


def stepAgeCmd(name):
    try:
        cur.execute("Update Person set Age=Age + 1 where Name = \'" + name + "\'")
        con.commit()

    except:
        print('Person: ', name, ' does not exist in Database')


def insertCmd(newName, newAge):
    try:
        cur.execute("INSERT INTO PERSON VALUES(" + "\'" + newName + "\', " + str(newAge) + ")")
        con.commit()

    except:
        print('Person: ', newName, ' does not exist in Database')


def updateAgeCmd(name, newAge):
    try:
        cur.execute("UPDATE Person SET age = ? WHERE name = ?", (newAge, name))
        con.commit()
    except:
        print("Person: ", name, "doesn't exist in database.")


def deleteAgeCmd(ageLimit):
    try:
        cur.execute("DELETE from Person WHERE age < " + str(ageLimit))
        con.commit()
    except:
        print("No people age < ", ageLimit, "to delete from database.")


def displayInRangeCmd(lowerAge, upperAge):
    try:
        cur.execute("SELECT * FROM Person WHERE age >= " + str(lowerAge) + " AND AGE <= " + str(upperAge))
        #con.commit()
        peopleList = cur.fetchall()
        # Use for loop when view only 
        for i in peopleList:
            print("Name: ", i[0], "Age: ", i[1])
    except:
        print("No people to displayed in given range: " + str(lowerAge) + " to " + str(upperAge))


# con = sqlite3.connect("../../Downloads/tutorial.db")
con = sqlite3.connect("tutorial.db")
cur = con.cursor()

createTable()
displayAll()
'''
name = input('\nEnter Name of Student to Modify: ')

print('Step Age up by 1')
stepAgeCmd(name)
displayAll()

name = input('\nEnter Name of Student to Display Age: ')
cmdDisplayAge(name)

name = input('\nEnter Name of Student to Delete: ')
cmdDelete(name)
displayAll()

print(('\nInsering a new Person'))
name = input('\nEnter Name of Person to Add: ')
age = int(input('\nEnter Persons Age: '))
insertCmd(name, age)
displayAll()
'''
# Q1 resetting Age
# print('Resetting Age to a new Value')
# name = input('\nEnter Name of Student to Reset Age: ')
# age = int(input('\nEnter New Age: '))
# updateAgeCmd(name, age)
# displayAll()

# --------------------------------------------
# Q2 displaying people within Age Range
print('Displaying details about People in Given Age Range Inclusive')
lowerAge = int(input('\nEnter Lower Age Limit: '))
upperAge = int(input('\nEnter Upper Age Limit: '))
displayInRangeCmd(lowerAge, upperAge)


# --------------------------------------------
# Q3 Deleting people younger tan a given Value
#print('Deleting Everyone in the list younger than a given age')
#ageLimit = int(input('\nEnter Lower Age Limit: '))
#deleteAgeCmd(ageLimit)
#displayAll()
