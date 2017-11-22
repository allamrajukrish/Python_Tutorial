num = 11
while num < 22:
   print ('The count is:', num)
   num=num+1
print ("Hey! I got it.")

newNum = 1
count=0
while newNum<=10:
	count=count+newNum
	newNum = newNum+1
print("The sum of first 10 numbers is", count)


#while with else
while newNum<=10:
	count=count+newNum
	newNum = newNum+1
	#print("The sum of first 10 numbers is", count)
else:
	print("You reached out of scope")
print("The sum of first 10 numbers is", count)

myList=['a',1,'b',2,'c',3]
for obj1 in myList:
	print ("Object is",obj1)

#range()

myList=['a',1,'b',2,'c',3]
for index in range(len(myList)):
	print ("Object at {} is {}" .format(index,myList[index]))

print(list(range(6)))

myNumList=[11,22,4,45,3]
for a in myNumList:
	if a%2==0:
		print("%d is a even num" %a)
	else:
		print("%d is a odd num" %a)


