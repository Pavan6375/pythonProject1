from numpy import *
arr = zeros(5)
print(arr)
brr = ones(20)
print(brr)
crr = arange(1,10)
print(crr)
dee = array([1,2,3,4],"i")
print(dee)
#dee.dtype()
print(dee)

def add(x,y):
    c= x+y
    return c

result = add(6,7)
print(result)

def greet(name):
    print("hello goodmornig")
    print(name, "welcome to office")

greet("pavan")
greet("ruchi")

def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i,"=",j)


person("pavan",age=26, city ="edison", mpb = 99999, lover = "ruchi")

def fact(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f

result = fact(5)
print(result)

z = 7
a =0
b=1
for i in range(2,z):
    z = a+b
    a= b
    b=z
    print(z)

import math
print(math.factorial(5))
list =[4,5,6,7,8]
print(math.sqrt(



