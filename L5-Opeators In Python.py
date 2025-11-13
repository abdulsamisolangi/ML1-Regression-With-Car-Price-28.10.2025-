'''L5-OPEATORS IN PYTHON:
These Operators are used to perform Arithmetic Operations, such as
Addition, Subtraction, Division, Floor Division, Modulus, Multiplication
and Exponentiation.
The Operators are:

a)	ARITHMETIC OPERATOR:

+ Addition:
(e.g. 5+4=9)

- Subtraction:
 (e.g. 5-4=1)

* Multiplication:
(e.g. 5*4=20)

/ Division:	
(e.g. 15/3=5)

// Floor Division: 
(e.g. 15//4=3.75 then the floor division (//) will be lower
    value i.e. 3)

% Modulus (Modulus=Remainder):
(e.g. 10%2=0), (e.g. 10%3=1), (e.g. 10%1=0), (e.g. 10%0=error)

** Exponentiation (Power):
(e.g. 2**=8)

PRIORITY OF ARITHMETIC OPERATORS:

    **>*,/,//,%>=+-
    
   1st Priority= ** (i.e. Exponent) 
(Always solve right to left)

   2nd Priority= *,/,//,% (i.e. Mul, Div, F Div, Mod)
(Always solve left to right)

   3rd Priority= +- (i.e. Add, Sub) 
(Always solve left to right)

FOR EXAMPLE:

    2**4//3*2+3-5
    16//3*2+3-5
    5*2+3-5
    10+3-5
    13-5
    8


b)	LOGICAL OPERATORS:
    In Python, logical operators are used to combine multiple conditions or
expressions and produce a boolean result.

There are three logical operators:
        
i) and:
It returns True if both the operands are True, otherwise it returns
 False.

ii) or:       
It returns True if at least one of the operands is True,   otherwise it returns False.
            
iii) not:       
It returns the opposite Boolean value of the operands. If the operand is True, it returns false, and if the operand is false, it returns True.

OPERANDS:
In Python, an operand refers to the value or variable upon which an operator performs an operation. Operators are special symbols or keywords that carry out specific tasks, such as arithmetic calculations, comparisons, or logical evaluations.

EXAMPLE:
Consider the expression:
Python
result = 5 + 3

In this example:
•	5 is an operand.
•	3 is an operand.
•	+ is the operator (addition operator).
•	result is the variable where the outcome of the operation is stored.

    Essentially, if an operator is performing an action, the operand is the "target"
or "subject" of that action.

i)	and:

age=15
income=20000

if age>=12 and income>=15000:
    print("Eligible for Loan")
    
else:
    print("Not Eligible")
(The result will be Eligible for Loan because both the operands are True).

ii)	or:
age=15
income=20000

if age>=19 and income>=15000:
    print("Eligible for Loan")
    
else:
    print("Not Eligible")
(The result will be Not Eligible because if operand is false).

iii) not: 

a=True
b=False

if not a:
    print("My name is a") #This will not Executed    
if not b:
    print("My name is b")
(The result will be My name is b because It returns the opposite Boolean value).

    
c) Relational / Comparison operators:

== (left side equal to right side)
!=(left side is not equal to right)
> (left side is greater than right)
< (right side is less than left)
>=(left side is greater than equal to right)
<=(right side is less than equal to left)

print(4>6==False)
    False==False
    False (result)

True==True==False
True==False
False (result)


d)	MEMBERSHIP OPERATORS:

.	These Operators are used to test whether a specific value or item is
    present within a sequence, such as a string, list, tuple or set.

.	There are two membership operators: “in” & “not in”.
    Whereas: (in=include) & (not in=not Included)

.	Always return as ‘True or False” as output.

Example:

list1=[1,2,3,4,5]
1 in list1 
(The result will be “True”) #Because 1 is included in list

list1=[1,2,3,4,5]
10 in list1 
(The result will be “False”) #Because 1 is not included in list

list1=[1,2,3,4,5]
10 not in list1 
(The result will be “True”) #Because 10 is not included in list


reg_user=[“Lala”, “Sami”, “Sarang”, “Tahir”]
Name=input(“Enter Your Name”)

If name in reg_user:
	Print(“Access Granted, Welcome”)
else:
	Print(“Access Denied, You are not registered”)'''

