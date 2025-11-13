'''#reversing list:
cars=["Mehran", "Civic", "Suzuki"]
cars.reverse()
print(cars)

#sort:
numbers=[40,10,30,20]
numbers.sort()	#by default asc (ascending) order
print(numbers)

cars=["Mehran", "Civic", "Suzuki"]
cars.sort()
print(cars)	#by default asc (ascending) order

numbers=[40,10,30,20]
numbers.sort(reverse=True)	#desc(descending) order
print(numbers)

cars=["Mehran", "Civic", "Suzuki"]
cars.sort(key=len, reverse=True)
print(cars)

#pop:
numbers=[40,10,30,20]
popped=numbers.pop(1)
print(f"{numbers}\n{popped}")	#pop is used to remove & return an element.

cars=["Mehran", "Civic", "Suzuki"]
popped=cars.pop(1)
print(f"{cars}\n{popped}")	


#copying list:
cars=["Mehran", "Civic", "Suzuki"]
copy_cars=cars.copy()	#shallow copy
print(copy_cars, cars)


#joining a list:
cars=["Mehran", "Civic", "Suzuki"]
carss=[1,2,3,4,5]
print(cars+carss)


#comprehension of list:
squares=[x**2 for x in range(1,6)]
print(squares)


even_list=[x for x in range(1,20) if x%2==0]
print(even_list)	#for even list

odd_list=[x for x in range(1,20) if x%2!=0]
print(odd_list)		#for odd list


list=['apple', 'orange', 'banana', 'papaya', 'mango']
uc_lst = [x.upper() for x in list]
print(uc_lst)	#for upper case of characters.


list=['apple', 'orange', 'banana', 'papaya', 'mango']
uc_lst = [x.capitalize() for x in list]
print(uc_lst)	#capitalization of characters.

list=['APPLE', 'ORANGE', 'BANANA', 'PAPAYA', 'MANGO']
uc_lst = [x.lower() for x in list]
print(uc_lst)	#for lower case of characters.


list=['apple', 'orange', 'banana', 'papaya', 'mango']
for x in list:
    print(x)

#list iteration:
fruits=['apple', 'orange', 'banana', 'papaya', 'mango']
index=0
while index < len(fruits):
    print(fruits[index])
    index += 1


fruits=['apple', 'orange', 'banana', 'papaya', 'mango']
index=0
while index < len(fruits):
    print(fruits[index])
    lst=fruits[index]
    for x in lst:
        print(x)	#for breaking the characters in loop
    index += 1	


# num=[1,9,19,10,11]


fruits=['apple', 'orange', 'banana', 'papaya', 'mango']
index=0
while index < len(fruits):
    print(fruits[index])
    lst=fruits[index]
    for x in lst:
        print(x)	#for breaking the characters in loop
    index += 1


sort=[]
sort.extend("rafay")
print(sort)   #for breaking every alphabet


#for breaking & again joining every alphabet:

#step 1
sort=[]
sort.extend("rafay")
print(sort)

sort1=['r', 'a', 'f', 'a', 'y']
sort1=["".join(sort1)]
print(sort1)

the result will be:
['r', 'a', 'f', 'a', 'y']
['rafay']	

#step 2
sort=[]
sort.extend("rafay")
print(sort)
sort=["".join(sort)]
print(sort)

the result will be:
['r', 'a', 'f', 'a', 'y']
['rafay']

#replace:

cars=["Mehran", "Civic", "Suzuki"]
print("current list" , cars)
x=input("Enter a character you want to remove:")

ul=[y.replace(x, "") for y in cars]	#ul=updated list
print("updated list",ul)	

the result will be:
current list ['Mehran', 'Civic', 'Suzuki']
Enter a character you want to remove:a
updated list ['Mehrn', 'Civic', 'Suzuki']


ch=input("Which character you want to remove:")	#ch=character
lst=[]
while True:
    user=input("Enter an element to add:")
    user2=user.replace(ch,"")
    lst.append(user2)
    print(lst)

the result will be:
    Which character you want to remove:@
    Enter an element to add:lalsami1880@gmail.com
    ['lalsami1880gmail.com']	'''

