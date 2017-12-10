myInfoDict = {'Name': 'Krish', 'Office_Name': 'Stellentsoft', 'IdNo': 'STL1110'}
tempDict={'a':1,'b':2,'c':3}
print ("myInfoDict['Name']: ", myInfoDict['Name'])
print ("myInfoDict['Office_Name']: ", myInfoDict['Office_Name'])
print("myInfoDict before the updating : ",myInfoDict)

#Update the dictonary

myInfoDict['Name'] = 'Prashanth'
myInfoDict['Office_Name'] = 'Coding Sastra'
myInfoDict['IdNo'] = 'CS1234'
print("myInfoDict after the updating : ",myInfoDict)
#Adding new key-Value
myInfoDict['Address'] = 'Vizag'
myInfoDict['PhoneNo'] = 9441239901
print("myInfoDict after the updating : ",myInfoDict)

#Predefined methods
print ("Length of myInfoDict is : %d" % len (myInfoDict))

print ("myInfoDict Type :", type (myInfoDict))

#clear():This method removes all items from the dictionary.
tempDict.clear()
print ("Finally the Length of  : %d" %  len(tempDict))

#copy():This method returns a copy of the dictionary.
myInfoDict_copy = myInfoDict.copy()
print ("MyInfoDict_copy : ",myInfoDict_copy)

#get()
print ("Value : %s" %  myInfoDict_copy.get('Name'))
print ("Value : %s" %  myInfoDict_copy.get('abc', "Not Found"))

#items()
print ("Items are  : %s" %  myInfoDict_copy.items())

#keys()
print ("Keys are  : %s" %  myInfoDict_copy.keys())
print ("Keys are  : %s" %  myInfoDict_copy.values())

#update()

subDict = {'Language': 'Python' }

myInfoDict_copy.update(subDict)
print ("updated myInfoDict_copy is : ", myInfoDict_copy)


a=['bcd','food','gcd', 'elep']

for x in a:
	elmement=x
	for char1 in elmement:
		if char1=='a' or char1=='e' or char1=='i' or char1=='o' or char1=='u':
			print(elmement)
			break


list1=['Krish', 'prasanth', 'Theja']
list2=['Swift','Python','Python']
[{'Name': 'Krish', 'Language': 'Swift'},{'Name': 'prasanth', 'Language': 'Python'},{'Name': 'Theja', 'Language': 'Python'}]

a={'Name': 'Krish', 'Language': 'Swift'}
del a['Language']
print(a)






 
