'''L1-TAKING INPUT FROM THE USER:

name = input("Enter Your name: ")
print("Hello," + name) 	#name= Lala
(The result will be Hello,Lala)

name = input("Enter Your name: ")
print("Hello," + name)
print(type(name)) 		#name= Lala
(The result will be Hello,Lala)
<class 'str'>


a)	TAKING INPUT FROM THE USER AS INTEGER:

num = input("Enter a number:")
print(num)			#number=5
(The result will be 5)

num = input("Enter a number: ")
print(num)
print(type(num))	#number=5
 (The result will be 5)
<class 'str'>

num = int(input("Enter a number: "))
print(num)
print(type(num))	#number=5
num=num+2
print(num)
(The result will be 5
<class 'int'>
7)

    “When adding num with numeric value then you have to add int with
input i.e. called type Operators in Python.”


b)	TAKING INPUT FROM THE USER AS FLOAT: 

(float=value in decimals i.e. 0.0 etc.)

num = float(input("Enter a number: "))
print(num)			#number=5
 (The result will be 5.0)

num = float(input("Enter a number: "))
print(type(num))	#number=5

(The result will be <class 'float'>)

num = float(input("Enter a number: "))
num=num+2
print(num)			#number=5
(The result will be 7.0)


c)	TAKING INPUT FROM THE USER AS BOOL:

    While bool means true or false. If we do not enter any number in the box
(i.e. num value), it will show false.

num = bool(input("Enter a number: "))
print(num)		#number=5
(The result will be True)

num = bool(input("Enter a number: "))
print(type(num))	#number=5
(The result will be <class 'bool'>)'''