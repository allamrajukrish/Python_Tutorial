print("Hello World!")

a=23
print (a)
# This is how we do single line comment, we use '#'' before the line.

'''
This is how we do multi line commenting, we use ''' 
''
import os
clear = lambda: os.system('cls')
clear()

import os
clear = lambda: os.system('clear')
clear()


myName = 'Krish'
idNum = 10123
varIsFlag = True
print(type(idNum))   #function "type" will tell us about the datatype of the object
print (type(myName))
print (type(varIsFlag))

type(14)
print(type(True))
print(type(999888777)) #Python2.7 will treat it like a longint

import keyword
print(keyword.kwlist)

#Basic Operators
#___________Addition____________
varAddition = 32+23
print(varAddition)

print(33+44+55+66)

print(1.1+2.2+3.3+4.4+5)

#____________Subtraction____________

varSubtraction = 23-32
print(varSubtraction)

print(12-3)

print(10-2.5)

#___________Multiplication___________

varMultiplication = 5*8
print(varMultiplication)

print(10*4)

print(2.2*4)

print(5**3) #Exponent 
'''
here ** is used to multiply the same number with 
given number of times. You can also read it like
5 to the power 3 or 5 cube 
'''

#______________Division_________________


varDivision = 44/11
print(varDivision)

print(48/6)

print(5/2)

print(96/8.0)

print (44//11) # here // will round the division result

print (5.0 // 2) # here // will round the division result

varModular = 5%2 # which gives the reminder
print(varModular) 

#Operator Precedence : Complex arithmetic operations

varResult = ((12+13)*3)/5+150-(5**3)
print("The Result is %d" %varResult)


