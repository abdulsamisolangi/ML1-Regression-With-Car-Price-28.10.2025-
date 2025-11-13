'''Datatypes:

List - [ ], indexing, mutable(CRUD Operations), ordered #(CRUD=Creat, Read, Update, Delete)

Tuples - ( ), immutable, indexing, Fixed, Fast Operations, ordered  

Dictionaries {1:"rafay"} mutable, key:value pair (format), index (keys)

Sets {}, No index, mutable, unordered


#list

#numbers=[0,1,2,3]
numbers = [1,2,"rafay",20.4]
print(numbers[0])

num=[]
num1=["rafay",1,"umer"]
print(numbers[3])
num1.append(["Sheikh",2,0,1])

.append(arg):
to insert any value into the list
print(num1)


list1=[1,2,3,4,5,6,7,8,9]
list2=[1,2,3,4,5,6,7]

list2.reverse()
print(list2)


list1=[1,2,3,4,5,6,7,8,9]
list2=[1,2,3,4,5,6,7]

#list2.reverse()
#list1.unique()

list_unique=list(set(list1)) 	#unique is used to remove duplicate values.
print(list_unique)
    

list1=[1,2,3,4,5,6,7,8,9]
list2=[1,2,3,4,5,6,7]

#list1.extend(list2)
list1_extend= list(set(list2))
print(list1_extend)


num=[]

for i in range(1,10):
    val=int(input(f"enter number {i+1}"))
    num
    
    
list1=[1,2,3,4,5]
#list1=[0,1,2,3,4]
#list1=[-5,-4,-3,-2,-1]
#list1=list1.reverse()

for x in list1:
    print(list1[-1])


fruits=["apple", "banana", "grapes", "mangoe"]
fruits.reverse()

for x in fruits:
    print(x)

fruits=["apple", "banana", "grapes", "mangoe"]

fruits.remove("banana")
print(fruits)


fruits=["apple", "banana", "grapes", "mangoe"]

fruits.remove("banana")
print(fruits[2])

extend() #to extend list:

num=[1,2,3,4,]
num.extend([4,5,6,7,8,9])
print(num)

num=[1,2,3,4,]
num.append([4,5,6,7,8,9])
print(num)


num=[1,2,3,4,]
num.append([4,5,6,7,8,9])
print(num[4][1])


user1=[]
un=input("Enter your username")
password=input("Enter your password")
user1.append([un,password])
print(user1)'''

