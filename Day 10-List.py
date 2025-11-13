'''list

my_list = [1,2,3,4]
print(my_list)
(result=[1, 2, 3, 4])


list3 = [1,2,3,4,[1,2,3],["rafay","shaikh"]]
print[list3]

#to access an elements from the list
list3 = [1,2,2,3,4,[1,2,3],["rafay","shaikh"]]
#list3=[0, 1, 2, 3, 4,    5,     ,       6]
#list3=[ -7, -6, -5, -4, -3,     -2,     -1] #reversion of list]
print(list3[5][0])


#list - slicin:

list3 = [1,2,3,4,[1,2,3],["rafay","shaikh"]]
print(list3[0:5:2])

list4=[1,2,3,4,5,[6,7],[9,10]]
print(list4[0:6:1])

list4=[1,2,3,4,5,[6,7],[9,10]]
print(list4[::-1])	#reversion of slicin list


#replace elements
cars=["Mehran", "Civic", "Suzuki"]
print(cars)
cars[2] = "Honda"
print(cars)

#append
cars=["Mehran", "Civic", "Suzuki"]
print(cars)
cars[2] = "Honda"
cars.append("hello")
print(cars)

#remove
cars=["Mehran", "Civic", "Suzuki"]
print(cars)
cars[2] = "hello"
cars.remove("hello")
print(cars)

#extend
cars=["Mehran", "Civic", "Suzuki"]
print(cars)
cars.extend(["hello"])
print(cars)

#insert
cars=["Mehran", "Civic", "Suzuki"]
print(cars)
cars.insert(2,"corolla")
print(cars)

#clear

cars=["Mehran", "Civic", "Suzuki"]
print(cars)
cars.clear()
print(cars)

#finding index - within a range of elements:

cars=["Mehran", "Civic", "Suzuki"]
print(cars)
index = cars.index("Suzuki")
print(cars.index("Suzuki"))

#finding index - within a range:

print(cars)
cars2=['Mehran', 'Suzuki', 'Civic', 'Corolla', 'Alsvin']
print(cars2.index("Alsvin"))

cars2=['Mehran', 'Suzuki', 'Civic', 'Corolla', 'Alsvin']
print(cars2.index("Alsvin",4))


#count

cars2=['Mehran', 'Suzuki', 'Mehran', 'Civic', 'Mehran', 'Corolla', 'Alsvin']
print(cars2.count("Mehran"))


#check

cars2=['Mehran', 'Suzuki', 'Civic', 'Corolla', 'Alsvin']
print(cars2)
check=input("which one you want to check")

if check in cars2:
    (cars2.index(check))
    
    
    
keyword: suzuki
indexes: 1,3,6
count= 3

#Step 1:

cars2=['Mehran', 'Suzuki', 'Civic','Suzuki', 'Corolla','Alsvin', 'Suzuki', 'Camry', 'Passo', 'Yaris']
print(cars2)

user=input("Enter a keword you want to search:")
indexes = []

for i in range(len(cars2)):
    if cars2[i] == user:
        indexes.append(i)
        
if indexes:
    print(f"keyword: {user}")
    print("idexes: ", indexes)
    print("count", cars2.count(user))

else:
    print("keyword not found")


#Step 2:
    
cars2=['Mehran', 'Suzuki', 'Civic','Suzuki', 'Corolla','Alsvin', 'Suzuki', 'Camry', 'Passo', 'Yaris']
print(cars2)

user=input("Enter a keword you want to search:")
indexes = []

for i in range(len(cars2)):
    if cars2[i] == user:
        indexes.append(i)
        
if indexes:
    print(f"keyword: {user}")
    print("idexes: ", ", ".join(map(str, indexes)))
    print("count", len(indexes))

else:
    print("keyword not found")'''