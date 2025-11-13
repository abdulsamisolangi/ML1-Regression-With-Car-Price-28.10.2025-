'''Dictionaries in python:

syntax:
    
my_dictionary = {"key": "value", "key2": "value"}

age=20 (age=key & value=20)

course={'course':'AI / ML', 'instructor': 'Rafay', 'institute': 'youexcel'}
print(course)
print(type(course))

the result wil be:
{'course': 'AI / ML', 'instructor': 'Rafay', 'institute': 'youexcel'}
<class 'dict'>


#constructing dictionaries:

course2=dict(name='rafay', age=28, training="AI/ML")
print(course2)
print(type(course2))

the result will be:
{'name': 'rafay', 'age': 20, 'training': 'AI/ML'}
<class 'dict'>


course3=dict[('name','rafay'),('age',28), ('training','AI/ML')]
print(course3)
print(type(course3))

the result will be:
dict[('name', 'rafay'), ('age', 28), ('training', 'AI/ML')]
<class 'types.GenericAlias'>


Accessing Dictionay Values:

course={'course': 'AI / ML', 'instructor': 'Rafay', 'institute': 'youexcel'}
print(course['instructor'])

result will be:
Rafay

only keys:

course={'course': 'AI / ML', 'instructor': 'Rafay', 'institute': 'youexcel'}
print(course.keys())

the reult will be:
dict_keys(['course', 'instructor', 'institute'])

only values:
course={'course': 'AI / ML', 'instructor': 'Rafay', 'institute': 'youexcel'}
print(course.values())

the result will be:
dictdict_values(['AI / ML', 'Rafay', 'youexcel'])


total items:
course={'course': 'AI / ML', 'instructor': 'Rafay', 'institute': 'youexcel'}
print(course.items())

the result will be:
dict_items([('course', 'AI / ML'), ('instructor', 'Rafay'), ('institute', 'youexcel')])


#.get()
course={'course': 'AI / ML', 'instructor': 'Rafay', 'institute': 'youexcel'}
print(course.get('email', 'Not available'))

the result will be:
Not available


#to add item in dictionary:
course={'course': 'AI / ML', 'instructor': 'Rafay', 'institute': 'youexcel'}
course['email'] = "rafayshaikh@gmail.com"
print(course)

the result will be:
{'course': 'AI / ML', 'instructor': 'Rafay', 'institute': 'youexcel', 'email': 'rafayshaikh@gmail.com'}


#to modify item in dictionary:
course={'course': 'AI / ML', 'instructor': 'Rafay', 'institute': 'youexcel'}
course['email']= "rafay@ssuet.edu.pk"
print(course)

the result will be:
{'course': 'AI / ML', 'instructor': 'Rafay', 'institute': 'youexcel', 'email': 'rafay@ssuet.edu.pk'}

#to delete item in dicitonary:
course={'course': 'AI / ML', 'instructor': 'Rafay', 'institute': 'youexcel'}
course['email']= "rafay@ssuet.edu.pk"
print(course)
del course['course']
print(course)

the result will be:
{'course': 'AI / ML', 'instructor': 'Rafay', 'institute': 'youexcel', 'email': 'rafay@ssuet.edu.pk'}
{'instructor': 'Rafay', 'institute': 'youexcel', 'email': 'rafay@ssuet.edu.pk'}

course={'course': 'AI / ML', 'instructor': 'Rafay', 'institute': 'youexcel'}
print(course)
print(course.pop('course'))

the result will be:
{'course': 'AI / ML', 'instructor': 'Rafay', 'institute': 'youexcel'}
AI / ML

# iteration in dictionary:
course={'course': 'AI / ML', 'instructor': 'Rafay', 'institute': 'youexcel'}
for keys in course:
    print(keys)	#for keys.
    
the result will be:
course
instructor
institute


course={'course': 'AI / ML', 'instructor': 'Rafay', 'institute': 'youexcel'}
for value in course:
    print(course[value])	#for values

the result will be:
AI / ML
Rafay
youexcel


course={'course': 'AI / ML', 'instructor': 'Rafay', 'institute': 'youexcel'}
for x in course:
    print(course[x])	#for values

the result will be:
AI / ML
Rafay
youexcel


course={'course': 'AI / ML', 'instructor': 'Rafay', 'institute': 'youexcel'}
for value in course.values():
    print(value)

the result will be:
AI / ML
Rafay
youexcel

#loop through both key-value pair:
course={'course': 'AI / ML', 'instructor': 'Rafay', 'institute': 'youexcel'}
for keys, value in course.items():
    print(keys, value)

the result will be:
course AI / ML
instructor Rafay
institute youexcel

#nested dictionaries:
uni={'student1':{'name': 'M.Rafay','age':28},
     'student2':{'name': 'Syed Sameer Ali','age':35},
     'student3':{'name':'Fakiya Siddiqui','age':27}

        }

print(uni['student2'])

the result will be:
{'name': 'Syed Sameer Ali', 'age': 35}


clg={'student1':{'name': 'Khalid','age':30},
     'student2':{'name': 'Sultan','age':35},
     'student3':{'name':'Arsalan','age':40}

        }

print(clg['student3'])

the result will be:
{'name': 'Arsalan', 'age': 40}


yetc={'Ai teacher':{'name': 'Rafay','age':30},	#yetc=youexcel training centre
     'Cc teacher':{'name': 'Jahanzaib','age':35},
     'Owner':{'name':'Farhan Qazi','age':44}

        }

print(yetc['Owner'])

the result will be:
{'name': 'Farhan Qazi', 'age': 44}


clg={'student1':{'name': 'Khalid','age':30, 'class' :{'Section':'C'}},	#nested dictionary
     'student2':{'name': 'Sultan','age':35, 'class' :{'Section':'B'}},
     'student3':{'name':'Arsalan','age':40, 'class' :{'Section':'A'}},

        }

print(clg['student1']['class']['Section'])

the result will be:
C'''
