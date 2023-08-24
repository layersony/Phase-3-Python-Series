import ipdb
# Operation - comment

# comparison, membership, identity, arthimetic, logical, bitwise 

'''
    = assignment operator

    comparison operator
    == - equal
    < - less than
    > - greater than
    != - not equal
    >= - greater than or equal
    <= - less than or equal


    logical operator
    or - return true if one of the statements is true
    and - returnd true if all of the statements are true
    not - reverse of the 2 above

    Arthimetic 
    +, -, *, /, %, 

    Bitwise operator - used to compare (binary) numbers
    eg - 010001000111100
    AND (&)
    OR (|)
    NOT (-)
    XOR (^)
    << - Zero fill left shift
    >> - Right shift

    Iidentity operator
    is - return true if both variables are in the same object
    is not - return true if both variables are not in the same object

    membership operator
    in - return true if variable is present in sequence
    not in - return true if variable is not present in sequence


    // functions

    function funtionName(){
        return 'some data'
    }

    def functionName():
        // some data


'''

# def greeting(gname):
#     print('Hello, Mr/Mrs ' + gname)


# print('Today is a Good day')
# greeting('Alicia')

# def summation(a, b):
#     return a + b

# ttl = summation(1, 4)
# print(ttl)

'''
Data-types
Variables
Conditional Statements
Loops - While, for loop
Data sTructure - list comphresion, Dictonaries, sets
'''

# String

'MAingi Samuel'
"Maingi Samuel Mutunga"
'''
lajhdss
dskdsfhkfsjhh
fdjdsjkjkfjk
'''

"""
lajhdss
dskdsfhkfsjhh
fdjdsjkjkfjk
"""

# Formatting a string
# f'Hello, Good Morning {name}'


# Syntax of a variable

# variablename = ValueError
# myName = 'Patience'

# Conditional Statements

'''
if.. elif...else
switch
'''

#syntax

#if condition:
    # code here

#elif condition:
    # code here
#else:
    # code here


# weather = "raining"
# money = 100

# if weather == "sunny" or money >= 100:
#     print('Go Swimming...')
# elif weather == "raining":
#     print('Play with Mud...')
# else:
#     print('Go back to bed...')

# match condition:
#     case case1:
#         # code here
#     case case2:
#         # code here
#     case case3:
#         # code here
#     case case4:
#         # code here
#     case _:
#         #code here


# lang = 'Kotlin'

# match lang:
#     case 'Kotlin':
#         print('Am doing Kotlin')
#     case 'JS':
#         print('Am doing Kotlin')
#     case 'Java':
#         print('Am doing Kotlin')
#     case 'Python':
#         print('Am doing Kotlin')
#     case _:
#         print('Am doing Kotlin')


'''
Loops
For loop

# syntax

for variable in variables:
    code here
'''
# # enumerate()
# sports = ['Basketball', 'Football', 'Hockey', 'TT', 'handball']
# for sport in sports:
#     print(sports)

#While loop
'''
variable
while condition:
    code here
    increment
'''

# v = 0
# while v < 5:
#     print('Niko hapa')
#     v += 1


# dictionaries
# myDict = {
#     'key':'value',
#     'key':'value'
# }

# myCar = {
#     'brand':'Audi',
#     'seat': 5,
#     'price': '5,000,000'
# }

# # access
# # print( myCar['brand'] )
# # print( myCar.get('brand') )
# # add
# myCar['wheels'] = 4
# myCar.update({'color':'black'})

# print(myCar)
# # remove
# print('*'*30)
# myCar.pop('seat')
# del myCar['brand']
# print(myCar)


# Data sTructure - list comphresion, Dictonaries, sets
# list
# myStudents = ['Paul', 'John', 'Natasha', 'Jane']
# print(myStudents)

# myStudents.insert(2, 'Wise')

# print(myStudents)

# tuples - once created cannot be changed (execution)
# varaibleName = ('element1', 'element2', 'element3')
myStudents = ('Paul', 'John', 'Natasha', 'Jane', 'John')
mydigits = (1,6,8,7,6,9,8,5,2,7,4,4,8,1,1,9)

# access items
# print( myStudents[6] )

# # loop over tuple
# for i in myStudents:
#     print(i)

# myStudents.remove('Paul')

# print(mydigits.count(1))

# print( len(myStudents) )
# print( len(mydigits) )



# Sets

# 0,1
# False, True

# sports = { "basketball", -1, True, False, 12.9, , 0}
# print(sports)
# print(len(sports))

# others = {"mango", "avocado", "orange", "basketball", 'football', 'football'}

# # print( 'football' in others )
# # others.add('Google Meet')
# print(others)
# others.remove('mango')

# print(others)

# others.discard('avocado')
# print(others)


# List comphresion

# sports = ['basketball', 'football', 'softball', 'baddie', 'bano', 'rugby', 'hockey', 'night-running', 'wrestle', 'motorcross']

# # newSports = [] # only contain B in the them

# # for sport in sports: # loop
# #     if 'b' in sport: # condition
# #         newSports.append(sport) # action

# # # syntax
# # newList = [action  loop   condition]

# newSports = [sport for sport in sports if 'b' in sport ]
# print(newSports) #


# myStudents = ['Paul', 'Alicia', 'Faith', 'Mark', 'John', 'Joseph', 'Marion', 'Isaack', 'Reagan', 'Sasha']

# # namesStartingWithS = []

# # for student in myStudents:
# #     if 's' in student:
# #         namesStartingWithS.append(student)

# namesStartingWithS = [ student for student in myStudents if 's' in student]

# print(namesStartingWithS)

# print(range(1000, 1100))
# for i in range(1000, 1100, 1):
#     myRangeList.append(i)

# myRangeList = [i for i in range(1000, 1100, 2)]

# print(myRangeList)




############################################
########### OOP ############################
############################################


# height, color, age, weight, name, id number

# types of attributes
    # private -> __name='maingi'
    # protected -> _name='maingi'
    # public ->    name='maingi'

# class Person:
#     # code here, attributes, methods, properties
#     def __init__(self, name, age, color):
#         self.fname = name
#         self._age = age
#         self.color = color

#     @property
#     def age(self):
#       return self._age
    
#     @age.setter
#     def age(self, value):
#         if value > self._age:
#             self._age = value # updating the current age
# `

#     def __str__(self):
#         return f'Person {self.fname} of age: {self.age}'

# person1 = Person('Jane', 16, 'chocolate')
# person2 = Person('Isaack', 32, 'white')

# print(person1.age) # before
# person1.age = 17
# print(person1.age) # after





