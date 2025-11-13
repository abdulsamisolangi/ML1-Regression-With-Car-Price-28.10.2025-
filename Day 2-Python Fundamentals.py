Python Fundamentals:
variables in python:
    
print ("hello"+"world")
name="rafay"
print ("name",name)

num=123
print(num+num*num/num)

a="hello"
b="world"
print (a+b)

a=1
b=2
c=3
quad=(-b+((b**2)-4*a*c)**(1/2))/(2*a)
print (quad)

a=2
b=3
quad = a**2 + 2*a*b +b*2
print (quad)

pi=3.142
r=5
areaofcircle = (pi * r**2) #pi=3.142
print (areaofcircle)

variables in variable:
    
num1=50
num2=100
print(num1+num2)

e=5
m=10
c=20
e=(m c**2) #energy
print(e)

num1=int(input("Enter a first value:"))
num2=int(input("Enter a 2nd value:"))

add=num1+num2
sub=num1-num2
div=num1/num2
mul=num1*num2
print("This is Addition:",add,"/n This is Substraction:",sub,"/n This is Division:",div,"/n This is Multiplicatiton:",mul)

Quad1= + (a,b,c)
Quad2= -
AOC= (pi,r)
(a+b)**2 (a,b)

a1=int(input("Quad1 value of a1"))
b1=int(input("Quad1 value of b1"))
c1=int(input("Quad1 value of c1"))

a2=int(input("Quad2 value of a2"))
b2=int(input("Quad2 value of b2"))
c2=int(input("Quad2 value of c2"))

pi=3.142
r=5
quad1 = (a1**2 + 2*a1*b1 +b1*2)
quad2 = (a1**2 - 2*a1*b1 +b1*2)
print ("answer of quad1:",quad1)
print ("answer of quad2:",quad2)

Data types in python
int- Numeric (Whole number) 0,1,2,3,4 ....

print (123+123)

Operators in python:
    
Arithmetic operator:
+,
-,
/,
%,
//,
*,
**




Logical Operators:
and, or, not

relationoal / comparison operators:

== (left side equal to right side)
> (left side is greater than right)
< (right side is greater than left)
>=
<=
!=
in

shafi=26
sami=35

check=shafi==sami
print(check)

(space is called in python as indentation)


Decisions in python:

if  always works or true conditions
else always welcomes false condtions

Marksheet:

obtain=int(input("Enter your obtained marks:"))
total=500
per=(obtain/total)*100

if per >80:
    print("A+,and Percentage is:",per)
elif per>=70:
    print("A,and Percentage is:",per)
elif per >60:
    print("B,and Percentage is:",per)
elif per >50:
    print("C,and Percentage is:",per)
else:    
    print("Fail",per)