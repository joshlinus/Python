if 5 < 2:
    print("5 is greater than 2")
else:
    print("This is quantum math")
#this is a comment
'''
This 
is 
a 
multi
lined 
comment
'''
#Creating variables
x = 5
y = "5"
z = "Five"

#Printing Variables
print (x)
print (y)
print (z)

#Changing Variables
y = "Five"
print(y)

#String variables can be declared either by using single or double quotes
v = "John"
#is the same as
v = 'John'
print (v)

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:
#2myvar = "John"
#my-var = "John" #NO DASHES
#my var = "John"

#assign multiple values
x, y, z = "Cat", "Hat", "Mat"
print (x)
print (y)
print (z)

#assign multiple variables
B = N = M = "Letters"
print (B)
print (N)
print (M)

#Global variables
x = "the greatest"

def myfunc():
    print("I am " + x)

myfunc()

#Global variables pt 2
x = "the greatest"

def myfunc2():
    x = "AWESOME"
    print("I am " + x)

myfunc2()


#Global variables pt 3
x = "the greatest"

def myfunc3():
    global x 
    x = "AWESOME"
    print("I am " + x)

myfunc3()


