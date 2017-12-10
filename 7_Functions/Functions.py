#Functions
'''def functionname( parameters ):
   "function_docstring"
   return [expression]'''

# Function definition is here


def printVal( val ):
   #"This prints a string in this function"
   print (val)
   return 1000

# Now you can call printme function
printVal("calling user defined function first time.")
printVal("calling user defined function second time.")
mystr = printVal(val='A')
print(mystr)

def changeTheList( _mylist1 ):
   print ("Values inside the function before change: ", _mylist1)
   _mylist1[1]="Prasanth"
   _mylist1[2]="Theja"
   print ("Values inside the function after change: ", _mylist1)
   return

# Now you can call changeme function
mylist = ['Krish','Stellent','soft']
changeTheList( mylist )
#changeTheList()
print ("Values outside the function: ", mylist)
# Function definition is here
def printinfo( arg1, *vartuple):
   print ("Output is: ")
   print (arg1)
   print (vartuple)
   print (arg1)
   for var in vartuple:
      print ("In the loop",var)
   return

# Now you can call printinfo function
#printinfo( 10 )
printinfo( 70, 60, 50,'abc' )


def personalInfo( name, age = 31 ):
   print ("Name: ", name)
   print ("Age: ", age)
   return;

# Now you can call printinfo function
personalInfo( age=24, name="John" )
personalInfo( name="Michael" )

'''[{'name': 'John Haden','city'='NY'},\
{'name': 'Michael Jordan','city'='MI'},\
{'name': 'Tely Haden','city'='NY'}\
{'name': 'Rozer Rozers','city'='MIA'}\
{'name': 'Michael Gitter','city'='NY'}\
{'name': 'Bob Jonson','city'='MIA'}]'''


def myCustomFun(a,b):
   c=a+b
   print("a is", a)
   print("b is", b)
   print("Result is", c)

myCustomFun(b=2,a=7)

