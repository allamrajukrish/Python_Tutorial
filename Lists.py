myTechLanguages = ['C', 'Python', 'Objective-C', 'Swift'];
myNumList = [1, 2, 3, 4, 5, 2]
alphaList = ["a", "b", "c", "d"]
myAlphaNumList=[1,'a',2,'b',3,'c', 2]
print("My My Tech Languages list is {}" .format(myTechLanguages));
print("My My Numbers list is {}" .format(myNumList))
print("My AlphaNumeric list is {}" .format(myAlphaNumList))
print(myTechLanguages[1])
alphaList[0]  
print(myAlphaNumList[1:5])

newList = myNumList + alphaList #appending of two lists
print(newList)

myAlphaNumList[5]='z' #Updating of list
print("Updated AlphaNumeric list is {}" .format(myAlphaNumList))

del myAlphaNumList[3]
print ("After deleting the myAlphaNumList is : ", myAlphaNumList)
print(myNumList*3)
print(len(myAlphaNumList))

print(myAlphaNumList[::-1]) #to print the list in reverse order

print(max(myNumList))
print(min(alphaList))
print(max(myTechLanguages))


#append()
myTechLanguages.append("C++")
print("updated list is ", myTechLanguages)
#count()
'''This method returns method returns 
count of how many times obj occurs in list.'''
a=2
print(myAlphaNumList.count(a))

#extend()
'''This method appends the contents to the list.'''
alphaList.extend('a')
print(alphaList)
alphaList.extend(myNumList)
print(alphaList)

#index()
'''This method returns the lowest 
index in list that obj appears'''

print(alphaList.index(2))

#insert()

'''This method inserts the 
object into list at mentioned index.'''

alphaList.insert(3,'a')
print(alphaList)

#pop()
'''This method removes and returns last object 
when it is occured or obj from the list
'''
alphaList.pop()
print ("alphaList : ", alphaList)
alphaList.pop(1)
print ("alphaList : ", alphaList)

#remove()
'''This method removes the first occurence 
of the object in the list.'''

alphaList.remove('a')
print(alphaList)

alphaList.remove('a')
print(alphaList)

#reverse()
alphaList.reverse()
print(alphaList)

#sort() When the list is homogeneous
myTechLanguages.sort()
print(myTechLanguages)













