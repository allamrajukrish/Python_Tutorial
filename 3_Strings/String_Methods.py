myStr = "Hey! I'm just a string"
print("Hey\tHello")
#capitalize() #Capitalizes first letter of string

print(myStr.center(50,"#"))

#center(width, fillchar) 
'''Returns a string padded with 
fillchar (what ever the char)with the 
original string centered to a 
total of width.'''

#count(str, beg = 0 end = len(string))
'''Counts how many times a string occurs 
in another string or in a substring of string 
if starting index beg and ending index end are given.'''
print(myStr.count("st",0,len(myStr)))


print(myStr.find("string",0,len(myStr)))

#find(str, beg = 0 end = len(string))
'''Determine if str occurs in string or in a 
substring of string if starting index 
beg and ending index end are given returns 
index if found and -1 otherwise.'''

print(myStr.index("string",0,len(myStr)))
#index(str, beg = 0, end = len(string))
'''Same as find(), but raises an exception 
if str not found.'''

print(myStr.find('abc',0,len(myStr)))
print(myStr.index('just',0,len(myStr)))


#isalnum()
'''This method returns true if string has 
at least 1 character and all characters 
are alphanumeric and false otherwise.'''
str1="A1"
print("-------------------")
print(str1.isalnum())
print("-------------------")



#isdigit()
'''This method returns true if string has 
at least 1 character and all characters 
are numeric and false otherwise.'''

str1="A123!"
print("+++++++++++++++++++")
print(str1.isdigit())
print("+++++++++++++++++++++")



#isalpha()
'''This method returns true if string has 
at least 1 character and 
all characters are alphabetic 
and false otherwise.'''

str1="abc"
print("**********************")
print(str1.isalpha())
print("+++++++++++++++++++++")

#islower()
'''This method returns true if string has 
at least 1 cased character and 
all cased characters are in lowercase 
and false otherwise.'''
print("**********************")
print(str1.islower())
print("**********************")
#isnumeric()
'''This method returns true if a unicode string 
contains only numeric characters and 
false otherwise.'''
a="12.4"
print(a.isnumeric())


#isspace()
'''This method returns true if string contains only 
whitespace characters and false otherwise.'''
myStr = "    Hi Good            "
print("______________________")
print(myStr.isspace())
print("______________________")



#istitle()
'''This method returns true if string is properly 
"titlecased" and false otherwise.'''
print("+++++++++++++++++++++++++++++++")

myStr = "HEY HELLO GOOD EVENING"
print(myStr.istitle())
print("+++++++++++++++++++++++++++++++")

#isupper()
'''This method returns true if string has at least 
one cased character and all cased characters 
are in uppercase and false otherwise.'''
print(myStr.isupper())
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

#join()
'''This method returns a string in which the 
string elements of sequence have been 
joined by str separator.'''

#ljust(width[, fillchar])
'''This method returns the string left justified 
in a string of length width. 
Padding is done using the specified 
fillchar (default is a space). 
The original string is returned if width 
is less than the length of the actual string.'''

#lstrip()
'''This method returns a copy of the string in which 
all chars have been stripped from the 
beginning of the string, by default whitespace characters.'''

#rstrip()

#max()
'''This method returns the max alphabetical 
character from the string str.'''
#min()
'''This method returns the min alphabetical 
character from the string str.'''

#replace(old, new, no of occurences)
'''method returns a copy of the string 
in which the occurrences of old have been 
replaced with new, optionally restricting 
the number of replacements to max'''


myStr = "Hey Just Checking"


print(myStr.isalnum())

print(myStr.isdigit())

print(myStr.isalpha())

print(myStr.islower())

print(myStr.isnumeric())

print(myStr.isspace())

print(myStr.istitle())

print(myStr.isupper())

str1 = ","
strSeq = ("Vizag", "Andhrapradesh", "530016") 
# above is a sequence of strings.
print (str1.join(strSeq))


myName = "Hey, This is Krish"
print (myName.ljust(50, '#'))

myName = "     Hey, This is Krish"
print (myName.lstrip())

myName = "aaaaaaaaaaaaaaaaHez, This is Krish___________"
a = myName.lstrip('a')
b = a.rstrip('_')
print("value of b is %s" %b)

myName= "krishna"
print(max(myName))

print(min(myName))


testStr = "He is Krish. Krish is working in Stellentsoft"
print (testStr.replace("Krish", "Prasanth"))
print (testStr.replace("Krish", "Prasanth", 1))

print(testStr.title())
