"""
(), **, *, /, %, +, -
"""
#Let's see an example with basic operators

print(11*3+44/2)
#In Other words if we divided this in terms of precedence
firstVal = 11*3
secondVal = 44/2
finalVal = firstVal+secondVal 
print (finalVal)


# (11-33*2/3)?
#(100/1+3**2)?
#(11-33)*2/3?
#(100/1)+3**2?

#Complex arithmetic operations
#(22*2+56)**2?
#(2*5-7)*10?
#(5.0 * (8+(16-2.0)/(4+1))/2)%4
print((5.0 * (8+(16-2.0)/(4+1))/2)%4)
a = 16-2.0
b = 4+1
c = a/b
d = 8
e = d+c
f = e/2
g = 5.0 * f
h = g%4
print(h) 


