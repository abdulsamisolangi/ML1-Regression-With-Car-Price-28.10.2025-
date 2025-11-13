'''CONCATENATION:

    Concatenation in Python refers to the process of joining two or more
sequences (such as strings, lists, or tuples) end-to-end to form a single,
longer sequence. While it applies to various data types, it is most commonly
associated with string manipulation.

Here's how concatenation works with strings in Python:

i)	USING THE + OPERATOR: 
This is the most straightforward method for concatenating strings.
	
string1='Hello'
string2='World'
string3=string1+string2
print(string3)
(The result will be HelloWorld)


ii)	USING THE += OPERATOR:
		This operator concatenates a string to an existing string variable and
	assigns the result back to the same variable.

message = "Good"
message += " morning"
print(message)
(The result will be Good morning)


iii) USING THE JOIN() METHOD: 
        The join () method is particularly efficient for concatenating a list of
     strings, especially when dealing with a large number of strings. It takes
     an iterable (like a list or tuple) of strings as an argument and joins them
     using the string on which the method is called as a separator.

words = ["Python", "is", "fun"]
sentence = " ".join(words)
print(sentence)
(The result will be Python is fun)


iv)	USING F-STRINGS (FORMATTED STRING LITERALS): 
        F-strings offer a concise and readable way to embed expressions inside
    string literals, effectively performing concatenation.

name = "Alice"
age = 30
greeting = (f"Hello, {name}! You are {age} years old.")
print(greeting)
(The result will be Hello, Alice! You are 30 years old.)


v)	USING THE FORMAT() METHOD: 
        This method provides another way to format strings and insert values into
    placeholders.
  
item = "apple"
price = 1.50
description = "The {} costs ${:.2f}.".format(item, price)
print(description)
(the result will be The apple costs $1.50.)'''
