In Python, "decision making" refers to the ability of a program to execute different blocks of code based on whether certain conditions are met. This allows for dynamic and responsive programs that can adapt their behavior to various inputs or situations.
Python provides several statements to implement decision-making logic:
if statement: This is the simplest form. A block of code indented beneath an if statement will execute only if the specified condition evaluates to True.
Python

    age = 18
    if age >= 18:
        print("You are eligible to vote.")
if-else statement: This extends the if statement by providing an alternative block of code to execute if the initial condition evaluates to False.
Python

    number = 7
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
if-elif-else statement (or if-else if-else chain): This allows for handling multiple conditions sequentially. The program checks each elif condition in order, and the first block whose condition evaluates to True is executed. If none of the if or elif conditions are met, the else block (if present) is executed as a fallback.

"Nested if"
A nested if statement in Python refers to an if statement that is placed inside another if or else block. This allows for more complex and hierarchical decision-making within your code.
How it works:
The outer if statement's condition is evaluated first.
If the outer condition is True, the code block associated with it is executed, and this block can contain another if statement (the nested if).
The nested if statement's condition is then evaluated. If it's True, its corresponding code block is executed.
If the outer condition is False, the else block (if present) of the outer if statement is executed, and this else block can also contain a nested if statement.
Example:
Python

age = 25
has_license = True

if age >= 18:  # Outer if statement
    print("You are old enough to drive.")
    if has_license:  # Nested if statement
        print("You also have a license, so you can drive legally.")
    else:
        print("You are old enough, but you need a license to drive legally.")
else:
    print("You are not old enough to drive.")
In this example, the inner if statement (checking has_license) is only evaluated if the outer if statement (checking age >= 18) is True.
This demonstrates how nested if statements allow for conditional execution based on multiple layers of criteria.


"Multiple operators" in Python refers to the use of more than one operator within a single expression or statement. When multiple operators are present, Python follows specific rules to determine the order in which they are evaluated. These rules are known as operator precedence and associativity.
Operator Precedence:
Python assigns a precedence level to each operator. Operators with higher precedence are evaluated before operators with lower precedence. For example, multiplication and division generally have higher precedence than addition and subtraction.
Python

result = 5 + 3 * 2  # Multiplication (3 * 2) is evaluated first, then addition
# result will be 11 (5 + 6)


"Relational/Comparison Operators"
In Python, "relational operators" are synonymous with "comparison operators." These operators are used to compare two values or operands and determine the relationship between them. The result of a comparison operation is always a Boolean value: True if the relationship holds, and False otherwise.
Here are the six common relational/comparison operators in Python:
Equal to (==): Checks if two operands are equal.
Python

    print(5 == 5)  # True
    print(5 == 10) # False
Not equal to (!=): Checks if two operands are not equal.
Python

    print(5 != 10) # True
    print(5 != 5)  # False
Greater than (>): Checks if the left operand is greater than the right operand. 
Python

    print(10 > 5)  # True
    print(5 > 10)  # False
Less than (<): Checks if the left operand is less than the right operand.
Python

    print(5 < 10)  # True
    print(10 < 5)  # False
Greater than or equal to (>=): Checks if the left operand is greater than or equal to the right operand.
Python

    print(10 >= 10) # True
    print(10 >= 5)  # True
    print(5 >= 10)  # False
Less than or equal to (<=): Checks if the left operand is less than or equal to the right operand.
Python

    print(5 <= 5)  # True
    print(5 <= 10) # True
    print(10 <= 5) # False
These operators are fundamental for controlling program flow through conditional statements (like if, elif, else) and loops, allowing programs to make decisions based on comparisons. They can be used with various data types, including numbers, strings, and even custom objects (if comparison methods are defined for them).
