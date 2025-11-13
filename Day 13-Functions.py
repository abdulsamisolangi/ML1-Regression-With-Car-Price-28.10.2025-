'''.Functions In Python:

1. create function def (def=define)
2. parameter
3. argument


def sm(a,b,):	#(parameter=a,b)
    add=a+b
    print(add)

sm(3,4)
(result will be 7)

def sm(a,b):
    add=a+b
    return add
 
print(sm(50,100))
(result will be 150)

def sm(a,b):
    sub=a-b
    print(sub)    

sm(5,6)
(result will be -1)

def a(a,b):
    add=a+b
    return add

def b(a,b):
    sub=a-b
    return sub    

def c(a,b):
    mul=a*b
    return mul

def d(a,b):
    div=a/b
    return divide



keyword searched: rafay
indexes[0,1]
count:2

list=["rafay","rafay", "hello"]
ke="rafay"

user=input("Enter a keyword you want to search:")
indexes = []

for i in range(len(list)):
    if list[i] == user:
        indexes.append(i)
        
if indexes:
    print(f"keyword: {user}")
    print("idexes: ", indexes)
    print("count", list.count(user))

else:
    print("keyword not found")

(the result will be
keyword: rafay
idexes:  [0, 1]
count 2)

def extnd(a,b,):
    extended=a+b
    return extended

list1=["Rafay", "hello",123]
list2=[1,2,3,4,5,6,7]

print(extnd(list1,list2))
'''